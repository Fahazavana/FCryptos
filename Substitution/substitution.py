"""
A simple Substitution cryptography methods
"""
SUBS = [
    ('A','A'),('B','Z'),('C','Y'),('D','X'),('E','E'),('F','W'),('G','V'),('H','T'),('I','I'),
    ('J','S'),('K','R'),('L','Q'),('M','P'),('N','N'),('O','O'),('P','M'),('Q','L'),('R','K'),
    ('S','J'),('T','H'),('U','U'),('V','G'),('W','F'),('X','D'),('Y','C'),('Z','B')
]

def clean(string):
    return string.replace(' ','')

def applySubstitution(message):
    m = ''
    for w in message:
        x = ord(w.lower())-97
        if 0<=x<=25:
            m += SUBS[x][1]
        else:
            m+=w
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
    if m == "2" :
        print("Decrypted message : ")
    else:
        print("Crypted message : ")
    print(applySubstitution(message))