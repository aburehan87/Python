#using append
#inout 2 list and output their addition in the third one

l1=[10,20,30]
l2=[5,6,7]
l3=[]

for x,y in zip(l1,l2):
    l3.append(x+y)
#end(for)
    print(l3)