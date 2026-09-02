names = ["archana", "manikanta", "lasya", "anjali"]

marks = [90, 30, 70, 100]

attendance = [91, 78, 45, 68]

total = sum(marks)

average = total / len(marks)

print("highest marks:", max(marks))
print("lowest marks:", min(marks))

print(names)
print(marks)
print(attendance)

highest = max(marks)
print("highest marks:", highest)

print("student:", names[marks.index(highest)])

lowest = min(marks)
print("lowest marks:", lowest)

print("student:", names[marks.index(lowest)])

print("average marks:", average)

unique_names = set(names)
print("unique students:", unique_names)

print("total students:", len(unique_names))