class Enigma:
    """
    Main class of enigma 
    Using all class defined above to create the machine
    """

    def __init__(self, ref, r1, r2, r3, pb, kb):
        self.reflector = ref
        self.rotor1 = r1
        self.rotor2 = r2
        self.rotor3 = r3
        self.plugboard = pb
        self.keyboard = kb

    def set_rings(self,ring):
        ring = ring.upper()
        ring = [ ord(x)-65 for x in ring ]
        self.rotor1.set_ring(ring[0])
        self.rotor2.set_ring(ring[1])
        self.rotor3.set_ring(ring[2])


    def set_key(self,key):
        self.rotor1.rotate_to_letter(key[0])
        self.rotor2.rotate_to_letter(key[1])
        self.rotor3.rotate_to_letter(key[2])

        
    def encipher(self, letter):
        if (self.rotor3.left[0] == self.rotor3.notch) and (self.rotor2.left[0] == self.rotor2.notch):
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif (self.rotor2.left[0] == self.rotor2.notch):
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif (self.rotor3.left[0] == self.rotor3.notch):
            self.rotor2.rotate()
            self.rotor3.rotate()

        else:
            self.rotor3.rotate()


        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)
        signal = self.rotor3.forward(signal)
        signal = self.rotor2.forward(signal)
        signal = self.rotor1.forward(signal)
        signal = self.reflector.reflect(signal)
        signal = self.rotor1.backward(signal)
        signal = self.rotor2.backward(signal)
        signal = self.rotor3.backward(signal)
        signal = self.plugboard.backward(signal)
        return self.keyboard.backward(signal)
