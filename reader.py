
'''
Reads tab separated table to dictionary:

Example:
Opintojakso			Tunnus		Toteutus	Laajuus
----------------------------------------------------------------------
Tekniikan alan viestintä 	R504T15A1	17001		5,00
Engineering English for IT 	R504T15C1	16001		5,00

Idea is to use this dictionary to replace course codes in ics summary
to more humar readable form.

'''
class reader:

    filepath = 'courses.txt'

    def get(self):
        a = open(self.filepath,'r',encoding="utf-8")

        data = []
        first = True

        while True:
            line = a.readline()
            if not line:
                break

            if first:
                first = False
                continue

            d = self.read_line(line)
            if d:
                data.append(d)

        #print(data)
        return data

    def read_line(self, line):
        data = None

        l = line.split('\t')
        #print(l)

        temp = []

        for c in l:
            out = c.replace('\n','').strip()
            if out != '':
                temp.append(out)

        if len(temp) >= 4:
            data = {}
            for i, t in enumerate(temp):
                if i == 0:
                    data['name'] = t
                elif i == 1:
                    data['code'] = t
                elif i == 2:
                    data['group'] = t
                elif i == 3:
                    data['op'] = t

        return data
