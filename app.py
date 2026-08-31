print("GitHub Actions Deployment Started")
print("CI/CD Test Started")

import json

# Read student data
with open("students.json", "r") as file:
    students = json.load(file)

# Find the student with the highest marks
topper = max(students, key=lambda student: student["marks"])

print("===== Student Report =====")
print("Topper :", topper["name"])
print("Marks  :", topper["marks"])