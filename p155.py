def prime(n):
    i=2
    while i<n-1:
        if n%i==0:
            return False
        i+=1
        return True
def main():
    x=int(input("Enter x:"))
    if prime(x):
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime")
main()