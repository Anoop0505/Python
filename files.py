#fh=open("D:\COMPPB34108rProrPr__Grades (1).txt","r")
####print(fh.read(5))
####print(fh.read(None))
####print(fh.read())
####print(fh.read(5000))
####print(fh.readline(5))
####print(fh.readlines(50))
####print(fh.readlines(500))
####for x in fh:
#### print(x,)
####with open("D:\COMPPB34108rProrPr__Grades (1).txt","r") as fh:
####    content=fh.read(10000)
####    print(content)
##fh=open("D:\COMPPB34108rProrPr__Grades (1).txt","r")
##print(fh.tell())
##print(fh.read(1))
##print(fh.tell())
#fileptr = open("D:\COMPPB34108rProrPr__Grades (1).txt","r")
#print("The file pointer is at byte :",fileptr.tell())
#fileptr.seek(10);
#print("After reading, the file pointer is at:",fileptr.tell())
#fout=open("D:\COMPPB34108rProrPr__Grades (1).txt","w") 
#print("hello",file=fout)
#fout.close () 
#print(fout)
fh1=open("D:\\a.txt","r")
L=[]
for x in fh1:
    L.append(int(x))
length=len(L)
tot=sum(L)
minmum=min(L)
maximum=max(L)
print(length,tot,minmum,maximum)