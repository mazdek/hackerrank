#!/bin/python
import sys

time = raw_input().strip()
if time[8] == 'P':
    sa = (int(time[0] + time[1]) + 12)
    if str(sa)[0] == '2' and str(sa)[1] == '4': 
        print '12' + time[2:8]
    else:
        print str(sa) + time[2:8]
elif time[8] == 'A':
    if time[0] == '1' and time[1] == '2':
        print '00' + time[2:8]
    else:
        print time[0:8]
