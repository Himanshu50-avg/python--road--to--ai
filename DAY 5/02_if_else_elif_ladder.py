a=int(input("enter your age:"))
if(a>=18):
    print("you are above the age of consent")
elif(a<0):
    print("you aare entering a invalid age")
elif(a==0):
    print("you are not entering a valid age")
else:
    print("below the age of consent")