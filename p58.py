#if elif else
#input 2 numbers and output greatest
x,y=int(input("Enter two numbers:\n")),int(input())

if   x>y:
    print(f"{x} is greatest")
    
elif y>x:
    print(f"{y} is greatest")
    
else:
    print("Equal")