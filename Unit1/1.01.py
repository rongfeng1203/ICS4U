#1
import math


celsius = float(input("Enter the temperature in Celsius: "))#float converts user input directly 
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
#2
age = int(input("Enter your age: ")) #int converts user input directly
age_in_days = age * 365
print("Your age in days is:", age_in_days)
#3
price = float(input("Enter the price of the item: ")) #float converts user input directly
taxes = price * 0.13
total = price + taxes
print("Total price is:", price, "plus taxes of", taxes, "equals", total)
#4
num1 = int(input("Enter the first number: ")) #int converts user input directly
num2 = int(input("Enter the second number: ")) #int converts user input directly
sum = num1 + num2
difference = abs(num1 - num2)#aboslute value of difference
product = num1 * num2
quotient = float(num1) / float(num2) if num2 != 0 else "undefined"#includes a check to avoid division by zero
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
#5
length = float(input("Enter the length of the rectangle: ")) #int converts user input directly
width = float(input("Enter the width of the rectangle: ")) #int converts user input directly
area = length * width
perimeter = 2 * (length + width)
area_rounded = int(round(area)) #rounds the area to the nearest integer because just float doesn't round
perimeter_rounded = int(round(perimeter)) 
print("Rounded area of the rectangle is:", area_rounded, "and original area is:", area)
print("Rounded perimeter of the rectangle is:", perimeter_rounded, "and original perimeter is:", perimeter)
#6
items = int(input("How many items are you buying? "))
price = float(input("What is the price per item? "))
subtotal = items * price
discount_input = input("Do you have a discount? (yes/no): ")
discount = bool(discount_input.lower() == "yes")#treats any input other than "yes" as False
if discount == True:
    total_price = subtotal - (subtotal * 0.1)
else:
    total_price = subtotal
print(f"Final total: ${total_price}")
#7
distance = float(input("Enter the distance traveled in kilometers: "))
time = float(input("Enter the time taken in hours: "))
if time != 0:  # safety check to avoid division by zero
    speed = distance / time
    rounded_speed = math.floor(speed)
    print("Average speed is:", rounded_speed, "km/h")
    print(f"Exact speed is: {speed:.2f} km/h")
else:
    print("Time cannot be 0.")
#8
Test1 = float(input("Enter the score for Test 1: "))
Test2 = float(input("Enter the score for Test 2: "))    
Test3 = float(input("Enter the score for Test 3: "))
average = (Test1 + Test2 + Test3) / 3
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Average: {average:.1f}")
print("Letter grade:", grade)
#9
sec = int(input("Enter the number of seconds: "))
hours = int(sec//3600)
minutes = int((sec%3600)//60)
sec = int((sec%3600)%60)
print(hours,"hours, ", minutes, "minutes, ", sec, "seconds")
#10
bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to be paid: ${total_amount:.2f}")
