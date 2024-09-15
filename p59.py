#input number and output choice

x,y=int(input("enter two numbers:\n")),int(input())
ch=int(input("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Choice:\n"))

if    ch==1:
    print(f"Add:{x+y}")
    
elif  ch==2:
    print(f"Sub:{x-y}")
    
elif  ch==3:
    print(f"Mult:{x*y}")
    
elif  ch==4:
    print(f"Div:{x//y}")
    
else:
    print("wrong choice")