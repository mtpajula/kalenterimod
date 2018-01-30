from gkalenteri import *
from icskalenteri import *
from reader import *


print('\nGet google calendar events\n')
go = input("y/n? ")
if go == 'y':
    gk = gkalenteri()
    gk.get()

print('\nDelete event with stamp [kalenterimod]\n')
go = input("y/n? ")
if go == 'y':
    gk.delete('[kalenterimod]','description')

print('\nDelete events containing string you give.\n')
go = input("y/n? ")
if go == 'y':
    q = input('in s(summary)/d(description)? ')
    if q == 's':
        key = 'summary'
    elif q == 'd':
        key = 'description'
    else:
        key = ''

    if key != '':
        d = input('delete string? ')
        if d != '':
            gk.delete(d, key)

print('\nGet events from ics-file (timeedit.ics)\n')
go = input("y/n? ")
if go == 'y':
    ics = icskalenteri()
    ics.get()
    ics.show()

print('\nClean summaries from ics (based on courses.txt) and add stamp to description\n')
go = input("y/n? ")
if go == 'y':
    r = reader()
    d = r.get()
    ics.fix_events_summary(d)
    ics.add_events_description_stamp()
    ics.show()

print('\nAdd ics-events to google calendar\n')
go = input("y/n? ")
if go == 'y':
   gk.add(ics.events)
