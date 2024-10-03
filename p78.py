#using while loop
#calculate sum of all numbers from 1 to x

x=int(input("Enter x:\n"))

sum,i=0,1

while i<=x:
    sum=sum+i
    i+=1
    
    
    print(f"sum:{sum}")
    