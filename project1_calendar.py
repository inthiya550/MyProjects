#importing the calandar module
import calendar
#taking input for the year and the month
year=int(input("enter the year"))
month=int(input("enter the month"))
#displaying the calendar by taking month and year from the user
calandar=calendar.month(year,month)
print(calandar)