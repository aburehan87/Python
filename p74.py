#using lower()
#input char and output vowel or not

ch1=input("enter a character\n")

if ch1.lower() in 'aeiou':
    print(f"{ch1} is a vowel")
    
else:
    print(f"{ch1} is not a vowel")