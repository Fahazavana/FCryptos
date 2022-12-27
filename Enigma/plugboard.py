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
