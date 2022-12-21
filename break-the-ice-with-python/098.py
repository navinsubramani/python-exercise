'''You are given a date. Your task is to find what the day is on that date.

Input

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

08 05 2015
Output

Output the correct day in capital letters.

WEDNESDAY'''

Date = input("Enter the date in MM DD YYYY format: ").split(" ")
MONTH = int(Date[0])
DAY = int(Date[1])
YEAR = int(Date[2])

import calendar
print(MONTH, DAY, YEAR)

DayID = calendar.weekday(YEAR, MONTH, DAY)
print(calendar.day_name[DayID])
