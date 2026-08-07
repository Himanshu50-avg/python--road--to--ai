f=open("file.txt")
'''data=f.readline()
line2=f.readline()
dd=f.readlines()
print(data)
print(line2)
print(dd)
print(type(data))
print(type(dd))'''

line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()
f.close()