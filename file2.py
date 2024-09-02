#file2

f=open("Brocode.txt","x")
f.close()

f=open("Brocode.txt","a")
text=f.write("Rehan Waddo")

f=open("Brocode.txt","r")
text=f.read()
f.close()
print(text)