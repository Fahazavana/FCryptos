class Rotors:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def show(self):
        print(self.left)
        print(self.right)
        print('')

    # Rotating the rotors
    def rotate(self):
        self.left = self.left[1:]+self.left[0]
        self.right = self.right[1:]+self.right[0]
        # self.show()

    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.left = self.left[n:]+self.left[0:n]
        self.right = self.right[n:]+self.right[0:n]

    def set_ring(self, pos): 
        self.left = self.left[-pos:]+self.left[:-pos]
        self.right = self.right[-pos:]+self.right[:-pos] 

        index_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(index_notch - pos) % 26]
