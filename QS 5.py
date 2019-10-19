#Question Set 5_1
h=int(input('Enter the hardness of the steel \n'))
c=float(input('Enter the carbon content of the stell\n'))
t=int(input('Enter the tensile strength of the stell\n'))
if h>50 and c<0.7 and t>5600:
    print('Grade 10')
elif h>50 and c<0.7:
    print('Grade 9')
elif c<0.7 and t>5600:
    print('Grade 8')
elif h>50 and t>5600:
    print('Grade 7')
elif h>50 or  c<0.7 or t>5600:
    print('Grade 6')
else:
    print('Grade 5')
    
    
    
    


#Question Set 5_2
h=int(input('Enter the class held\n'))
a=int(input('Enter the class attended\n'))
print('Number of class held {} and Number of class attended {}\n'.format(h,a))
p=a/h*100
print('Pengentage of class attended=\n',p)
if p>75:
    print('Student is allowed for exam\n')
else:
    print('Student is not allowed for exam\n')








#Question Set 5_3
p=int(input('Enter the percentage \n'))
if p>=90:
    print('Distinction')
elif p>=80 or p>90:
    print('First Class')
elif p>=70 or p>80:
    print('Second Class')
elif p>=60 or p>70: 
    print('Third  Class')
else: 
    print('Fail')     