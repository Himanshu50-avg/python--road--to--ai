'''wap to write the greatest of four numbers entered
 by user'''

a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
d=int(input("enter fourth number :"))

if(a>b and a>c and a>d):
    print(a, "is the largest number among all four no.")

elif(b>a and b>c and b>d):
    print(b,"is the largest number among all four no.")

elif(c>a and c>b and c>d):
    print(c,"is the largest number among all four no.")
elif(d>a and d>c and d>b):
    print(d,"is the largest number among all four no.")
