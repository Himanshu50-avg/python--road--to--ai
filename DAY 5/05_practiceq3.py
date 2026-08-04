'''a spam comment is defined as a text containing
the following keyword;
"Make a lot of money","buy now","subscribe this",
"click this".wap a program to detect the spam'''

print(".................................................")
print("              WELCOME TO SPAM CHECKER            ")
print(".................................................")
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("enter the msg to be checked:")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("the message is a spam")
else:
    print("message is not a spam")

