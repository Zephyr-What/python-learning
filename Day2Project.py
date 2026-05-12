# DYNAMIC STUDENT REPORT SYSTEM
# Ask how many students to enter
# For each student, take their name and 3 subject marks as input
# Store each student as a dictionary
# Put all of them in a list
# After all input is done, print a full report showing:

# Each student's name, average, and pass/fail status
# Who is the top student
# Class average across all students

num = int(input("Enter Number of Student Records to Enter: "))
students = []
for i in range(num):
    name = input("Enter Student Name: ")
    count = int(input("Enter Number of Subjects: "))
    marks = []
    for j in range(count):
        mark = float(input(f"Enter Mark for Subject {j+1}: "))
        marks.append(mark)
    student ={
        "name" : name,
        "marks" : marks
    }
    students.append(student)
for student in students:
    avg = sum(student["marks"])/len(student["marks"])
    status = "Pass" if avg >=40 else "Fail"
    print(f'{student["name"]} Average: {avg:.1f} Status: {status}')
highest_avg = 0
top_student = ""
for student in students:
    avg= sum(student["marks"])/len(student["marks"])
    if avg > highest_avg:
        highest_avg = avg
        top_student = student["name"]

print("Top student:", top_student, "with average:", highest_avg)
total_avg = sum(sum(student["marks"])/len(student["marks"]) for student in students) / len(students)
print(f"Class Average: {total_avg:.1f}")
