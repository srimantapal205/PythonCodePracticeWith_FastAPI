"""
Lists are a collection of data
"""

myList = [90, 67,89,43,100,5]
print(myList)
print(myList[0])


peopleList= ['A','B','C']
print(peopleList)
print(type(peopleList))
peopleList[2] = 'D'
print(peopleList[2])

#Get length
print(len(peopleList))

# Slicing
print(peopleList[0:2])
print(myList[2:4])

#append
myList.append(1000)
print(myList)

#insert
myList.insert(0, 2000)
print(myList)

#remove
myList.remove(89)
print(myList)
#pop()
myList.pop(0)
print(myList)

#sort
myList.sort()
print(myList)




# - Create a list of 5 animals called zoo
zoo =['Tiger', 'Lion', 'Dog', 'Cat', 'Rat']
print(zoo)
# - Delete the animal at the 3rd index.
zoo.pop(3)
print(zoo)
#- Append a new animal at the end of the list
zoo.append('Cow')
print(zoo)
#- Delete the animal at the beginning of the list.
zoo.pop(0)
print(zoo)
#- Print all the animals
for an in zoo:
    print(an)
#- Print only the first 3 animals
print(zoo[0:3])




