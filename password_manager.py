from cryptography.fernet import Fernet



def write_key():

    key=Fernet.generate_key()
    with open("key.key","wb") as key_f:
        key_f.write(key)

def load_key():
    file = open("key.key","rb")
    kkey=file.read()
    file.close()
    return kkey



manage_pwd=input("Enter the master password: ")
ld_key=load_key() + manage_pwd.encode()
fer=Fernet(ld_key)

def add():
    name = input("Enter your account name: ")
    pwd=input("ENter your password: ")

    with open ("Password.txt","a") as f:
        f.write(name +"|" + fer.encrypt(pwd.encode()))

def view():
    with open ("Password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            usr,passw=data.split("|")
            print("User: ",usr, "password: ",passw)

while True:

    ch=input("You want to add a new password or to view an old one: Press 'q' to quit: ")
    
    if ch=="q":
        break
    if ch=='add':
        add()
    elif ch=='view':
        view()
    continue


    
    continue 