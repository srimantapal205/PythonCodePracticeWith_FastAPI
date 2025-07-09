"""
Varibles
"""
cost = 10
print(cost)

tax_percent = .25
tax = cost*tax_percent
price = tax+cost
print(price)

print(10+(10*.25))

username = "Python_code"
first_name = "Hello"


print(username)
print(first_name)

print(username+ " " +first_name)

welcome = 'Welcome to Python!'
print(welcome)


'''
Assignment
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.

'''
tAmout = 50
productPrice = 15
taxAmount = productPrice*(3/100)
rAmount = tAmout - (productPrice+taxAmount)
print(rAmount)