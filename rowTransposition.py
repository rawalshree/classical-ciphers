'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


import math

global plain
global cipher
global chunks
global Success
Success = False
chunks = {}
plain = ""
cipher = ""


class RowTransposition:

    def setKey(self, key):
        global Success
        self.key = str(key)
        if self.key > 0:
            Success = True


    def encryption(self, plainText):
        global cipher, chunks, Success
        self.plainText = plainText

        if Success:
            while len(self.plainText) % len(self.key) != 0:
                self.plainText += "*"

            for x in range(len(self.key)):
                y = x
                while y < len(self.plainText):
                    cipher += self.plainText[y]
                    y += len(self.key)
                chunks[int(self.key[x])] = cipher
                cipher = ""
            
            for x in range(len(self.key)):
                cipher += chunks[x+1]
            
            return cipher
        else:
            print("Invalid Key")
            return self.plainText


    def decryption(self, cipherText):
        global plain, chunks
        self.cipherText = cipherText

        if Success:
            z = 1
            height = len(self.cipherText) / len(self.key)
            for x in range(0, len(self.cipherText), height):
                chunks[z] = self.cipherText[x:x+height]
                z += 1

            for x in range(height):
                for y in range(len(self.key)):
                    plain += chunks[int(self.key[y])][x]
                

            return plain
        else:
            print("Invalid Key")
            return self.cipherText