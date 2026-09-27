#1
from functools import reduce


cube = lambda x: x ** 3
#2
is_positive = lambda x: True if x > 0 else False
#3
full_name = lambda first, last: first + " " + last
#4
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

sorted = lambda people: sorted(people, key=lambda person: person["age"])

#1
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius_temps)
result = list(fahrenheit)
print(result)  
#2
numbers = [23, 67, 12, 89, 45, 91, 34, 56]
filtered = list(filter(lambda x: x > 50, numbers))
print(filtered)
#3
words = ["apple", "banana", "kiwi", "strawberry"]
length = (lambda words: list(map(len, words)))(words)
print(length)
#4
words = ["apple", "banana", "apricot", "kiwi", "avocado"]
filtered = list(filter(lambda word: word.startswith("a"), words))
print(filtered)
#5
numbers = [2, 3, 4, 5]
product = (lambda numbers: reduce(lambda x, y: x * y, numbers))(numbers)
print(product)
#6
numbers = [1, 2, 3, 4, 5, 6, 7]
squared = list(map(lambda x: x ** 2, numbers))
more_than_20 = list(filter(lambda x: x > 20, squared))
print(more_than_20)
#1 one line functions
#2 goes thru every value of a list, and perform the same function on them
#3 when the project gets big, easy for others to maintain
#4 writing lambda functions and practicing the special functions 
#5 seperate, for example, grouped functions, like all strinfs or all for one character/scene 