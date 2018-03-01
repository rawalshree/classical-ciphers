
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
            position[x+97] = self.key[x]
            
    def encryption(self, plainText):
        global cipher
        self.plainText = plainText
        
        return cipher
        
    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText

        return plain