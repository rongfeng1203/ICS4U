
##day 2
#1
Grade = float(input("Enter the Grade: "))
if Grade >= 90:
    grade = "A"
elif Grade >= 80:
    grade = "B"
elif Grade >= 70:
    grade = "C"
elif Grade >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {Grade:.1f}")
print("Letter grade:", grade)
#2
age = int(input("Enter the age: "))
if age >= 65:
    ticket = "$10"
elif age >= 18:
    ticket = "$15"
elif age >= 13:
    ticket = "$12"
elif age >= 3:
    ticket = "$8"
else:
    ticket = "Free"
print(f"Ticket price: {ticket}")
#3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    larger = num1
elif num2 > num1:
    larger = num2
else:
    larger = "Both numbers are equal"
print(f"Larger number: {larger}")
#4
age=int(input("Enter your age: "))
driver_license = input("Do you have a driver's license? (yes/no): ")
if age >= 21 and driver_license.lower() == "yes":
    print("You are eligible to rent a car.")
elif age>= 21 and driver_license.lower() != "no":
    print("You need a license to rent a car.")
elif age < 21 and driver_license.lower() == "yes":
    print("You must be 21 to rent a car.")
else:
    print("You must be 21 or older and have a license to rent a car.")
#5
size = input("Enter the size of the pizza (small/medium/large): ").lower()
chesse = input("Do you want extra cheese? (yes/no): ").lower()
price = 0
if size == "small":
    price = 10
elif size == "medium":
    price = 14
elif size == "large":
    price = 18

if chesse == "yes":
    price += 2

print(f"Total price for the pizza is: ${price:.2f}")
#6
gpa = float(input("Enter your GPA: "))
vhours = int(input("Enter the number of volunteer hours: "))
if gpa >= 3.5 and vhours >= 50:
    print("You are eligible for full scholarship.")
elif gpa >= 3.0 and vhours >= 25:
    print("You are eligible for partial scholarship.")
elif gpa >= 3.5 and vhours < 25:
    print("You are eligible for academic scholarship only.")
elif gpa >= 3.0 and vhours > 50:
    print("You are eligible for community service scholarship.")
else:
    print("You are not eligible for any scholarship.")
#7
num = int(input("Enter a number: "))
while num > 1:
    print (num)
print("Blast off!")

#8
num = 17
i=0
guess = int(input("Guess the secret number: "))
while guess != num:
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    guess = int(input("Guess again: "))
    i+= 1
else:
    print("Congratulations! You guessed the secret number. You guessed it in", i, "tries.")
#9
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("The sum is:", total)
#10
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(1, end + 1):
    print(start, "x", i, "=", start * i)