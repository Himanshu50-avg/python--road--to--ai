# wap to get sum of n natural number 
n=(int(input("enter number :")))
i=1
sum=0
'''while(i<=n):
    sum += i
    i=i+1
print(sum)'''


for i in range(n+1):
        sum += i
        i=i+1
print(sum)


