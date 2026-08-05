'''wap to  print the following staR PATTERN
*
**
***'''

n=int(input("enter n"))
for i in range(1,n+1):
     print("" * (n+i),end="")
     print("*"* i,end="")
     print("")

