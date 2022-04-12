# 1. Define a function named is_two. It should accept one input and return True if the passed input is 
# either the number or the string 2, False otherwise.
def is_two(n):
    if input.int() == 2 or input.lower() == 'two':
        return True
    else:
        return False

## optimal:
def is_two(n):
    return n == 2 or n == '2'

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    if letter.lower() in ['a','e', 'i', 'o', 'u']:
        return True
    else:
        return False


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(letter):
    if is_vowel(letter):
        return False
    else:
        return True

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word 
# if the word starts with a consonant.
word = "coffee"
def cap_consonant(word):
    if word[0].lower() not in ['a','e', 'i', 'o', 'u']:
        return word.capitalize()
    else:
        return (f"{word} doesn't begin with a consonant")
print(cap_consonant(word))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
price = 20
good_service = True
def calculate_tip(price):
    if good_service == True:
        return price * 0.25
    if ok_service == True:
        return price * 0.15
    elif bad_service == True:
        return price * 0.05

print(calculate_tip(price))

## another way
def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 100:

   
    

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
original_price = 100
discount_pct = 20
def apply_discount(original_price):
    return original_price * ((100 - discount_pct)/100)

print(apply_discount(100))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
input = ('1, 2, 3, 4')              # a string needs parenthesis and quotes
def handle_commas(input):
    if type(input) != str:
        return 'input must be a string'
    return input.replace(", ", "")  # replace takes argument to be replaced, and replacement value

print(handle_commas(input))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
num = 87
def get_letter_grade(num):
    if type(num) == float or type(num) == int:
        if 100 >= num > 89:
            return 'A'
        elif 89 >= num > 79:
            return 'B'
        elif 79 >= num > 69:
            return 'C'
        elif 69 >= num > 59:
            return 'D'
        else:
            return 'F'
    else:
        return 'input a number please'
print(get_letter_grade(num))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

input = ('Alibaba')

def remove_vowels(input):
    vowels = ('a', 'e', 'i', 'o', 'u')    #specify values to remove
    for letter in input:                    # for loop
        if letter.lower() in vowels:        # compare the input to the list of undesired characters, after converting input to lower
            input = input.replace(letter, '')   #replace function takes item to replace first, relacement value second
    return input                                #retrun stores the value
print(remove_vowels(input))                     # print to test

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is
# Anything that is not a valid python identifier should be removed
# Leading and trailing whitespace should be removed
# Everything should be lowercase
# Spaces should be replaced with underscores
# For example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

input = '!H@rvey Doll@z!'
def normalize_name(input):
    for letter in input:
        if letter.isspace() == True:
            input = input.replace(" ", "_")
    for letter in input:
        if letter.isalnum() == False and letter != "_":
           input = input.replace(letter, '')
        else:
            continue
    input = input.lower()
    input = input.strip()
    return input
print(normalize_name(input))

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
values = [1, 1, 1]
def cumulative_sum(values):
    total = 0
    for value, num in enumerate(values)
    sumin values:
        total += value 
    return total
print(cumulative_sum(values))
# Additional Exercise
# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27