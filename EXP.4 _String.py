#Q_1
def itemcheck(item):
    val=True
    item=input('Enter the item')
    if len(item)<=3:
        print(item[1:3],item(-1))
        val=False
        
    else:
        print('Enter the item again\n')
    return val
    
    
    
    
if(itemcheck('Chocolate')):
    print('valid')
else:
    print('Invalid')
    
    
    
    
    
    
#Q_2
#def split(string):
    
    
    
    
    
    
    
    
    
    
    
    
    
#Q_3    
#def passcheck(password):
#    val=True
#    
#    if(len(password)<=6 and len(password)>=12):
#       print('Minimum length is 6 to 12')
#       val=False
#    
#    for i in password:
#        if i.isalpha():
#            break
#    else:
#        print('password should have at least one albheat')
#        val=False
#    
#    for i in password:
#        if i.isdigit():
#            break
#    else:
#        print('password should have at least one number')
#        val=False
#        
#    sym="@#$"
#    for i in password:
#        if i in sym :
#            break
#    else:
#        print('password should have at least one special symbole')
#        val=False
#        
#    return val
#
#if(passcheck("12abc#dgb")):
#             print('Valid')
#else:
#    print('Invalid')