fruits=['apple','Mango','banana','orange']
vegies=['carrot','cucumber','spinach','onion']
meats= ['chcken','mutton','turkey','lamb']

groceries=[fruits,vegies,meats]
print(groceries)

for collections in groceries:
    for food in collections:
        print(food,end=" ")
    print()