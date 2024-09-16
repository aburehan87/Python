#greatest of three numbers
#logical AND

x,y,z=int(input("Enter three numbers\n")),int(input()),int(input())

if y<x>z:
    print(f"{x} is greatest")
    
elif y>z:
    print(f"{y} is greatest")
    
else:
    print(f"{z} is greatest")