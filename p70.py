#Relational operators
#logocal AND
#input 3numbers and output greatest

x,y,z=int(input("ENter three numbers\n")),int(input()),int(input())

if   x>y and y>z:
    print(f"{x} is greatest")

elif y>z:
    print(f"{y} is greatest")
    
else:
    print(f"{z} is greatest")