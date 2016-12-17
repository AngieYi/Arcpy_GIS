# yi_hongyan_lab1_part3.py
# Purpose:  implement python basic sytax and grammers, string, math, date and time, function and dot notation
# Author:  Hongyan Yi
# Inputs: None
# Outputs:   Prints to console
# Instructions:  
#   1. In a terminal window anchored in your directory, start python.exe (C:\Python27\ArcGIS10.2\python.exe)
#	2. At the Python prompt, type:  execfile("yi_hongyan_lab1_part3.py")
#	3. This file finish three tasks,the content of each task was commented at the beginning.


#  Lab 1.part3
from datetime import date
from datetime import datetime, timedelta
from calendar import monthrange


# task1: caculate and show days delta of two date with string operators
today_date = date.today()           # Return the current local datetime, with tzinfo None.
birth_date = date(2015,9,18)        # format: can use day with 0 : date(1985,12,05), cannot use month with 0: date(2015,09,18) 
interval = today_date - birth_date
str_interval = str(interval)
index = str_interval.find("days")
str_interval_days = str_interval[:index + 4]        # get string from beginning to the end of days 
print "\nNow Alex was born %s" %(str_interval_days) # use string to show days


# task2: caculate and show days delta of two date
end_of_term = date(2016,3,18)
interval = end_of_term - today_date
interval_days = interval.days       # get int days from date
print "This term has %d days left" %(interval_days) 


# task3: caculate and show months delta of two date
# algorithm: find the days of d1.month,add the days to d1 until d1<=d2, the times of loop is the month delta 
def monthdelta(d1, d2):     # by defalut d1 < d2
    delta = 0
    while True:             # use loop: while True,if-else-break 
        mdays = monthrange(d1.year, d1.month)[1]    # calendar.monthrange(year, month)Returns weekday of first day of the month and number of days in month, for the specified year and month.
        d1 += timedelta(days = mdays)               # convert int to date: datetime.timedelta, mdays datatype is int, use timedelta to transfer to date,
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

month_delta = monthdelta(birth_date,end_of_term)
print "After this term, Alex will be %d months old" %month_delta





