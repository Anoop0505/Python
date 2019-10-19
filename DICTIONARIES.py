Mobile={"brand": "samsung", "model": "S10", "Screen size":6.1}
#print(Mobile)
#print(Mobile["model"])
#print(Mobile.get("model")) 
#Mobile ["model"] ="S11"
#print(Mobile)
#for i in Mobile:
# print(i)
#for i in Mobile:
# print(Mobile[i])
#for i in Mobile.values():
# print(i)
#for x,y in Mobile.items():
# print(x,y)
#if "model" in Mobile:
# print("yes")
#
#print(len(Mobile))
#Mobile["colour"]="white"
#print(Mobile)
print(Mobile.pop("model"))
print(Mobile)
print(Mobile.popitem())
print(Mobile)
del Mobile["brand"]
print(Mobile)