#weight conversion

weight=float(input("Enter your weight:"))
type=input("K or L ?:")

if type=="K":
    weight=weight*2.205
    unit="Lbs"
elif type=="L":
    weight=weight/2.205
    unit="Kgs"
print(f"Your weight is {round(weight)} {unit}")
