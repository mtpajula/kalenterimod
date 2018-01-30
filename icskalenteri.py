from datetime import timezone, datetime

'''
Reads ics-calendarfile to dictionary.
That dictionary is in correct format for sending it to google calendar.

Also offers method to fix event summary
(timeedit calendar ics summary is a hot mess)
Also offers method to put stamp in desctiption for future easy removal.

'''
class icskalenteri:

    filepath = 'timeedit.ics'
    events = []

    def get(self):
        a = open(self.filepath,'r',encoding="utf-8")

        events = []
        event = []
        record = False

        while True:
            line = a.readline()
            if not line:
                break
            #print(line)

            if line.startswith('BEGIN:VEVENT'):
                record = True
                continue
            elif line.startswith('END:VEVENT'):
                self.set_event(event)
                record = False
                event = []

            if record:
                event.append(line)

    def set_event(self, eventlist):

        #print(eventlist)

        event = {}
        event['reminders'] = { 'useDefault': True }

        elements = ['DTSTART','DTEND','SUMMARY','LOCATION','DESCRIPTION',
                'UID','DTSTAMP','LAST-MODIFIED'
            ]

        prev = ''
        for line in eventlist:
            key = ''
            for e in elements:
                if line.startswith(e):
                    key = e.lower()
                    line = line.replace(e+':', '', 1)

            line = line.replace('\\n', ' ')
            line = line.replace('\n', '')
            line = line.replace('\\', '')

            if key != '':
                if key == 'dtstart':
                    event['start'] = {
                            'dateTime' : self.change_datetime(line)
                            #'timeZone' : 'Finland/Helsinki'
                        }
                elif key == 'dtend':
                    event['end'] = {
                            'dateTime' : self.change_datetime(line)
                            #'timeZone' : 'Finland/Helsinki'
                        }
                else:
                    event[key] = line
                prev = key
            else:
                if prev != '':
                    event[prev] = event[prev] + line

        self.events.append(event)

    def change_datetime(self, din):
        #20180206T061500Z
        #print(din)
        d_obj = datetime.strptime(din, '%Y%m%dT%H%M%SZ')
        d_obj = d_obj.replace(tzinfo=timezone.utc)

        #'dateTime': '2015-05-28T09:00:00-07:00',
        #'timeZone': 'America/Los_Angeles',

        dout = d_obj.__str__().replace(' ','T')
        #print(dout)
        return dout

    def fix_events_summary(self, replaces):
        for e in self.events:
            s = e['summary'].replace('.',',').split(', ')
            #print(s)

            # clean repeating info
            news = ''
            for p in s:
                if p in news and len(p) >= 5:
                    continue
                news += p + ' '

            news = news.replace('  ', ' ').strip()
            #print(news)

            #replace based on given replace-dict
            for r in replaces:
                news = news.replace(r['code'],r['name'])

            e['summary'] = news

    def add_events_description_stamp(self):
        for e in self.events:
            if 'description' in e:
                e['description'] = e['description'] + ' [kalenterimod]'
            else:
                e['description'] = '[kalenterimod]'

    def show(self):
        for e in self.events:
            print(e['start']['dateTime'] + '\t' + e['summary'])
            #print(e['description'])
