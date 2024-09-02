foods=[]
prices=[]
total=0

while True:
    food=input("Enter food to buy:(q to Quit)")
    if food=='q':
        break;
    else:
        price=float(input("Enter price of your food:"))
        foods.append(food)
        prices.append(price)
print("---Your Cart---")

for food in foods:
    print(food,end=" ")
for price in prices:
    total+=price
print()    
print(f"Your total cart bill is: {total}")
