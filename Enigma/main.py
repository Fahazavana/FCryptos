from keyboard import Keyboard
from plugboard import Plugboard
from rotors import Rotors
from reflector import Reflector
from enigma import Enigma

# REFLECTOR - ROTORS - PLUGBOARD - KEYBOARD
if __name__ == "__main__":
    # Rotor settings
    # https://en.wikipedia.org/wiki/Enigma_rotor_details

    # Rotors List
    I = Rotors("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotors("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotors("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotors("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotors("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    # Reflector list
    A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
    B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

    # Keayboard
    KB = Keyboard()

    # Plugboard
    PB = Plugboard(['AB', 'CD', 'EF'])

    # Define the enigma machine 
    ENIGMA_MACHINE = Enigma(B, IV, II, I, PB, KB)

    # Ring settings
    ENIGMA_MACHINE.set_rings("AAB")

    # Key setting (Initial position letter of each rotor)
    ENIGMA_MACHINE.set_key("CAT")

    message = "TESTING"
    ciphered = ""
    for m in message:
        ciphered += ENIGMA_MACHINE.encipher(m)
    print(ciphered)
