# # # If-Else Statements in Python
# # # If-Else statements are used for conditional execution of code blocks.

# age = 18

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
# # Output: You are eligible to vote.'

# # # If-Elif-Else Statements in Python
# # # If-Elif-Else statements are used for multiple conditional checks.

# age = 18

# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
# # Output: You are an adult.


# # Traffic Light Example
# # This example demonstrates the use of if-elif-else statements to determine actions based on traffic light colors. 
# traffic_light = input("Enter the Color of Light : ").lower()
# if traffic_light == "red":
#     print("Stop")
# elif traffic_light == "yellow":
#     print("Caution, Go Slow!!")
# elif traffic_light == "green":
#     print("Go")
# else:
#     print("Invalid color")

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



