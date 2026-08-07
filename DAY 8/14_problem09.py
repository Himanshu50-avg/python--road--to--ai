'''to cheeck whether a file is identical
and matches the content of other'''

with open("file.txt")as f:
    content=f.read()
with open("file2.txt") as f:
    content2=f.read()
if(content==content2):
    print("Yes both files are identical")
else:
    print("no")