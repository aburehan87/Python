#logcical OR
#input age and output eligible or not

age=int(input("Enter age\n"))

if age<7 or age>65:
    print("Entry is  not allowed")
    
else:
    print("Entry is allowed")