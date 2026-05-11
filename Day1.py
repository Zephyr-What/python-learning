# marks = [50,40,30,20,10,33,56]
# print(marks[0])
# print(marks[1:4])
# print(len(marks))

# sq = [i**2 for i in range(1,10)]
# print(sq)

# sq= [i**2 for i in range(1,20) if i%2 == 0]
# print(sq)

#DICTIONARY
student = {
    "name":"John",
    "age":20, 
    "marks":[50,40,30]
    }
print(student["name"])
print(student["age"])
print(student["marks"])
for key,value in student.items():
    print(key,value)