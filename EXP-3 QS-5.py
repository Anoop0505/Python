#EXP_3_Q1 
lijst = list(range(1, 101))
i = 0

while i < 100:
    print("{:>5d}".format(lijst[i]), end=" ")
    i = i+1
    if i % 10 == 0:
        print("")







#EXP_3_Q2
n=int(input("enter number of rows"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()    
