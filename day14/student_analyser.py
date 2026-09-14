# Day 14 - Sprint Review
# Student Performance Analyzer

students = [
    ["Aman", 85],
    ["Riya", 92],
    ["Karan", 67],
    ["Simran", 74],
    ["Rahul", 92],
    ["Neha", 56],
    ["Arjun", 85],
    ["Mehak", 45]
]

total_marks = 0
highest = students[0]
lowest = students[0]

grade_count = {}

# Process the dataset
for student in students:
    name = student[0]
    marks = student[1]

    total_marks = total_marks + marks

    # Find highest marks
    if marks > highest[1]:
        highest = student

    # Find lowest marks
    if marks < lowest[1]:
        lowest = student

    # Assign grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    # Store grade frequency using hashmap
    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1


average = total_marks / len(students)

print("----- Student Performance Report -----")

print("Total Students:", len(students))
print("Average Marks:", average)

print("Highest Scorer:", highest[0], "-", highest[1])
print("Lowest Scorer:", lowest[0], "-", lowest[1])

print("\nGrade Distribution:")

for grade in grade_count:
    print(grade, ":", grade_count[grade])

print("\n----- Insights -----")

if average >= 75:
    print("Overall performance is good.")
else:
    print("Overall performance needs improvement.")

print("Highest marks were scored by", highest[0])
print("Lowest marks were scored by", lowest[0])
