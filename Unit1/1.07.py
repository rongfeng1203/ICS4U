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

        