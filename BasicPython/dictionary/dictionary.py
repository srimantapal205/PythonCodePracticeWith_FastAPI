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


# ShaloCopy
user_dictionary =us