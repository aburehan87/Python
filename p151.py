def main():
    l1=[10,20,30]
    l2=list(map(lambda a:a**2,l1))
    l3=list(map(lambda b:b**3,l2))
    print(l1,l2,l3,sep="\n")
main()