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


# Handle exceptions in python

try:
    x = generate_number(4)
    print(list(x))
except ValueError:
    print("Value Error occurred. Please provide a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Generation completed successfully.")
finally:
    print("Execution of the try-except block is complete.")

data_list = []
with open("file.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
    for word in data.split():
        data_list.append(word)

print(data_list)

# convert list as dictionary
data_list_dict = [{'word': word, 'length': len(word)} for word in data_list]
print(data_list_dict)

# Create a filter dict with words length greater than 5
filterDict= []
def getFilterDict(len):
    for item in data_list_dict:
        if item['length'] > len:
            filterDict.append(item)
    return filterDict

result = getFilterDict(5)
print(result)

result = getFilterDict(8)
print(result)



#[{'word': 'After', 'length': 5}, {'word': 'removing', 'length': 8}, {'word': 'even', 'length': 4}, {'word': 'numbers', 'length': 7}, {'word': 'Generation', 'length': 10}, {'word': 'completed', 'length': 9}, {'word': 'successfully.', 'length': 13}, {'word': 'Execution', 'length': 9}, {'word': 'of', 'length': 2}, {'word': 'the', 'length': 3}, {'word': 'try-except', 'length': 10}, {'word': 'block', 'length': 5}, {'word': 'is', 'length': 2}, {'word': 'complete.', 'length': 9}]