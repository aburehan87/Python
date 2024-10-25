#using append
#short programme of previous programme

l1=[10,20,30]
l2=[5,60,7]
l3=[]

l3=[x if x>y else y for x,y in zip(l1,l2)]
print(l3)