'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


global plain
global cipher
global position
position = {}
plain = ""
cipher = ""


class Monoalphabetic:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        self.key = key

        for x in range(26):
            position[chr(x+97)] = self.key[x]
            

    def encryption(self, plainText):
        global cipher, position
        self.plainText = plainText

        for char in self.plainText:
            cipher += position[char]

        return cipher
        
        
    def decryption(self, cipherText):
        global plain, position
        self.cipherText = cipherText

        for char in self.cipherText:
            plain += position.keys()[position.values().index(char)]

        return plain