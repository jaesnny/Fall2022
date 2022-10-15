#JenniferChu
#1873159

import datetime

start = open('/Users/jennychu/inputDates.txt', 'r')
stop = open('/Users/jennychu/parsedDates.txt', 'w')

months = {"January":"1", "February": "2", "March":"3", "April":"4", "May":"5", "June":"6", "July":"7", "August":'8', "September":"9", "October":"10", "November":"11", "December":"12"}

for i in start:
    if i is not '-1':
        splitlines = i.split()
        if len(splitlines) >= 3:
            mm = splitlines[0]
            dd = splitlines[1]
            yyyy = splitlines[2]
            if mm in months:
                comma = dd[-1]
                if comma == ",":
                    dd = dd[:len(dd)-1]
                    mm_num = months[mm]
                    date_today = datetime.date.today()
                    file_date = datetime.date(int(yyyy), int(mm_num), int(dd))
                    date_diff = date_today - file_date
                    if date_diff.days >= 0:
                        finish = mm_num + '/' + dd + '/' + yyyy
    else:
        break
start.close()
stop.close()