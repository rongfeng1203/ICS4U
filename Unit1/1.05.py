#1 Basic List Operations

#2 List Slicing
list(range(21))
print(list[0:10])
print(list[-5:])
print(list[5:15])
print(list[::3])
print(list[::2])
print(list[::-1])

#3 List Analysis
scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
avg_scores = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)
i=0
for score in scores:
    if score >= 85:
        i+= 1
print(f"Number of scores above 85: {i}")
sorts = sorted(scores)
print(f"Average score: {avg_scores}")
print(f"Maximum score: {max_score}")
print(f"Minimum score: {min_score}")

#4 String Basics
string = "Rina Feng"
print(string.upper())
print(string.lower())
print(string.title())
print(f"Length of string: {len(string.replace(' ', ''))}")
if "a" in string.lower():
    print("The letter 'a' is present in the string.")
print(string.replace(" ", "_"))
#5 String Slicing
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"First 5 letters: {alphabet[0:5]}")
print(f"Last 5 letters: {alphabet[-5:]}")
print(f"Every 3rd letter: {alphabet[::3]}")
print(f"Letters 11-15: {alphabet[10:15]}")
print(f"Reversed alphabet: {alphabet[::-1]}")
#6 Text Processing
user_input = "   hELLo, WoRLD!   "
user_input =(user_input.strip().title())
count = len(user_input.split())
user_input = user_input.replace("!", "")
user_input = user_input.replace(",", " ")
if user_input.startswith("Hello"):
    print("The string starts with 'Hello'.")
#7 Processing Text
paragraph = "Python is a powerful programming language. Python is easy to learn. Python is versatile."
split_paragraph = paragraph.split(". ")
print(len(split_paragraph))
split_words = paragraph.split(" ")
print(len(split_words))
i = 0
for word in split_words:
    if word.lower() == "python":
        i += 1
for word in split_words:
    if word.lower() == "python":
        replace_word = word.replace("Python", "Java")
print(replace_word)

#8 Create a Shopping List
shopping_list = []
shopping_list.append("apples")
shopping_list.append("bread")
shopping_list.append("milk")
shopping_list.append("eggs")
shopping_list.append("cheese")
print(list(enumerate(shopping_list, start=1)))
join_list = ", ".join(shopping_list)
print(f"Shopping list: {join_list}")
shopping_list.remove("bread")
sorting_list = sorted(shopping_list)
print(f"Sorted shopping list: {sorting_list}")

#9 Word Game
variable = "PYTHON"
list = [list(variable)]
list.reverse()
scrambled_word = "".join(list)
print("Scrambled word:", scrambled_word)
guess = input("Unscramble the word: ")
if guess.upper() == word:
    print("Correct!")
else:
    print("Incorrect. The word was", variable)

#10 Grade Analyzer
scores = [12, 23, 34, 45, 56, 78, 89, 99, 1, 100]
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
above_80 = 0
for score in scores:
    if score > 80:
        above_80 += 1
print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Number of scores above 80:", above_80)
#11 Name Formatter
full_name = input("Enter your full name: ")
full_name = full_name.title()
parts = full_name.split()
print("First name:", parts[0])
if len(parts) == 3:
    print("Middle name:", parts[1])
    print("Last name:", parts[2])
else:
    print("Last name:", parts[1])
initials = ""
for name in parts:
    initials += name[0] + "."
print("Initials:", initials)
#12 Email Processor
email = input("Enter your full email adress: ")
if "@" in email and "." in email:
    username, domain = email.split("@")
if "." in domain:
    name, extension = domain.split(".")
if "@" in email and "." in email:
    print("email is valid.")
    