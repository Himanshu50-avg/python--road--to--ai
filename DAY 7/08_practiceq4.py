''' wap to write a recursive function to print
sum of n natural numbers

sum of n = sumof(n-1)+n'''


def sumofn(n):
    if (n==1):
        return 1
    else:
        return sumofn(n-1)+n


k=int(input('enter a number'))
print(sumofn(k))