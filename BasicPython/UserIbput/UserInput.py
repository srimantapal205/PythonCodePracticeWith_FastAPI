"""
User Input
"""
first_name = input("Enter your first name:: ")
print(first_name)

day = input("How many days before your birthday:: ")

print(f"Hi {first_name}, only {day} before your birthday")



"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""
days = int(input("How many days until your birthday ? :: "))

week = round(days / 7, 2)

print(f" only {week} week before your birthday")

