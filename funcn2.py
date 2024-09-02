#count timer
import time

def count(start,end):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Job Done!")
count(0,5)
