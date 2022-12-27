class Keyboard():
    """
    Input/outpout letter
    """

    def forward(self, letter):
        """
        Find the position of a given letter
        and convert to a signal()

        Letter --> Number
        """
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)

    def backward(self, signal):
        """
        Convert a signal to a letter

        Number --> Letter
        """
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]


class Plugboard:
    def __init__(self, pairs):
        # Swapped letter
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Default alphabet
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            # Sawapping letter
            # like the connection in the real enigma machine
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.right.find(B)
            self.left = self.left[:pos_A]+B+self.left[pos_A+1:]
            self.left = self.left[:pos_B]+A+self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)


class Rotors:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self,signal):
        letter = self.right[signal]
        return self.left.find(letter)
    
    def backward(self,signal):
        letter = self.left[signal]
        return self.right.find(letter)



class Reflector:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self,signal):
        letter = self.right[signal]
        return self.left.find(letter)





## REFLECTOR - ROTOR I - ROTOR II - ROTOR III - PLUGBOARD - KEYBOARD

if __name__ == "__main__":
    # Rotor settings
    # https://en.wikipedia.org/wiki/Enigma_rotor_details

    I = Rotors("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotors("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotors("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotors("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotors("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    Ref_A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
    Ref_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    Ref_C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
    

    KB = Keyboard()
    PB = Plugboard(['AB','GX','OM'])
    # Letter to Cypher

    letter = 'Q'
    # Transform to signal
    signal = KB.forward(letter)
    # Passing throug the Plugboard
    signal = PB.forward(signal)
    # Third Rotor
    signal = III.forward(signal) 
    print(signal)
    # second Rotor
    signal = II.forward(signal) 
    print(signal)
    # first Rotor
    signal = I.forward(signal) 
    print(signal)
    # REFLECTOR
    signal =  Ref_A.reflect(signal)
    print(signal)
    # first Rotor
    signal = I.backward(signal) 
    print(signal)
    # second Rotor
    signal = II.backward(signal) 
    print(signal)
    # Third Rotor
    signal = III.backward(signal) 
    print(signal)
    # Passing throug the Plugboard
    signal = PB.backward(signal)
    print(signal)
    #Lamp
    letter = KB.backward(signal)
    print(letter)
