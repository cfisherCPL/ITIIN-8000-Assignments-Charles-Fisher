"""
HW pt1 Description Provided on Canvas
Ask for the users first and last name, favorite color, and date of birth
Calculate how many days old the user is
Write the user's name in the format last name, first name and favorite color in a .txt named UserName
Write the user's age in days to a binary file named Days Old
Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old
A file named hw3part1.py should perform these tasks when it is run
"""

# Import datetime (from datetime import date)
import datetime
from datetime import date
# Import csv
import csv


# prompt first name
fName = input("What is your first name? ")
# prompt last name
lName = input("What is your last name? ")
# prompt favorite color
fColor = input("What is your favorite color? ")

# prompt DoB
yearBorn = int(input("What year you were born? "))
monthBorn = int(input("What month you were born? (1-12) "))
dayBorn = int(input("What day you were born? (1-31) "))
# make sure to prompt with format note!

# Calculate how many days old the user is and stash as variable
bday = date(yearBorn, monthBorn, dayBorn)
today = date.today()

dateDif = today - bday
print('Days old = ' + str(dateDif.days))
daysOld = dateDif.days

# do the file work below here:
# create .txt file UserName with open()

userName = lName + ', ' + fName + ', ' + fColor
with open('UserName.txt', 'wt') as userNameOut:
    userNameOut.write(userName)

# Write the user's name in the format last name, first name
# and favorite color in a .txt named UserName
# close .txt file --> did this using 'with'!

# create and open filename.bin in wb mode
# Write the user's age in days to a binary file named Days Old
# close .bin file --> used 'with' again...
byteData = bytes(str(daysOld), 'utf-8')
print(len(byteData))

with open('DaysOld', 'wb') as fileOut2:
    fileOut2.write(byteData)


# create list from user input as shown:
# Last Name, First Name, Favorite Color, Days Old
userList = [lName, fName, fColor, daysOld]
# create and open filename.csv
# create the csv writer object
# use writer to write row from list

with open('UserData.csv', 'w') as fout:
    csvout = csv.writer(fout)
    csvout.writerow(userList)



# close csv

