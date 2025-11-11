import copy


l1= [1, 2, 3, 4]
l2= [3, 4, 5, 6]

l3 = l1+l2
print(l3)

# Create a new list with unique values from l3
newList = []

for item in l3:
    if item not in newList:
        newList.append(item)
       
print(newList)

# use python filter functon for get the even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, newList))


oddNumbers = list(filter(lambda x: x%2 !=0, newList))

print("Even_numbers", even_numbers)
print("Odd_numbers", oddNumbers)

nl = copy.deepcopy(newList)

for x in newList:
    if x%2 == 0:
        nl.remove(x)
print("After removing even numbers", nl)

nl2 = list(set(l3))
print('Get Unique list: ',nl2)

st1 = set(l3)
st1.add(7)
print('Get set: ',st1)





### Generators in Python

def generate_number(n):
    for i in range(n):
        yield i*i

gen = generate_number(5)
print(list(gen))

oddgenlst = []
for x in generate_number(10):
    if x %2 !=0:
        oddgenlst.append(x)

print("Generator odd numbers: ", oddgenlst)


# Using map function

getSqureNumber = list(map(lambda x: x*x, oddgenlst))
print("Get square of odd numbers: ", getSqureNumber)


getEvenNumber = list(filter(lambda x: x%2 == 0, generate_number(10)))
print('Get even number from generator:',getEvenNumber)