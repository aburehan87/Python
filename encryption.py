#programme for encryption and decryption of the string
import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)#this will seperate every letter in the string chars


key=chars.copy()#this will store all elements of the chars in the key
random.shuffle(key)#shuffles the elements in the key every next time



#encryption
text=input("Enter your password:")
cipher_text=""
for letter in text:
    index=chars.index(letter)#i will go in every letter in the text and store the value in the variable index from chars
    cipher_text+=key[index]#this will update the cipher text with the letters in the key

print(f"Original password :{text}")
print(f"Ecrypted password: {cipher_text}")

#decryption
cipher_text=input("Enter an encrypted password to decrypt it:")#here we put the encypted text to generate it into the normal text
text=""
for letter in cipher_text:
    index=key.index(letter)
    text+=chars[index]
print(f"Original Password:{text}")


    

