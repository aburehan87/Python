#using functions

def add(x,y):
    z=x+y
    print(f"Addition is {z}")
#end:add
    
def main():
    print("Enter two numbers:", end=" ")
    a,b=int(input()), int(input())
    add(a,b)
#end:main
    
main()

