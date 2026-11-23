students = [
    {"name": "Lavanya", "marks": 90},
    {"name": "satya", "marks": 75},
    {"name": "Priya", "marks": 85}
]

ascending = sorted(students, key=lambda x: x["marks"])

descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
for student in ascending:
    print(student)

print("Descending Order:")
for student in descending:
    print(student)
