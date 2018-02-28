import math

global plain
global cipher
plain = ""
cipher = ""

class Railfence:

    def setKey(self, key):
        self.key = key

    def encryption(self, plainText):
        global cipher
        self.plainText = plainText

        for x in range(self.key):
            for y in range(x, len(self.plainText), self.key):
                cipher += self.plainText[y]

        return cipher

    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText
        diff = len(self.cipherText) % self.key
        width = int(math.ceil(len(self.cipherText) / (self.key * 1.0)))

        for x in range(width):
            z = x
            while z < len(self.cipherText) and len(plain) < len(self.cipherText):
                if (z < width * diff) or diff == 0:
                    plain += self.cipherText[z]
                    z += width
                else:
                    plain += self.cipherText[z]
                    z += width - 1
            
        return plain