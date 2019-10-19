#m=[]
#
#for i in range(1,20):
#    if i%2==0:
#        m.append(i)
#print(m)



#item=input('enter the number with space').split(' ')
#print(item)
#l=[]
#
#for i in item:
#    if i not in l:
#        l.append(i)
#print(l)
#





p=input('Enter the name with comma\n').split(',')
L=[]
firstname=[]
for i in p:
    L=i.split(" ")
    firstname.append(L[1])
print(firstname)
    