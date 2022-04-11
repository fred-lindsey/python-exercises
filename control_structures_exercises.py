import pandas as pd

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
     overtime_pay = hourly_wage * 1.5
     weekly check = weekly_hours * hourly_wage
     total_pay = weekly_check + (weekly_hours - 40) * overtime_pay
print(total_pay)

# 2. LOOP basics
#While
#Create an integer variable i with a value of 5.
i = 5
#Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:

#Each loop iteration, output the current value of i, then increment i by one.
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <= 100:
    print (i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
#Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000.
i = 2
while i < 10000000:
    print(i)
    i = i**2

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5

#b. For Loops
#Write some code that prompts the user for a number, then shows a multiplication 
# table up through 10 for that number.
num = input('Pick a number: ')
num = int(num)

for n in range(1,11):
  print(f'{num} * {n} = {num * n}')

# Create a for loop that uses print to create the output shown below
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

i = 1
for i in range (1, 11):
    print(str(i) * i)
    i += 1

# C. break and continue
#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
# continue prompting the user if they enter invalid input. (Hint: use the isdigit method on 
# strings to determine this). Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.

user_number = input("Choose an odd number between 1 and 50: ")          # define the function
while True:                                                           # create the True condition to set the desired limits, range and odd
    if user_number.isdigit() = False or int(user_number) < 1 or int(user_number) > 50 or int(user_number) % 2 == 0:
        user_number = input(("Your input must be an odd number between 1 and 50")            
    else:
        break

user_number = int(user_number)

print(f"Number to skip is: {user_number}")

for i in range(1, 50):
    if i % 2 == 0:
        continue
    elif i == user_number:
        print("Yikes! Skipping to next number")
        continue
    print (f"Here is an odd number: {i}")

# D. The input function can be used to prompt for input and use that input in your python code.
#  Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a numeric type.)

n = 0                                                   #set the inputs
i = input("Please enter a positive number: ")

# # while True:
#   if this condition is true, keep prompting
# else:
#   break

while True:                                             # use the while loop to screen for incorrect values and run until correct
  if i.isdigit() == False or int(i) < 0:                # specify the incorrect inputs
    print('incorrect input')
    i = input("Please enter a positive number: ")       # add another entry field for i for users to enter correct value
  
  else:
    break                                               # add the break for a correct value to progress to next step


for n in range(int(i)):                                 # add a for loop to specify operation for certain vaules
        print (n)
        n += 1

# E. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the 
# number the user entered down to 1.

n = 1
i = input("Please enter a positive integer: ")

while True:
    if i.isdigit() == False or int(i) < 0:
        print("incorrect input ")
        i = input("Please enter a posiitve integer: ")

    else:
        break

for n in range(int(i), 0, -1):                      #the RANGE function is used to count in this scenario >> specifies using "i"  
    print(n)                                        # as the range, 0 as the end value, and -1 as the count increment


# 3. Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.

    n = 1
    for n in range(1, 101):
        print(n)

# For multiples of three print "Fizz" instead of the number

n = 1
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    else:
        print(n)

# For the multiples of five print "Buzz".
n = 1
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    if n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# For numbers which are multiples of both three and five print "FizzBuzz".

n = 1
for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
   
    else:
        print(n)

# 4. Display a table of powers.

# Prompt the user to enter an integer.
i = input("Please enter an integer: ")
while False:
    if i.isdigit():
        print("Please enter an integer in numerical form: ")
        i = input("Please enter an integer")
    else:
        break
# Display a table of squares and cubes from 1 to the value entered.
print( "BASE" + "|" + "SQUARED" + "|" + "CUBED")
for n in range(int(i)):
  n += 1  
  print( n , "|" , n**2 , "|" , n**3)
  print(" ")


# Ask if the user wants to continue.

move_along = input("would you like to continue? Y/N")
print(move_along)

# Assume that the user will enter valid data.
# Only continue if the user agrees to.

#6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, 
# author, and genre. Loop through the list and print out information about each book.

books = []
    {
        'title': 'title 1',
        'author': 'author 1',
        'genre': 'genre 1'
    
    }

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

