import  random
class train:

    def __init__(self,trainNO):
        self.trainNO=trainNO

    def book(self,trainNO):
        print(f"Ticket is booked in{self.trainNO}")

    def getstatus(self):
        print(f"your  train {self.trainNO} is running on Time")

    def getfare(self,startingadd,destination):
        print(f"Fare of Ticket from {startingadd} to {destination} in {self.trainNO} is {random.randint(2,555)}")


x=train(11200)
x.book()
x.getstatus()
x.getfare('AHMEDABAD','CHAPRAA')