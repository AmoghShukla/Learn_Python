# If-Else Statements in Python
# If-Else statements are used for conditional execution of code blocks.

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Output: You are eligible to vote.'

# If-Elif-Else Statements in Python
# If-Elif-Else statements are used for multiple conditional checks.

age = 18

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# Output: You are an adult.


# Traffic Light Example
# This example demonstrates the use of if-elif-else statements to determine actions based on traffic light colors. 

traffic_light = input("Enter the Color of Light : ").lower()
if traffic_light == "red":
    print("Stop")
elif traffic_light == "yellow":
    print("Caution, Go Slow!!")
elif traffic_light == "green":
    print("Go")
else:
    print("Invalid color")

# ATM Example
# This example uses if-elif-else statements to simulate an ATM transaction based on user input

balance  = 10000

Withdrawl_Amount = int(input("Enter the Amount You want to Withdraw : "))

if Withdrawl_Amount > 0 and Withdrawl_Amount % 100 == 0 and Withdrawl_Amount <= balance:
    balance -= Withdrawl_Amount
    print("You Withdrew Rs.", Withdrawl_Amount, "from your Account, Your New Balance is : ", balance, "Rs.")
elif Withdrawl_Amount > 0 and Withdrawl_Amount % 100 == 0 and Withdrawl_Amount > balance:
    balance -= Withdrawl_Amount
    print("Insufficient Funds!!")
else:
    print("Please Enter the a Valid Amount!!")

# Election Eligibility Example
# This example checks if a person is eligible to vote based on their age and citizenship status.


voter_id = input("Do you have the Voter Identification card of India? (yes/no) : ").lower()
if voter_id == "yes":
    age = int(input("Enter Your Age : "))
    if age >= 18:
        print("You are eligible to vote.")
    elif age < 18:
        print("You are not eligible to vote, You are a Minor.")
    else:
        print("Invalid Input, Please Enter Valid Details!!")
else:
    print("You are not eligible to vote, You dont have the Voter Id Card.")

# Supermarket Discount Example
# This example calculates the total bill amount after applying discounts based on the membership category of the Customer.
print("------:Welcome to Supermarket:------")

bill_amount = float(input("Enter the Total Bill Amount : "))
membership = input("Enter Your Membership Category (Platinum/Gold/None) : ").lower()

if membership == "platinum":
    discount = 20
elif membership == "gold":
    discount = 10
else:
    discount = 0

final_amount = bill_amount - (bill_amount * discount / 100)
print("Your Final Bill Amount after discount is : Rs.", final_amount)


# Write a Program to Determine the Person who has Donated Blood Based on their Age and Weight above 50

age = int(input("Enter Your Age : "))
weight = float(input("Enter Your Weight in Kg : "))

if 65 >= age >= 18 and weight > 50:
    print("You are Eligible to Donate Blood.")
else:
    print("You are Not Eligible to Donate Blood.")

# Calculate Driving Eligibility Based on Age, Carrying License

age = int(input("Enter Your Age : "))
license = input("Do you have a Driving License? (yes/no) : ").lower()
if age >= 18 and license == "yes":
    print("You are Eligible to Drive.")
elif age >= 18 and license == "no":
    print("You are Not Eligible to Drive as You dont have a Driving License, You'll have to pay fine of Rs.5000")
else:
    print("You are Not Eligible to Drive as You are a Minor.")

# Electricity Price Calculator Based on Units Consumed and Discount Applied where 1 unit  = 5rs and 100 units = 0% discount, 101-300 = 10% discount and 301 to 500 units = 20% discount
units_consumed = int(input("Enter the Number of Units Consumed : "))
cost_per_unit = 5

if units_consumed <= 100:
    discount = 0
elif 101 <= units_consumed <= 300:
    discount = 10
elif 301 <= units_consumed <= 500:
    discount = 20
else:
    discount = 30

total_cost = units_consumed * cost_per_unit
final_amount = total_cost - (total_cost * discount / 100)
print("Your Final Bill Amount after discount of ", discount, "% is : Rs.", final_amount)