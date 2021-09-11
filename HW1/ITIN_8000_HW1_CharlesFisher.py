# Let's add a timestamp. How?
# datetime module import is an option, yeah?
from datetime import datetime

# get today's timestamp
today = datetime.now()
# print(today)
# used printline above to test that this badboi was werkin. It is.

# extract the monthly name from today's date as a string and store as a variable for later
# https://www.programiz.com/python-programming/datetime/strftime
# use above as shown in class
month_name = today.strftime('%B')  # Laternote: keep track of your %format marker

# extract day of month as a number
# day_number = today.day
day_number = 10
print(day_number)

# if the day is 1, 21, or 31, define suffix variable as st
# if 2 or 22 set as nd
# if 3 or 23 set as rd
# otherwise set as th

if day_number == 1 or day_number == 21 or day_number == 31:
    suffix = "st"
elif day_number == 2 or day_number == 22:
    suffix = "nd"
elif day_number == 3 or day_number == 23: \
        suffix = "rd"
else:
    suffix = "th"

print(suffix)

# Extract the year as a number from today's date
year_number = today.year

# Multiply year number by(times) the day number and
# determine if the result number's modulus of 2 is zero (it's even) and define the day_type as "even"
# else, define as "odd"

if (year_number * day_number) % 2 == 0:
    day_type = "even"
else:
    day_type = "odd"

# print the hello statement as defined below:
# “Hello. Todays Date is [Month Name] [Day Number][th/nd/st/rd] of [Year].
# # The product of the month and day is [Month Number * Day], which is an [Odd/Even] number.
print('Hello. Todays date is', month_name, str(day_number) + suffix, 'of',
      str(year_number) + '. The product of the month and day is', str(today.month * day_number), 'which is an',
      day_type, 'number.')

# create a new line to print to
# print "if you counted..."
print('If you counted the days this month so far you would have:')

# LOOP THYME
n = 1
while n <= day_number:
    print(n)
    n += 1

print("days.")
