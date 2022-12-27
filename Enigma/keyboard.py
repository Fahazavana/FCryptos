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
