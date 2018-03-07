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


class Vigenre:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        global Success
        self.key = key

        if self.key.isalpha():
            Success = True

    def encryption(self, plainText):
        global cipher
        self.plainText = plainText

        if Success:
            for x in range(len(self.plainText)):
                if self.plainText[x].isalpha():
                    char = chr(((ord(self.plainText[x]) + ord(self.key[x % len(self.key)]))) - 97)
                    if ord(char) > ord('z'):
                        char = chr(ord(char) - 26)
                    cipher += char
                        
            return cipher
        else:
            print("Invalid Key")
            return self.plainText


    def decryption(self, cipherText):
        global plain
        self.cipherText = cipherText

        if Success:
            for x in range(len(self.cipherText)):
                if self.cipherText[x].isalpha():
                    char = chr(((ord(self.cipherText[x]) - ord(self.key[x % len(self.key)]))) + 97)
                    if ord(char) < ord('a'):
                        char = chr(ord(char) + 26)
                    plain += char
            
            return plain
        else:
            print("Invalid Key")
            return self.cipherText
