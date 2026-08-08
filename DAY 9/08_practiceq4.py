# using static
class demo:
    a=4
    @staticmethod  #not usings self
    def greet():
        print("hello")

b=demo()
b.a=5
b.greet()
print(b.a)


