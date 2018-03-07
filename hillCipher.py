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


class HillCipher:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        global Success
        self.key = key
        if len(self.key) == 4 and self.key.isalpha():
            Success = True

    def encryption(self, plainText):
        global cipher, Success
        self.plainText = plainText

        if Success:
            if len(self.plainText) % 2 != 0:
                self.plainText += 'x'
            
            a = ord(self.key[0]) - 97
            b = ord(self.key[1]) - 97
            c = ord(self.key[2]) - 97
            d = ord(self.key[3]) - 97

            for x in range(0, len(self.plainText), 2):
                p1 = ord(self.plainText[x]) - 97
                p2 = ord(self.plainText[x+1]) - 97
                
                char1 = (a * p1 + b * p2) % 26 + 97
                char2 = (c * p1 + d * p2) % 26 + 97

                cipher += chr(char1) + chr(char2)
            
            return cipher
        else:
            print("Invalid Key")
            return self.plainText


    def decryption(self, cipherText):
        global plain, Success
        self.cipherText = cipherText

        if Success:
            a = ord(self.key[0]) - 97
            b = ord(self.key[1]) - 97
            c = ord(self.key[2]) - 97
            d = ord(self.key[3]) - 97

            deter = (a*d - b*c) % 26

            for x in range(1,26):
                if x * deter % 26 == 1:
                    midt = x

            temp = a
            a = d * midt % 26
            d = temp * midt % 26
            b = (-b % 26) * midt % 26
            c = (-c % 26) * midt % 26

            for x in range(0, len(self.cipherText), 2):
                p1 = ord(self.cipherText[x]) - 97
                p2 = ord(self.cipherText[x+1]) - 97
                
                char1 = (a * p1 + b * p2) % 26 + 97
                char2 = (c * p1 + d * p2) % 26 + 97

                plain += chr(char1) + chr(char2)

            return plain
        else:
            print("Invalid Key")
            return self.cipherText