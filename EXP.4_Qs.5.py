#EXP4_QS5-Q1
def GrossSalary(basicpay,DA,HRA,IncomeTax,ProfessionalTax):
    print("Gross Pay\n",basicpay+DA+HRA-IncomeTax-ProfessionalTax)
    
    
basicpay=int(input("Enter the basic pay\n"))
DA=basicpay/100*40
HRA=basicpay/100*25
IncomeTax=int(input("Enter the incometax\n"))
ProfessionalTax=int(input("enter the professionaltax\n"))
GrossSalary(basicpay,DA,HRA,IncomeTax,ProfessionalTax)






#EXP4_QS5-Q2
def dec_bin(num):
    if(num>1):
        dec_bin(num//2)
    print(num%2, end=' ') 

    
    
num=int(input("Enter the decimal number\n"))
dec_bin(num)
