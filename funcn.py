# functions=a block of reusable code

#a code for printig happy bday three times


def happy(name,age):
    print(f"Happy Birthday to {name}")
    print(f"Your are {age} years old")

happy("Shabuddin",21)
happy("Rehan",20)
happy("Adib",20)

def add(num1,num2):
    return num1+num2

print(add(2,3))

def mult(num3,num4):
    return num3*num4

print((mult(2,3)))


def name(first_name,last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    return first_name + " " + last_name
full_name=name("rehan","waddo")
print(full_name)

    