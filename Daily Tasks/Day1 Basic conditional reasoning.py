# Question 1: Pass or Fail
# Problem Statement:
# Given a mark, print Pass when it is at least 40; otherwise Fail.
marks = int(input("Enter the marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
    

# Question 2: Positive or Non-positive
# Problem Statement:
# Print Positive when a number is greater than 0; otherwise Non-positive.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Non-positive")
    

# Question 3: Even or Odd
# Problem Statement:
# Print Even or Odd for a given integer.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    

# Question 4: Adult Check
# Problem Statement:
# Print Adult for age 18 or above; otherwise Minor.
age = int(input("Enter the age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")
    
    
# Question 5: Discount Eligibility
# Problem Statement:
# Print Discount when purchase amount is at least 1000; otherwise No Discount.
purchase_amount = int(input("Enter the purchase amount: "))
if purchase_amount >= 1000:
    print("Discount")
else:
    print("No Discount")
    
    
# Question 6: Temperature Alert
# Problem Statement:
# Print Hot when temperature is above 30; otherwise Normal.
temperature = int(input("Enter the temperature: "))
if temperature > 30:
    print("Hot")
else:
    print("Normal")
    
    
# Question 7: Attendance Status
# Problem Statement:
# Print Eligible when attendance is at least 75; otherwise Shortage.
attendance = int(input("Enter the attendance percentage: "))
if attendance >= 75:
    print("Eligible")
else:
    print("Shortage")
    

# Question 8: Stock Availability
# Problem Statement:
# Print In Stock when quantity is greater than 0; otherwise Out of Stock.
quantity = int(input("Enter the quantity: "))
if quantity > 0:
    print("In Stock")
else:
    print("Out of Stock")
    
    
# Question 9: Higher Score
# Problem Statement:
# Given two scores, print the higher score.
score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
if score1 > score2:
    print("Higher score is:", score1)
else:
    print("Higher score is:", score2)
    
    
# Question 10: Lower Price
# Problem Statement:
# Given two prices, print the lower price.
price1 = float(input("Enter the first price:"))
price2 = float(input("Enter the second price:"))
if price1 < price2:
    print("Lower price is:", price1)
else:
    print("Lower price is:", price2)
    
    
# Question 11: Grade A
# Problem Statement:
# Print A when mark is at least 80; otherwise Not A.
mark = int(input("Enter the marks: "))
if mark >= 80:
    print("Grade A")
else:
    print("Not A")
    

# Question 12: Free Delivery
# Problem Statement:
# Print Free Delivery for an order of 500 or more; otherwise Delivery Charge.
order_amount = float(input("Enter the order amount: "))
if order_amount >= 500:
    print("Free Delivery")
else:
    print("Delivery Charge")
    
    
# Question 13: Multiple of Five
# Problem Statement:
# Print Multiple of 5 when a number is divisible by 5; otherwise Not Multiple of 5.
num = int(input("Enter a number:"))
if num % 5 == 0:
    print("Multiple of 5")
else:
    print("Not multiple of 5")


# Question 14: Weekend Check
# Problem Statement:
# For day numbers 1–5 print Weekday and 6–7 print Weekend.
day = int(input("Enter the day number (1-7):"))
if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day number")


# Question 15: Performance Level
# Problem Statement:
# Print Excellent for 90+, Good for 60–89, and Needs Improvement below 60.
marks = int(input("Enter the marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
else:
    print("Needs Improvement")
 
    
# Question 16: Number Comparison
# Problem Statement:
# For two numbers print First Greater, Second Greater, or Equal.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")
   
    
# Question 17: Salary Band
# Problem Statement:
# Print Low below 30000, Medium from 30000 to 59999, High for 60000+.
salary = int(input("Enter the salary:"))
if salary >= 60000:
    print("High Salary")
elif salary >= 30000:
    print("Medium Salary")
else:
    print("Low Salary")
    
    
# Question 18: Login Check
# Problem Statement:
# Compare stored and entered usernames; print Login Accepted or Invalid User.
stored_username = "admin"
entered_username = input("Enter the username: ")
if entered_username == stored_username:
    print("Login Accepted")
else:
    print("Invalid User")
 
    
# Question 19: Student Eligibility
# Problem Statement:
# Print Eligible only when attendance is at least 75 and mark is at least 40.
attendance = int(input("Enter the attendance: "))
mark = int(input("Enter the mark: "))
if attendance >= 75 and mark >= 40:
    print("Eligible")
else:
    print("Not Eligible")
    
# Question 20: Range Check
# Problem Statement:
# Print In Range when a number is between 10 and 50 inclusive; otherwise Out of Range.
num = int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("In Range")
else:
    print("Out of Range")
