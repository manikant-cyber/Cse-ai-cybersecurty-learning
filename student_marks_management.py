students = {
    "archana": 90,
    "manikanta": 70,
    "lasya": 100,
    "anjali": 30
}

print(students)
print(students["archana"])

students["rahul"] = 85
print(students)

students["rahul"] = 95
print(students)

del students["anjali"]
print(students)

print(students.values())
print(students.items())

total = sum(students.values())
print("total marks:", total)

average = total / len(students)
print("average :", average)

highest = max(students.values())
print("highest marks:", highest)

lowest = min(students.values())
print("lowest marks:", lowest)