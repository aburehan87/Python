#validate user input exercises:
#1.username is no more than 12 char
#2.username does not contains any spaces
#3.username does not contains any digits

username=input("Enter your Username:")
if len(username) > 12:
    print("Not more than 12 characters")
elif not username.find(" ")==-1:
    print("Username cant contain spaces in between")
elif not username.isalpha():
    print("Username cannot contain digits")
else:
    print(f"Welcome {username}")
    