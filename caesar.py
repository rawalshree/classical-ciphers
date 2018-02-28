
global plain
global cipher
plain = ""
cipher = ""


class Caesar:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        self.key = key

    def encryption(self, plainText):
        global cipher
        self.plainText = plainText
        for char in self.plainText:
            if char.isalpha():
                char = chr(ord(char) + self.key)
                if ord(char) > ord('z'):
                    char = chr(ord(char) - 26)
                cipher += char
        return cipher
        
    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText
        for char in self.cipherText:
            if char.isalpha():
                char = chr(ord(char) - self.key)
                if ord(char) < ord('a'):
                    char = chr(ord(char) + 26)
                plain += char
        return plain