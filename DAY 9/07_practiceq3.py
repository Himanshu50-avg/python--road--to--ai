class demo:
    a=4


b=demo()
b.a=5
print(b.a)
print(demo.a)

'''the answer is 5  bcoz object attribute is always 
given precendance above object attribute'''