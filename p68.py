#nested single line if else
#input number output +ve -ve or zero

x=int(input("Enter a number\n"))
print(f"{x} is positive") if x>0 else print(f"{x} is negative") if x<0 else print(f"{x} is zero")