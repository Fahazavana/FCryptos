# A per block cryptography
# If the length of the key is
# shorter than the message


# This one is good if we choose
# A key with ths same length of the
# Message, and each key is used at most
# one time only (one time pad)


def clean(string):
    return string.replace(' ', '')


def Vingenere(message, key, task):
    """
    Vingenere crypting function
    """
    # Transforming the key to number in Z/26
    # And + if encryption, - if decryption
    K = [task * (ord(l) - 97) for l in key]
    # Length of the key
    k = len(K)
    # Initialize the crypted message
    m = ''
    i = 0
    for l in message:
        # Get a Z/26 representation of each letter of the message
        x = ord(l.lower()) - 97
        # Check if it is raly in Z/26
        if 0 <= x <= 25:
            # Encrypt/Decrypting each letter
            x = (x + K[i]) % 26
        # Go back to Letter
        m += chr(x + 97)
        # Block incremetation
        i = (i + 1) % k 
    # return the message
    return m


if __name__ == "__main__":
    m = ""
    while (m != "1") and (m != "2"):
        print("choose one option :")
        print("1-Encrypt a mesage.")
        print("2-Decrypt a message.")
        m = input("> ")
        m = clean(m)

    message = input("\nEnter your message : ")
    key = input('Enter your key : ')
    if m == "2":
        task = -1
        print("Decrypted message : ")
    else:
        print("Crypted message : ")
        task = 1
    print(Vingenere(message, key, task))
