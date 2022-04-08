#1. Conditional Basics

#a. prompt the user for a day of the week, print out whether the day is 
# Monday or not 
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

user_input = input('Which day of the week is it? ' )

if user_input == 'Monday':
    print('Today is Monday')
else:
    print(" It's not Monday!")

#b. prompt the user for a day of the week, print out whether 
# the day is a weekday or a weekend
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
user_input = input('Which day of the week is it? ' )
if user_input in weekdays:
    print("It's a weekday")
if user_input in weekend:
    print("It's a weekend!")
else:
    print("Please type a day of the week")
#c. create variables and make up values for
#       1. the number of hours worked in one week
weekly_hours = 80
#       2.the hourly rate
hourly_wage = 22
#       3. how much the week's paycheck will be
weekly_check = weekly_hours * hourly_wage
print(weekly_check)
#       4. write the python code that calculates the weekly paycheck. 
#           You get paid time and a half if you work more than 40 hours
if weekly_hours > 40:
     full_check = weekly_check * 1.5
print(full_check)

# 2. LOOP basics
#While
#Create an integer variable i with a value of 5.
i = 5
#Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:

#Each loop iteration, output the current value of i, then increment i by one.
    print(i)
    i += 4

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <= 100:
    print (i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= 0:
    print(i)
    i -= 5
#Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000.
i = 2
while i**2 < 10000000:
    print(i**2)
    i = i**2

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5

#b. For Loops
#Write some code that prompts the user for a number, then shows a multiplication 
# table up through 10 for that number.
# For example, if the user enters 7, your program should output:
int_multiplier = input(int)
for num in int_multiplier:
    print num * range(1,10
