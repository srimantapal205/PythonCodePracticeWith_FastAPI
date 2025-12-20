lstDict = [
        {'name': 'Alice', 'age': 30}, 
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35},
        {'name': 'David', 'age': 28}
    ]

print(type(lstDict))

# Get only name inside a list
nameList = [(person['name'], person['age']) for person in lstDict]
print(nameList)
