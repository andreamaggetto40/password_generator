import random as rand
import time

def init():
    print("Software used to create a password")

def encryption():
    string_to_encrypt = input("Insert string to encrypt : \n")

    if(len(string_to_encrypt) > 0):
        password = ""
        for i in range(len(string_to_encrypt)):
            key = int(input("Insert a number between 1 and 9 : \n"))

            if(key >= 1 and key <= 9):
                helper = ord(string_to_encrypt[i])
                helper += key
                password += chr(helper)
            else:
                print("An error occured!")
                break
        for i in range(len(string_to_encrypt),len(string_to_encrypt) * 2):
            password += str(rand.randint(len(string_to_encrypt),len(string_to_encrypt) * 2))
        time.sleep(2)
        print("Password encrypted!")
        return password
    else:
        print("String length MUST BE greater than 0!")

init()
password = str(encryption())

passwordFile = open("password.txt","w+")
passwordFile.write(password)