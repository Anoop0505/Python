maarks=eval(input("enter elements in ():"))
sum=0
n=len(marks)
for i in range(n):
    sum=sum+marks[i]
print("Sum of all marks=",sum)
print("average of the course=",sum/n)
print('highest mark=",max(marks))
print('lowest mark=',min(marks))    