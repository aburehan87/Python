#if elif(else if)else
#input number output +ve,-ve,zero

x=int(input("Enter a number:"))

if   x>0:
    print(f"{x} is +ve")

elif x<0:
    print(f"{x} is negative")

else:
    print(f"{x} is zero")