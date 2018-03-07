'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


global plain
global cipher
global Success
Success = False
plain = ""
cipher = ""


class Caesar:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
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
            for char in self.plainText:
                if char.isalpha():
                    char = chr(ord(char) + self.key)
                    if ord(char) > ord('z'):
                        char = chr(ord(char) - 26)
                    cipher += char
            return cipher
        else:
            print("Invalid Key")
            return self.plainText
        
        
    def decryption(self, cipherText):
        global plain, Success
        self.cipherText = cipherText
        if Success:
            for char in self.cipherText:
                if char.isalpha():
                    char = chr(ord(char) - self.key)
                    if ord(char) < ord('a'):
                        char = chr(ord(char) + 26)
                    plain += char
            return plain
        else:
            print("Invalid Key")
            return self.cipherText
        