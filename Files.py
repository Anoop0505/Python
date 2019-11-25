##q_1
#fp=open("D:\COMPPB38596rProrPr__numbers.txt","r")
#m=[]
#for i in fp:
#    m.append(int(i))
#    
#leng=len(m)
#tot=sum(m)
#mini=min(m)
#maxi=max(m)
#print(leng,tot,mini,maxi)    

#
##q_2
#fp1=open("D:\grades.txt","r")
#fp2=open("D:\out.txt","w")
#
#for i in fp1:
#    test=i.split()
#    rollno=test[0]
#    na=test[1]
#    to=int(test[2])+int(test[3])+int(test[4])+int(test[5])+int(test[6])
#    avg=int(to/5)
#    print(rollno,na,to,avg,file=fp2)
#fp1.close()
#fp2.close()


##q_3
#def printwords(N,data):
#    dictkeys=list(data.keys())
#    dictkeys.sort()
#    for w in dictkeys:
#        cnt=data[w]
#        if(cnt >=N):
#            print("word \"{}\"is present {} times".format(w,cnt))
#wholetext=""
#fp=open("D:\COMPPB34108rProrPr__sample_text.txt","r")
#wholetext=fp.read()
#mydict=dict()
#temp=wholetext.replace("\n"," ")
#for word in temp.split(" "):
#    if(word not in mydict):
#        mydict[word]=1
#    else:
#        mydict[word] +=1
#        
#fp.close()
#print("The file has lines \n",wholetext.count("\n")+1)
#
#print("The total number of distinct word is \n",len(mydict))
#printwords(5,mydict)





##q_4
#fp1=open("D:\\income.txt","r")
#fp2=open("D:\\final.txt","w")
#m=[]
#mc=0
#fc=0
#f=[]
#for i in fp1:
#    text=i.split()
#    if(text[0]=="M"):
#        mc+=1
#        m.append(int(text[1]))
#    else:
#        fc+=1
#        f.append(int(text[1]))
#a=sum(m)
#b=sum(f)
#avgm=a/mc
#avgf=b/fc
#print(mc,fc,avgm,avgf,file=fp2)
#fp1.close()
#fp2.close()









##q_5
#try:
#    f1=open("D:\\input.txt","r")
#    a=f1.read()
#    f2=open("D:\\output.txt","w")
#    f2.write(a[::-1])
#except FileNotFoundError as e1:
#    print(e1)
#except IOError as e2:
#    print(e2)
#finally:
#    f1.close()
#    f2.close()






##q_6
#custumerid=[]
#n=int(input("enter the number of customers"))
#for i in range(0,n):
#    try:
#        id=int(input("enter the customer id"))
#        if(id<0):
#            raise ValueError ("customer id should be positive")
#        if(id<1001 or id>1100):
#            raise ValueError ("customer id should be in limt of (1001-1100)")
#        custumerid.append(id)
#    except ValueError as e:
#        print(e)
#print("custumers id",custumerid)







#q_7
custumerid=[]
n=int(input("enter the number of customers"))
for i in range(0,n):
    try:
        sal=int(input("enter the customer salary"))
        if(sal<0):
            raise ValueError ("customer id should be positive")
        custumerid.append(sal)
        name=input("enter the name")
        custumerid.append(name)
        job=input("enter the type of job")        
        ide=int(input("enter your id"))
        custumerid.append(ide)
        if(job!="fulltime" or job!="parttime"):
            raise ValueError ("costumer job should be either pat time or full time")
        custumerid.append(job)    
    except ValueError as e:
        print(e)
print("custumers id",custumerid)