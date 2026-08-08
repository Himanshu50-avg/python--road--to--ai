class emp:
    language="python"
    sal=120000

    def __init__(self,name,sal,language): #dunder method which is automatically called whennew object is called
        self.name=name
        self.sal=sal
        self.language=language
        print("i am creating a object")


    def getinfo(self):
        print(f"the langauge is {self.language} and salary is {self.sal}")

    @staticmethod
    def greet():
        print("Good Morning")



x=emp("himannshu",12000,'java')


x.name="himanshu"  #insted of using this amking a fun
x.greet()
x.getinfo()

print(x.name,x.sal,x.language)