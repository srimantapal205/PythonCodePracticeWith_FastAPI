# List of students with their marks in 5 subjects
students_dict = {
    "Alice": [85, 90, 78, 92, 88],
    "Bob": [65, 70, 68, 72, 74],
    "Charlie": [80, 85, 88, 90, 84],
    "David": [55, 60, 58, 62, 57],
    "Emma": [95, 90, 92, 96, 94]
}

students = [
    ("Alice", [85, 90, 78, 92, 88]),
    ("Bob", [65, 70, 68, 72, 74]),
    ("Charlie", [80, 85, 88, 90, 84]),
    ("David", [55, 60, 58, 62, 57]),
    ("Emma", [95, 90, 92, 96, 94])
]


stu_avg_dict_1 = {}
# {'Alice': 86.6, 'Bob': 69.8, 'Charlie': 85.4, 'David': 58.4, 'Emma': 93.4}
#Get student names and average marks
for student in students_dict.items():
    name = student[0]
    marks = student[1]
    avg_marks = sum(marks) / len(marks)
    stu_avg_dict_1[name] = avg_marks

print(stu_avg_dict_1)

stu_avg_dict_2 = {}
for student in students:
    name = student[0]
    marks = student[1]
    avg_marks = sum(marks) / len(marks)
    stu_avg_dict_2[name] = avg_marks

print(stu_avg_dict_2)
# Find the student with the 75% average marks
avg_dict = []
target_avg = 75
for name, avg in stu_avg_dict_1.items():
    if avg > target_avg:
        print(f"{name}:{avg:.2f}")
        avg_dict.append({name: avg})

print(avg_dict)

