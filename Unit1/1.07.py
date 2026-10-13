def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

records = [
    {"name": "Ari", "mark": 84},
    {"name": "Bea", "mark": 91},
    {"name": "Mina", "mark": 76},
    {"name": "Noah", "mark": 88}
]

def SearchByName(records, targetName):
    for i in range(len(records)):
        if records[i]["name"] == targetName:
            return i
    return -1

marks = [{"name": "Ari", "mark": 84},
 {"name": "Bea", "mark": 91},
 {"name": "Chen", "mark": 76},
 {"name": "Devi", "mark": 88}]

element = [[1, 2, 3],
 [4, 5, 6]]

for i in range(len(element)):
    for j in range(len(element[i])):
        element[i][j] *= 2


students = [
    {"name": "Ari", "mark": 84},
    {"name": "Bea", "mark": 91},
    {"name": "Chen", "mark": 76},
    {"name": "Devi", "mark": 88},
    {"name": "Eli", "mark": 79},
]

def search_by_name(students, name):
    for i in range(len(students)):
        if students[i]["name"] == name:
            return i
    return -1

def sort_by_mark(students):
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i]["mark"] > students[j]["mark"]:
                students[i], students[j] = students[j], students[i]
    # Sort the records from lowest mark to highest mark.
    return students

def multiply_grid(grid, constant):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] *= constant
    # Multiply every element by constant.
    return grid

def swap_rows(grid, row_a, row_b):
    # Swap the two rows.
    grid[row_a], grid[row_b] = grid[row_b], grid[row_a]
    return grid

def factorial(n):
    # Write a recursive factorial function.
    if n == 0:
        return 1
    return n * factorial(n - 1)

def recursive_binary_search(array, target, low, high):
    # Search a sorted array recursively.
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursive_binary_search(array, target, low, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, high)

# Tests
print(search_by_name(students, "Chen"))  # Expected: 2
print(search_by_name(students, "Zoe"))   # Expected: -1

print(sort_by_mark(students))
# Expected marks in order: 76, 79, 84, 88, 91

print(multiply_grid([[1, 2], [3, 4]], 2))
# Expected: [[2, 4], [6, 8]]

print(swap_rows([[1, 2], [3, 4], [5, 6]], 0, 2))
# Expected: [[5, 6], [3, 4], [1, 2]]

print(factorial(4))  # Expected: 24

sorted_numbers = [2, 5, 8, 12, 16, 23]
print(recursive_binary_search(sorted_numbers, 12, 0, len(sorted_numbers) - 1))
# Expected: 3

books = [
    {"title": "River of Stars", "author": "A. Chen", "year": 2018},
    {"title": "The Glass Map", "author": "M. Patel", "year": 2009},
    {"title": "Northbound", "author": "J. Okafor", "year": 2022},
    {"title": "Small Worlds", "author": "L. Reyes", "year": 2014},
    {"title": "After the Rain", "author": "S. Morgan", "year": 2005},
]

def search_by_title(books, title):
    # Return the first matching index, or -1.
    for i in range(len(books)):
        if books[i]["title"] == title:
            return i
    return -1

def sort_by_year(books):
    # Sort books from earliest to latest publication year.
    for i in range(len(books)):
        for j in range(i + 1, len(books)):
            if books[i]["year"] > books[j]["year"]:
                books[i], books[j] = books[j], books[i]
    return books

def binary_search_by_year(books, target_year, low, high):
    # Recursively search the sorted array by year.
    if low > high:
        return -1
    mid = (low + high) // 2
    if books[mid]["year"] == target_year:
        return mid
    elif books[mid]["year"] > target_year:
        return binary_search_by_year(books, target_year, low, mid - 1)
    else:
        return binary_search_by_year(books, target_year, mid + 1, high)

# Tests
print(search_by_title(books, "Northbound"))  # Expected: 2
print(search_by_title(books, "Missing Book"))  # Expected: -1

sort_by_year(books)
print([book["year"] for book in books])
# Expected: [2005, 2009, 2014, 2018, 2022]

print(binary_search_by_year(books, 2014, 0, len(books) - 1))
# Expected: 2

print(binary_search_by_year(books, 2010, 0, len(books) - 1))
# Expected: -1

pixels = [
    [40, 120, 250],
    [0, 180, 90],
    [255, 75, 30],
]

def brighten(grid, amount):
    # Add amount to every value, with a maximum of 255.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = min(grid[i][j] + amount, 255)
    return grid

def swap_columns(grid, column_a, column_b):
    # Swap the selected columns in every row.
    for i in range(len(grid)):
        grid[i][column_a], grid[i][column_b] = grid[i][column_b], grid[i][column_a]
    return grid

def count_value(grid, target):
    # Count how many times target appears in the grid.
    count = 0
    for row in grid:
        count += row.count(target)
    return count

def sum_digits(n):
    # Recursively return the sum of the digits in n.
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

# Tests
print(brighten([[40, 250], [0, 100]], 20))
# Expected: [[60, 255], [20, 120]]

print(swap_columns([[1, 2, 3], [4, 5, 6]], 0, 2))
# Expected: [[3, 2, 1], [6, 5, 4]]

print(count_value([[1, 2, 1], [3, 1, 4]], 1))
# Expected: 3

print(sum_digits(324))  # Expected: 9
print(sum_digits(7))    # Expected: 7
print(sum_digits(0))    # Expected: 0
