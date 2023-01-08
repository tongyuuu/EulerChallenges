

import calendar

p = calendar.setfirstweekday(6)

def sundaycount(year):
    counter = 0
    for month in range(1,13):
        cal = calendar.monthcalendar(year,month)
        if cal[0][0]:
            counter = counter + 1
    return counter

total = 0
for s in range(1901,2001):
    total = total + sundaycount(s)

print(total)

