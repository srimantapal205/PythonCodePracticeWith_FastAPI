"""
String Formating

"""

first_name = "Python"
print("hi "+first_name)

print(f"Hi {first_name}")

sentence= "Hi {}"
print(sentence.format(first_name))

lastname = "Program"
sentence2= "Hi {} {}"
print(sentence2.format(first_name, lastname))