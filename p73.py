#using lower()
#input a character and output vowel or not

ch1=(input("Enter a character:\n"))
ch2=ch1.lower()

if ch2 in 'aeiou':
    print(f"{ch1} is a vowel")
    
else:
    print(f"{ch1} is not a vowel")