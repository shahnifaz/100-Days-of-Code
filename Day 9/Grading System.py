student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for names in student_scores:
    score = student_scores[names]
    if score > 90:
        student_grades[names] = "Outstanding"
    elif score > 80:
        student_grades[names]= "Exceeds Expectations"
    elif score > 70:
        student_grades[names] = "Acceptable"
    else:
        student_grades [names] = "Fail"

print(student_grades)