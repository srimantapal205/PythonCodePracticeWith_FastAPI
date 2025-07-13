"""
Functions

"""
print("Hello and wellcome to the functions module!")

def myFunction():
    print("This  is inside of function...!")


myFunction()

def printName(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')

printName("John", "Doe")

def coloAsLocal():
    color = "red"
    print(f'This is local color: {color}')

color = 'Green'
print(f'This is Global variable:: {color}')

coloAsLocal()


def multiplyNumbers(a, b):
    return  a*b

solution = multiplyNumbers(10, 6)

print(solution)


def print_list_numbers(numbers):
    for number in  numbers:
        print(number)
    print("End of the list")


num = [1, 2, 3, 4, 5]
print_list_numbers(num)

def buyItem(cost_of_item):
    return  cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return  cost_of_item*current_tax_rate

total_cost = buyItem(100)
print(total_cost)

"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def create_person_dict(firstname, lastname, age):
    person_dict = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
    }
    return  person_dict

person = create_person_dict("John", "Doe", 30)
print(person)



