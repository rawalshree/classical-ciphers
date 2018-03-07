'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


global plain
global cipher
global position
global Success
Success = False
position = {}
plain = ""
cipher = ""


class Monoalphabetic:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        global Success
        self.key = key
        if self.key.isalpha() and len(self.key) == 26:
            Success = True

            for x in range(26):
                position[chr(x+97)] = self.key[x]
            

    def encryption(self, plainText):
        global cipher, position, Success
        self.plainText = plainText
        
        if Success:
            for char in self.plainText:
                cipher += position[char]

            return cipher
        else:
            print("Invalid Key")
            return self.plainText
        
        
    def decryption(self, cipherText):
        global plain, position, Success
        self.cipherText = cipherText

        if Success:
            for char in self.cipherText:
                plain += position.keys()[position.values().index(char)]

            return plain
        else:
            print("Invalid Key")
            return self.cipherText