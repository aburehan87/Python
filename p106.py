#using tuple
#addition of list and tuple by conversion

ob1=[10,20,30]
ob2=(40,50,60)
#1:list+list
ob3=ob1+list(ob2)
print(ob3)
#2:tuple+tuple
ob3=tuple(ob1)+ob2
print(ob3)