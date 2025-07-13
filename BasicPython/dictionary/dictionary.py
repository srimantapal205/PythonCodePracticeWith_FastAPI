"""
Dictionary Example

"""
user_dictionary = {
    'username': 'john_doe',
    'name': 'John Doe',
    'age': 30,
}

user_dictionary["email"] = 'test@test.com'

print(user_dictionary)

print(user_dictionary.get('username'))

print(len(user_dictionary))

#user_dictionary.pop('email')
#print(user_dictionary)

#user_dictionary.clear()
#print(user_dictionary)

#del user_dictionary
#print(user_dictionary)


for x in user_dictionary:
    print(x)


for x, y in user_dictionary.items():
    print(f'{x} : {y}')

user_dictionary2 =user_dictionary.copy()
user_dictionary2.pop('age')
print(user_dictionary)
print(user_dictionary2)




user_dictionary2 =user_dictionary
user_dictionary2.pop('age')
print(user_dictionary)

print('----------------------------------------------------')

"""
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2

"""
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

print('-----------Create a for loop to print all keys and values-----------------\n')
for key, value in my_vehicle.items():
    print(f'{key} : {value}')
print('----------------------Create a new variable vehicle2, which is a copy of my_vehicle----------------------\n')
vehicle2 = my_vehicle.copy()
print(vehicle2)

print('-----Add a new key "number_of_tires" to the vehicle2 variable that is equal to 4----\n')
vehicle2['number_of_tires'] = 4
print(vehicle2)

print('-------------------------Delete the mileage key and value from vehicle2---------------------------\n')
vehicle2.pop('mileage')
print(vehicle2)

print('------------------------- Print just the keys from vehicle2---------------------------\n')


for key in vehicle2.keys():
    print(f'Key : {key}')
