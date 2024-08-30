ms=input("Enter Maritial status:")
gen=input("Enter gender:")
age=int(input("Enter age:"))
if(ms=="M"):
    print("JOB is ensured")
elif(ms=="UM" and age>30 and gen=="M"):
    print("Job is ensured")
elif(ms=="UM" and age>25 and gen=="F"):
    print("Job is ensured")
else:
    print("Job is not ensured")