'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


import math

global plain
global cipher
global Success
Success = False
plain = ""
cipher = ""


class Railfence:

    def setKey(self, key):
        global Success
        try:
            self.key = int(key)
            if self.key > 0:
                Success = True
        except:
            pass


    def encryption(self, plainText):
        global cipher, Success
        self.plainText = plainText

        if Success:
            for x in range(self.key):
                for y in range(x, len(self.plainText), self.key):
                    cipher += self.plainText[y]

            return cipher
        else:
            print("Invalid Key")
            return self.plainText


    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText

        if Success:
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
        else:
            print("Invalid Key")
            return self.plainText