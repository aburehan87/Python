#to create a 2D loop

rows=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
symbol=input("Enter a symbol:")
for i in range(rows):
    for j in range(col):
        print(symbol,end="")
    print()