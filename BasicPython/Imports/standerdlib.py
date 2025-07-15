"""
Stander Library comes with python

useful methods
"""

#Random
import  random
import  math
type_of_drinks = ['Coke', 'Pepsi', 'Sprite', 'Fanta', 'Dr Pepper']

def get_random_drinks(drinks):
    # Return random drinks from list
    return  random.choice(drinks)

print(get_random_drinks(type_of_drinks))

# Get random number
print(random.randint(1, 10))

squre_root = math.sqrt(16)