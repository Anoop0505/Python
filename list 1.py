#p=input('enter the numbers with semicolen\n').split(';')
#q=[]
#s=[]
#
#for i in p:
#    if i.startswith("+91"):
#        q.append(i)
#        
#    elif i.startswith("+1"):
#        s.append(i)
#print("{}".format(q))
#print("{}".format(s))




#l=input('enter values').split(",")
#a=input('enter value to be searched')
#for i in range(0,len(l)):
#    if a is l[i]:
#        print("Position:")
#        print(i)
#        print('count is: ',l.count(a))




#L1=[]
#L2=[]
#n=int(input("enter n"))
#for i in range(0,n):
#    x=int(input("enter list values"))
#    L1.append(x)
#print(L1)
#m=int(input("enter m"))
#for i in range(0,m):
#    x=int(input("enter list values"))
#    L2.append(x)
#print(L2)
#for i in L1:
#    if i not in L2:
#        print('Remove value ',i)
#        print('position',L1.index(i))




c=["Brazil","Russia", "India", "China"," South Africa"]
b=input('Enter the list of country').split(",")
print(b)
for i in b:
    if i not in c:
        print('Country is not present in BRIC',i)

















