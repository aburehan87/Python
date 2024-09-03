#range
#when u want to skip any number in the range

for x in range(1,20):
    if x==13:#this will skip the number 13
        continue
    else:
        print(x)
        
#nested loops:
        
for y in range(3):#this for loop will repeat the inner loop 3 times
    for x in range(0,9):
        print(x,end="")
    print()#this will create next line after every repeated loop
   
