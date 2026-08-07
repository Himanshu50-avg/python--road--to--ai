# with is used to automatically close the file 


with open("myfile.txt","w") as f:
    st="hello!!\nu are amazing"
    f.write(st)

# you don't have to close file