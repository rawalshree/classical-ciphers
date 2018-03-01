
global plain
global cipher
plain = ""
cipher = ""


class Vigenre:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        self.key = int(key)

    def encryption(self, plainText):
        global cipher
        self.plainText = plainText

        for x in range(len(self.plainText)):
            if self.plainText[x].isalpha():
                char = chr(((ord(self.plainText[x]) + ord(self.key[x % len(self.key)]))) - 97)
                if ord(char) > ord('z'):
                    char = chr(ord(char) - 26)
                cipher += char
                    
        return cipher


    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText

        for x in range(len(self.plainText)):
            if self.plainText[x].isalpha():
                char = chr(((ord(self.cipherText[x]) - ord(self.key[x % len(self.key)]))) + 97)
                if ord(char) < ord('a'):
                    char = chr(ord(char) + 26)
                plain += char
        
        return plain
