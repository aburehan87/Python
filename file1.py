#file handling in python

f=open("rehan.txt","r")	#openening the file in "r" i.e. read mode

text=f.read()	#reading the file

f.close()	#closing the file

print(text)		#printing the file after storing the contents in the "text" variable

#readlines()[0:4]: this  will read the  lines starting from zero to 3rd linex