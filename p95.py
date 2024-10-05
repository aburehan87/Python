#using append
#enter a list and enter squares of it at the end of the list

l1=[10,20,30]
l2=[]

for x in l1:
        
    l2.append(x*x)

print(l1,l2,sep="\n")