##q_1
#class student:
#    count=0
#    def __init__(self,rollno,name):
#        self.rollno=rollno
#        self.name=name
#        student.count=student.count+1
#        
#obj1=student(11,"Raja")
#print(obj1.rollno)
#print(obj1.name)
#print(obj1.count)
#obj2=student(12,"Elango")
#print(obj2.rollno)
#print(obj2.name)
#print(obj2.count)





##q_2
#class student:
#    def __init__(self,rollno,name,m1,m2,m3,m4,m5):
#        self.rollno=rollno
#        self.name=name
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#        self.m4=m4
#        self.m5=m5
#    def totalmarkes(self):
#        tot=self.m1+self.m2+self.m3+self.m4+self.m5
#        return tot
#obj1=student(11,"Raj",35,45,25,85,65)
#print(obj1.rollno)
#print(obj1.totalmarkes())
#obj2=student(12,"Baj",25,45,58,85,65)
#print(obj2.rollno)
#print(obj2.totalmarkes())
#obj3=student(13,"Saj",85,95,75,25,65)
#print(obj3.rollno)
#print(obj3.totalmarkes())
#obj4=student(14,"Gaj",15,25,35,65,45)
#print(obj4.rollno)
#print(obj4.totalmarkes())
#obj5=student(15,"Raj",75,95,35,15,85)
#print(obj5.rollno)
#print(obj5.totalmarkes())






#q_3
class student:
    def __init__(self,studentid,studentname,branch,sem):
        self.studentid=studentid
        self.studentname=studentname
        self.branch=branch
        self.sem=sem
    def setmarkers(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def getmarkers(self):
        return self.m1,self.m2,self.m3,self.m4,self.m5
    
s=[]

while 1:
    print("1 Add student detalils")
    print("2 Delete student details")
    print("3 Display grade sheet")
    print("4 Exit")
    choice=(int(input("Enter the choice")))
    
    if choice==1:
        sid=int(input("Enter the student id "))
        sname=input("Enter the student name")
        sbranch=input("Enter the branch")
        ssem=input("Enter the sem")






























