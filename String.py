vision='Prefessionals of integrity and character having care and concern for society'
print(len(vision))
print(vision[2])
print(vision[4])
print(vision[-1])
print(vision[1:4])
print(vision[16:25])
print(vision.upper())
print(vision.isupper())
print(vision.lower())
print(vision.casefold())
print(vision.find('care'))
print(vision.find('Presidency'))
print(vision.isalpha())
print(vision.isdecimal())
print(vision.islower())
print(vision.split())
for i in vision:
    print(i)
for i in vision:
    print(i,end='')
print(vision[::-1])


id='2017CSE'
print(id.isalnum())


string2='care; and; concern; for ; society'
#print(string2.split(','))
print(string2.split(';'))


string3='Presidency vision is '
print(string3+vision)