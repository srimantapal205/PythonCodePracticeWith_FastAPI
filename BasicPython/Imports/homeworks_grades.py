"""
- Modules get used all the time throughout the code.
- It helps with creating more files, with unique purposes, to help with clean maintainable code.
"""

homeworkAssignmentGrade = {
    'homework1': 85,
    'homework2': 90,
    'homework3': 78,
    'homework4': 92,
    'homework5': 88
}

def calculate_homework(homework_assignment_arg):
    sum_of_grades = 0
    average_grade =0
    for homework in homework_assignment_arg.values():
        sum_of_grades +=homework
        print(f'sum_of_grades with {homework}:: {sum_of_grades}')

    final_grade = round(sum_of_grades / len(homeworkAssignmentGrade),2)
    print(f'final average grade :: {final_grade}')


calculate_homework(homeworkAssignmentGrade)
