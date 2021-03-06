#BEAVERCRYPT
#MADE BY: ORANGEMAN9590 at GITHUB
#15, FEBRUARY, 2020

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
import termcolor
from termcolor import colored

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'main.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('clear')

if os.path.isfile('data.txt.enc'):
    while True:
        password = str(input("Enter password: "))
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("data.txt")   
            os.system('clear')
            print(colored(' ___                        ___               _   ', 'red'))
            print(colored('| _ ) ___ __ ___ _____ _ _ / __|_ _ _  _ _ __| |_ ', 'red'))
            print(colored("| _ \/ -_) _` \ V / -_) '_| (__| '_| || | '_ \  _|", 'red'))
            print(colored('|___/\___\__,_|\_/\___|_|  \___|_|  \_, | .__/\__|', 'red'))
            print(colored('                                    |__/|_|       ', 'red'))
            print(colored('           DEVELOPED BY: Orangeman9590         ', 'magenta')
            break

    while True:
        choice = int(input(
            "Press '1' to encrypt file.\nPress '2' to decrypt file.\nPress '3' to Encrypt all files in the directory.(REMOVES EVERYTHING)\nPress '4' to exit.\n"))
        clear()
        if choice == 1:
            enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            print("Encrypted")
        elif choice == 2:
            enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
            print("Decrypted")
        elif choice == 3:
            enc.encrypt_all_files()
            print("Encrypted")
        elif choice == 4:
            exit()
        else:
            print("Please select a valid option!")

else:
    while True:
        clear()
        print(colored(' ___                        ___               _   ', 'red'))
        print(colored('| _ ) ___ __ ___ _____ _ _ / __|_ _ _  _ _ __| |_ ', 'red'))
        print(colored("| _ \/ -_) _` \ V / -_) '_| (__| '_| || | '_ \  _|", 'red'))
        print(colored('|___/\___\__,_|\_/\___|_|  \___|_|  \_, | .__/\__|', 'red'))
        print(colored('                                    |__/|_|       ', 'red'))
        print(colored('           DEVELOPED BY: Orangeman9590         ', 'magenta')
        print("-----------------------------------------------------")
        password = str(input("Enter a password that will be used for decryption: "))
        repassword = str(input("Confirm password: "))
        if password == repassword:
            break
        else:
            print("Passwords Mismatched!")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    print("Restarting Program...")
    time.sleep(2)
    os.system('clear')
    os.system('python3 beaver.py')
