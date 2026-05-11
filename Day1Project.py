#Basic Student Report System Using Lists and Dictionaries
# Tasks:
# Store 3 students as dictionaries with name, and marks for 3 subjects
# Put all 3 in a list
# Loop through and print each student's name and their average mark
# Print who has the highest average

student1 = {
    "name":"John",
    "marks":[50,40,30]
    }   
student2 = {
    "name":"Jane",          
    "marks":[60,70,80]
    }
student3 = {
    "name":"Doe",
    "marks":[90,80,70]
    }

students = [student1, student2, student3]
for student in students:
    print(f'{student["name"]} Average: {sum(student["marks"]) / len(student["marks"]):.1f}')
highest_avg = 0
top_student = ""
for student in students:
    avg= sum(student["marks"])/len(student["marks"])
    if avg > highest_avg:
        highest_avg = avg
        top_student = student["name"]
    
print("Top student:", top_student, "with average:", highest_avg)