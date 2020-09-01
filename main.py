
import random

def encrypt(text, k):
    encrypted_message = ""

    for i in text:
        p = s.find(i)
        new_p = (p + k) % 26
        encrypted_message += s[new_p]
    return encrypted_message


def decrypt(text,k):
    decrypted_message = ""

    for i in text:
        p = s.find(i)

        new_p = (p - k) % 26

        decrypted_message += s[new_p]
    return decrypted_message

plain_text=input("Enter your message \n")
s="abcdefghijklmnopqrstuvwxyz"
key= random.randint(1, 25)
print("key is :",key)
option=int(input("choose a option : \n 1.encryption \n 2.decryption \n"))

if option==1:
    ans=encrypt(plain_text,key)
    print("Encrypted_message : ", ans)

elif option==2:
    ans=decrypt(plain_text,key)
    print("Decrypted_message : ",ans)
