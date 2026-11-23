students = {
    1: {"name": "Lavanya", "marks": 90},
    2: {"name": "Ravi", "marks": 85},
    3: {"name": "Priya", "marks": 95}
}

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
