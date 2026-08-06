def greatest(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>x and y>z):
        return y
    else:
        return z

x=int(input("enter a number:"))
y=int(input("enter a number:"))
z=int(input("enter a number:"))
k=greatest(x,y,z)
print(f"THE GREATEST NUMBER IS {k}")