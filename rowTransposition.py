'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


import math

global plain
global cipher
global chunks
chunks = {}
plain = ""
cipher = ""


class RowTransposition:

    def setKey(self, key):
        self.key = str(key)


    def encryption(self, plainText):
        global cipher, chunks
        self.plainText = plainText

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


    def decryption(self, cipherText):
        global plain, chunks
        self.cipherText = cipherText
        z = 0
        height = len(self.cipherText) / len(self.key)
        for x in range(0, len(self.cipherText), height):
            chunks[int(self.key[z])] = self.cipherText[x:x+height]
            z += 1

        for x in range(height):
            for y in range(len(self.key)):
                plain += chunks[y+1][x]

        return plain