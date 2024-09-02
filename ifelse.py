#ifelse statements

bill=int(input("Enter your bill:"))

if bill>1000:
    print("10% discount:")
elif bill>2000:
    print("20% discount")
elif bill>3000:
    print("You get a gift hamper")
else:
    print("Get out")


#eg

name=input("Enter your name:")

if name=="":
    print("Please enter your name:")
else:
    print(f"Hello {name}")
