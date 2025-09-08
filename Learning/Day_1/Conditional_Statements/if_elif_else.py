# # If-Else Statements in Python
# # If-Else statements are used for conditional execution of code blocks.

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Output: You are eligible to vote.'

# # If-Elif-Else Statements in Python
# # If-Elif-Else statements are used for multiple conditional checks.

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


