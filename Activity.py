#l=input('enter values').split(" ")
#a=input('enter value to be searched')
#for i in range(0,len(l)):
#    if a is l[i]:
#        pass
#    print("Position:",i)
#print(i)
#print('count is: ',l.count(a))
#
#





#i=11
#s=10
#while i==10:
# s=s-1
# i=i-1
# avg=i/10
#print("the sum of first 10 numbers is",s)
#print("the average of first 10 numbers is", avg)



#for i in range(1,6):
#     print(i,end="")
#print("")
#for j in range(1,6):
#     print(j,end="")




#string="python is easy"
#a='yes '
#print(a+string)






#for i in range(1,10):
#    print(i=i[:2],end="")
#
#




#max1=0
#max2=0
#n=int(input("Enter the number of element in the list"))
#L=[]
#for i in range(0,n):
#    L.append(int(input("Enter the number")))
#for i in range(0,len(L)):
#    if L[i]>max1:
#        max1=max2
#        max1=L[i]
#    elif L[i]>max2 and L[i]<max1:
#        max2=L[i]
#print("First max",max1)
#print("Second max",max2)



#n=int(input("Enter value of n : "))
#for i in range(n//2,n+1,2):
#    for j in range(1,n-i,2):
#        print(" ",end="")
#    for j in range(1,i+1) :
#        print("*")
#    for j in range(1,n-i):
#        print(" ",end="")
#    for j in range(1,i):
#        print("*",end="")
#        print("\n")
#for i in range(n,0,-1):
#    for j in range(i,n):
#        print(" ",end="")
#    for j in range(1,((i*2)-1)):
#        print("*",end="")
#        print("\n")





#res=0
#def check_relation(a,b):
#    if a==b:
#        return 0
#    elif a>b:
#        return 1
#    elif a<b:
#        return -1
#check_relation(3,5)
#if res=='0':
#    print("a is equal to b")
#elif res=='1':
#    print("a is greater than b")
#elif res=='-1':
#    print("a is less than b")
#
#
#
#
#
#
#
#


# Pyhton 3 code to print a HEART Shape 
  
# HERE, we have set the size of Heart, 
# size = 10 
size = 15
  
# FOR THE APEX OF HEART  
for a in range(int(size / 2), size + 1, 2): 
      
    # FOR SPACE BEFORE PEAK-1 : PART 1 
    for b in range(1, size - a, 2):  
        print(" ", end = "") 
  
    # FOR PRINTING PEAK-1 : PART 2 
    for b in range(1, a + 1): 
        print("*",end="")
  
    # FOR SPACE B/W PEAK-1 AND PEAK-2 : 
    # PART 3 
    for b in range(1, (size - a) + 1): 
        print(" ", end = "") 
          
    # FOR PRINTING PEAK-2 : PART 4 
    for b in range(1, a): 
        print("*",end = "") 
  
    print("") 
      
  
# FOR THE BASE OF HEART ie. THE INVERTED 
# TRIANGLE  
for a in range(size, -1, -1): 
      
# FOR SPACE BEFORE THE INVERTED TRIANGLE: 
# PART 5  
    for b in range(a, size): 
        print(" ", end = "") 
          
    # FOR PRINTING THE BASE OF TRIANGLE: 
    # PART 6 
    for b in range(1, (a * 2)): 
        print("*",end = "") 
    print("")  








