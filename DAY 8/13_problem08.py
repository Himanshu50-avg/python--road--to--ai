'''make copy of file'''


with open("file.txt")as f:
    content=f.read()
with open("file2.txt",'w')as f:
    f.write(content)