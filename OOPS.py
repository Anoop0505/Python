class Person:
    def __init__(self,name,number,mobilenumber,address):
        self.name=name
        self.number=number
        self.mobilenumber=mobilenumber
        self.address=address
class student(Person):
    def setdata(self,branch,studenttype,CGPA):
        self.branch=branch
        self.studenttype=studenttype
        self.CGPA=CGPA
    def getdata(self):
        return(self.name,self.number,self.mobilenumber,self.address,self.branch,self.studenttype,self.CGPA)
    
class professor(Person):
    def setdata(self,typeofemployment,subjecttaught,salary):
        self.typeofemployment=typeofemployment
        self.subjecttaught=subjecttaught
        self.salary=salary
    def getdata(self):
        return(self.name,self.number,self.mobilenumber,self.address,self.subjecttaught,self.salary)
s1=student("Raja",201,"9876543210","Kormangala,bangalore")
s1.setdata("CSE","Dayscholar",7)
print(s1.getdata())
p1=professor("Elango",1001,"0123456789","Anna Nagar Chennai")
p1.setdata("Part time","Python",50000)
print(p1.getdata()) 



       