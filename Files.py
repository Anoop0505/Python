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


##q_2
#fp1=open("D:\COMPPB38596rProrPr__Grades.txt","r")
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


#q_3
def printwords(N,data):
    dictkeys=list(data.keys())
    dictkeys.sort()
    for w in dictkeys:
        cnt=data[w]
        if(cnt >=N):
            print("word \"{}\"is present {} times".format(w,cnt))
wholetext=""
fp=open("D:\COMPPB34108rProrPr__sample_text.txt","r")
wholetext=fp.read()
mydict=dict()
temp=wholetext.replace("\n"," ")
for word in temp.split(" "):
    if(word not in mydict):
        mydict[word]=1
    else:
        mydict[word] +=1
        
fp.close()
print("The file has lines \n",wholetext.count("\n")+1)

print("The total number of distinct word is \n",len(mydict))
printwords(5,mydict)