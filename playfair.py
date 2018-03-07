'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


from collections import OrderedDict

global plain
global cipher
global postion
global Success
global Matrix
Success = False
Matrix = []
postion = {}
plain = ""
cipher = ""


class PlayFair:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122
    def setKey(self, key):
        global Matrix, Success
        self.key = key
        
        if self.key.isalpha():
            Success = True
            for x in range(97, 123, 1):
                if chr(x) != 'j':
                    self.key += chr(x)
            self.key = self.key.replace("j", "i")

            self.key = "".join(OrderedDict.fromkeys(self.key))
            Matrix = [[0 for x in range(5)] for y in range(5)]
            z = 0
            for x in range(5):
                for y in range(5):
                    Matrix[x][y] = self.key[z]
                    postion[self.key[z]] = (x,y)
                    z += 1


    def encryption(self, plainText):
        global cipher, Matrix, Success
        self.plainText = plainText
        if Success:
            self.plainText = plainText.replace("j", "i")
            self.plainText += "x"
            pair = []
            z = 0
            while z < len(self.plainText) - 1:
                if self.plainText[z] != self.plainText[z+1]:
                    pair += self.plainText[z] + self.plainText[z+1]
                    z += 2
                else:
                    pair += self.plainText[z] + "x"
                    z += 1

            for x in range(0, len(pair), 2):
                a = pair[x]
                b = pair[x+1]

                if postion[a][0] == postion[b][0]:
                    cipher += Matrix[postion[a][0]][(postion[a][1] + 1) % 5] + Matrix[postion[b][0]][(postion[b][1] + 1) % 5]

                elif postion[a][1] == postion[b][1]:
                    cipher += Matrix[(postion[a][0] + 1) % 5][postion[a][1]] + Matrix[(postion[b][0] + 1) % 5][postion[b][1]]

                else:
                    cipher += Matrix[postion[a][0]][postion[b][1]] + Matrix[postion[b][0]][postion[a][1]]
            
            return cipher
        else:
            print("Invalid Key")
            return self.plainText
            

    def decryption(self, cipherText):
        global plain, Matrix
        self.cipherText = cipherText
        if Success:
            self.cipherText = cipherText.replace("j", "i")
            self.cipherText += "x"
            pair = []
            z = 0
            while z < len(self.cipherText) - 1:
                if self.cipherText[z] != self.cipherText[z+1]:
                    pair += self.cipherText[z] + self.cipherText[z+1]
                    z += 2
                else:
                    pair += self.cipherText[z] + "x"
                    z += 1

            for x in range(0, len(pair), 2):
                a = pair[x]
                b = pair[x+1]

                if postion[a][0] == postion[b][0]:
                    plain += Matrix[postion[a][0]][(postion[a][1] + 4) % 5] + Matrix[postion[b][0]][(postion[b][1] + 4) % 5]

                elif postion[a][1] == postion[b][1]:
                    plain += Matrix[(postion[a][0] + 4) % 5][postion[a][1]] + Matrix[(postion[b][0] + 4) % 5][postion[b][1]]

                else:
                    plain += Matrix[postion[a][0]][postion[b][1]] + Matrix[postion[b][0]][postion[a][1]]
            
            return plain
        else:
            print("Invalid Key")
            return self.cipherText