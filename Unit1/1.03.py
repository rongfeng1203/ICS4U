#Basic Functions
def print_welcome():
    print("Welcome to python programming!")
def calculate_area(number):
    square = number * number
    return square
def full_name(first, last):
    return first + " " + last
def is_adult(age):
    return True if age >= 18 else False

#Functions with Multiple Returns
def analyze_numbers(num):
    neutral = "Zero"
    eo = "Even" if num % 2 == 0 else "Odd"
    absl = abs(num)
    if num > 0:
        neutral = "Positive"
    elif num < 0:
        neutral = "Negative"
    return neutral, eo, absl, num
#Default Parameters
def create_username(first_name, last_name, year=2024):
    return first_name[0].lower() + last_name.lower() + str(year)
#Temperature Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit   
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
