class calculator:
    def __init__(self,n):
        self.n=n


    def sqaure(self):
        print(f"SQUARE IS {self.n*self.n}")
    def cube(self):
            print(f"CUBE IS {self.n*self.n*self.n}")
    
    def sqaureroot(self):
            print(f"SQUAREROOT IS {self.n**1/2}")
    
    
a=calculator(4)
a.sqaure()
a.cube()
a.sqaureroot()