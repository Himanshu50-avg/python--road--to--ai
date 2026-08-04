#grading system
print("********************************************")
print("                WELCOME               ")
print("********************************************")

marks=int(input("enterr your marks :"))

if(marks<=100 and marks>=90):
    grade="A "
elif(marks<= 90 and marks>=80):
    grade="B"
elif(marks<=80 and marks>=70):
    grade="C"
elif(marks<=70 and marks>=60):
    grade="D"
elif(marks<=60):
    grade="F"

print("YOUR GRADE IS",grade)

print("********************************************")
print("                THANK YOU             ")
print("********************************************")
    