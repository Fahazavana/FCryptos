def clean(string):
    return string.replace(' ','')


def cesar(x,k):
    """
    A simple linear translation in Z/26Z
    To crypt and decrypt
    Using the cesar method.
    """
    return (x+k)%26

def applyCesar(txt,key):
    """
    Applying cesar methd to encrypt/decrypt a message provided
    By the user
    """
    m = ''
    for t in txt :
        if t!=' ':
            x = cesar(ord(t.lower())-97, key)
            m += chr(x+97)
        else :
            m +=t
    return m



if __name__ == "__main__":
    m = ""
    while (m!="1") and (m!="2") :
        print("choose one option :")
        print("1-Encrypt a mesage.")
        print("2-Decrypt a message.")
        m = input("> ")
        m = clean(m)

    message = input("\nEnter your message : ") 
    key  = input("Enter your key : ")
    try:
        key = int(key)
    except :
        print("key must be an int not a {}".format(type(key)))
    else:
        if m == "2" :
            key = -key
            print("Decrypted message : ")
        else:
            print("Crypted message : ")
        print(applyCesar(message, key))
    finally:
        print('Ending the program')