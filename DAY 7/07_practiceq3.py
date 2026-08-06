# c/5=(f-32)/9


def tempconverter(F):
    c=round(5*(F-32)/9,2)    #round fuction used
    print(f"{F} in celsius is{c}")

F=int(input("enter temp in F"))
tempconverter(F)