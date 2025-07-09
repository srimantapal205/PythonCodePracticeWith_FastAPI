"""
Flow control:: if else elif

"""
x = 2
if x > 1:
    print("X is greater than 1")

print("Outside of if block")

if x > 1:
    print("X is greater than 1")
else:
    print("Xis not greater than 1")

hour =17
if hour < 13:
    print("Good Morning")
elif hour <18:
    print("Good Afternoon")
else:
    print("Good Night")


"""
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')

if grade >=90 and grade <=100:
    print(f"Grade: A : {grade}")
elif grade >=80 and grade<=89:
    print(f"Grade: B : {grade}")
elif grade >= 70 and grade <= 79:
    print(f"Grade: C : {grade}")
elif grade >= 60 and grade <= 69:
    print(f"Grade: D : {grade}")
else:
    print(f"Grade: F : {grade}")
"""
grade = int(input('Enter your grade: '))
max_g =100
min_g =0
if grade <min_g or grade > max_g:
    print(f"Grade: Invalid : {grade}. Grade must be between {min_g} and {max_g}")
elif grade >=90:
    print(f"Grade: A : {grade}")
elif grade >=80 :
    print(f"Grade: B : {grade}")
elif grade >= 70:
    print(f"Grade: C : {grade}")
elif grade >= 60:
    print(f"Grade: D : {grade}")
else:
    print(f"Grade: F : {grade}")
