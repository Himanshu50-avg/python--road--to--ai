l=["hary","rohan","an"]

def rrem(l,word):
    for item in l:
        n=[]
        if item!=word:
            n.append(item.strip(word))
        return n
        l.remove(word)
        return l

print(rrem(l,"an"))