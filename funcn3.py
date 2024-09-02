# " *args " = used to pass multiple arguments in the funcn

def hello(*args):
    for arg in args:
        print(arg,end=" ")
        
hello('Hellow','Rehan','Waddo')
