'''
1 for snake
-1 for water
0 for gun
'''

print("*******************************************")
print("              WELCOME                      ") 
print("*******************************************")
import random
computer=random.choice([-1,0,1])  #using random 

you=input("ENTER YOUR CHOICE :").lower()  #converting into lowercase

youdict={"s":1,"w":-1,"g":0}  #CONVERT CHOICE INTO NUMBER
younum=youdict[you]


reversedict={1:"SNAKE",-1:"WATER",0:"GUN"} #CONVERT NO INTO WORD 

print(f"YOUR CHOICE is {reversedict[younum]}\n COMPUTER CHOICE IS {reversedict[computer]} ")

if(computer==younum):
    print("drawww!!")
else:
    if(computer==-1 and younum==1):
        print("YOU WIN!")
    elif(computer==-1 and younum==0):
        print("YOU lOSE!")
    elif(computer==1 and younum==-1):
        print("YOU lOSE!")
    elif(computer==1 and younum==0):
        print("YOU lOSE!")
    elif(computer==0 and younum==-1):
        print("YOU lOSE!")
    elif(computer==0 and younum==1):
        print("YOU WIN!")
    else:
        print("Something went wrong.....??")