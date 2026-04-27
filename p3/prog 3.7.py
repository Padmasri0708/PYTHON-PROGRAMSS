list=[10,20,30,"Python",True,False,1,56]
print(list)
x=list.copy()
print(list)
list.pop(3)
print(list)
del list[5]
print(list)
list.reverse()
print(list)
list.clear()
print(list)





flavour=input("Enter your icecream choice:")
if flavour=="Chocolate":
    print("You'll get one free")
elif flavour=="Vennella":
    print("You have no taste")
elif flavour=="Butterscotch":
    print("You are a kid to buy it")
else:
    print("other")
