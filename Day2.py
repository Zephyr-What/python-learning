# FUNCTIONS AND STRING METHODS
def greet(name):
    return f"hello {name}"
print(greet("Imad"))
# multi return values
def getstats(marks):
    return sum(marks), len(marks), sum(marks)/len(marks)

marks = [50,40,30,20,10,33,56]
total , count , avg = getstats(marks)
print (f"Total Marks : {total}, No of Subjects :{count}, Average : {avg:.1f}")

name = " imad hussain "
print(name.strip())
print(name.title())
print("Imad Hussain".split())
print(" ".join(["Imad","Hussain"]))
print("Computer".replace("o","pop"))