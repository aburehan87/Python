#email slicer

email=input("Enter your email:")
result=email.index("@")

username=email[:result]
domain=email[result+1:]#+1 will print letters after "@"

print(f"Your username is {username} and your domain is {domain}")

