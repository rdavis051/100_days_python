# this program is use to interpret students scores and create a new 
# dictionary of students grades that corresponds with the scores.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoione": 99,
    "Draco": 74,
    "Neville": 62,
}

print(student_scores)
# ToDo-1: Create an empty dictionary called student_grades
student_grades = {}

# ToDo-2: Write your code below to add the grades to student_grades

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# Don't change the code below
print(student_grades)
