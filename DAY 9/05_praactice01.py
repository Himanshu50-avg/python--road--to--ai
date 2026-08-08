class Programmer:
    company='MICROSOFT'

    def __init__(self,name,salaray,pincode):
        self.name=name
        self.salaray=salaray
        self.pincode=pincode

x=Programmer("HIMANSHU",1200000,370511)
print(x.name,x.salaray,x.pincode,x.company)
r=Programmer("ROHAN",1200000,370511)
print(r.name,r.salaray,r.pincode,r.company)