a=int(input("enter your marks in sub1 :")) 
b=int(input("enter your marks in sub2 :")) 
c=int(input("enter your marks in sub3 :")) 

#check for total percent
total_percentage=(100*(a+b+c))/300

if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("YOU ARE PASS")
else:
    print("YOU ARE FAIL")
