'''wap to create dict of hindi words with values as their english translation
provide user choice to  look it up'''

s={"kursi":"chair",
   "billi" : "cat",
   "machli":"fish"}

print(s)

word=input("enter word in hindi to see translation in englsih::--")
print(s.get(word))