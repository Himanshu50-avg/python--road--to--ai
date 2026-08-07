with open("poem.txt")as f:
    data=f.read()
    if("twinkle" in data):
        print("yes")
    else:
        print("not present")
           