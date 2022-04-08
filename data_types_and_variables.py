# 1.  What data type would best represent:

# A term or phrase typed into a search box?
    #str
# If a user is logged in?
    #bool
# A discount amount to apply to a user's shopping cart?
    #INT/float
# Whether or not a coupon code is valid?
    #bool
# An email address typed into a registration form?
    #str
# The price of a product?
    #float
# A Matrix?
    # dict
# The email addresses collected from a registration form?
    # list
# Information about applicants to Codeup's data science program?
    # dict

# 2. For each of the following code blocks, read the expression 
# and predict what the result of evaluating it would be, 
# then execute the expression in your Python REPL.

# Predict exercises
from tkinter import N

#Word Problems
#1. You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't 
# know yet if they're going to like it). If price for a movie per day is 
# 3 dollars, how much will you have to pay?
price = 3
mermaid = 3
bb = 5
herc = 1
total = price * (mermaid + bb + herc)
print(total)

#2. Suppose you're working as a contractor for 3 companies: Google, Amazon 
# and Facebook, they pay you a different rate per hour. Google pays 400 
# dollars per hour, Amazon 380, and Facebook 350. How much will you receive 
# in payment for this week? You worked 10 hours for Facebook, 6 hours 
# for Google and 4 hours for Amazon.

pay_google = 400
pay_amazon = 380
pay_facebook = 350
weekly_pay = (10 * pay_facebook) + (6 * pay_google) + (4 * pay_amazon)
print(weekly_pay)

#3. A student can be enrolled to a class only if the class is not full and 
# the class schedule does not conflict with her current schedule.

not_full = True
no_conflict = True
enrolled = not_full and no_conflict
print(enrolled)

#4. A product offer can be applied only if people buy more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific 
# amount of products.

items_bought = 3
offer_not_expired = True
premium_member = True
product_offer = ((items_bought > 2 or premium_member) and offer_not_expired)
print(product_offer)

# 5. Create a variable that holds a boolean value for each of the following 
# conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'
password_len = len(password) >= 5
print(password_len)
username_len = len(username) <=20
print(username_len)
password_not_username = username != password
print(password_not_username)
no_white_spaces = (password == password.strip() and username == username.strip())



















