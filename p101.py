#using append
#input 2 list and output third using if else

l1=[10,20,30]
l2=[5,60,7]
l3=[]

for x,y in zip(l1,l2):
    l3.append(x if x>y else y)
    print(l3)