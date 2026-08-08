class emp:
    sal=120000
    def getinfo(self):
        print(f"salary is {self.sal}")

    @staticmethod  #usse of static 
    def greet():
        print("good morning")

x=emp()
print("program started")
x.greet()
x.getinfo()