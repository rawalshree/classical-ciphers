'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''
#Sample Key = "universtabcdfghjklmopqwxyz tabcdfghjklmopqwxyzunivers fghjklmopqwxyzuniverstabcd"


from collections import OrderedDict
from itertools import islice, cycle
global plain
global cipher
global Success
global position1
global position2
global position3
global counter1
global counter2
global counter3
Success = False
counter1 = 0
counter2 = 0
counter3 = 0
position1 = {}
position2 = {}
position3 = {}
plain = ""
cipher = ""


class ThreeRotorEnigma:

    # A - Z ==> 65 - 90
    # a - z ==> 97 - 122

    def shift_dict(self, dct, shift):
        self.dct = dct
        self.shift = shift
        shift %= len(self.dct)
        return OrderedDict(
            (k, v)
            for k, v in zip(self.dct.keys(), islice(cycle(self.dct.values()), self.shift, None))
        )

    def setKey(self, key):
        global Success
        self.key = key
        self.key = " ".join(self.key.split())
        
        key1, key2, key3 = self.key.split(" ")

        if len(key1) == 26:
            for x in range(26):
                position1[chr(x+97)] = key1[x]
        
        if len(key2) == 26:
            for x in range(26):
                position2[chr(x+97)] = key2[x]

        if len(key3) == 26:
            for x in range(26):
                position3[chr(x+97)] = key3[x]
        
        if len(key1) + len(key2) + len(key3) == 78 and key1.isalpha() and key2.isalpha() and key3.isalpha():
            Success = True
            

    def encryption(self, plainText):
        global cipher, position1, position2, position3, counter1, counter2, counter3, Success
        self.plainText = plainText

        if Success:
            for char in self.plainText:
                cipher += position3[position2[position1[char]]]
                counter3 += 1
                position3 = self.shift_dict(position3, 1)
                if counter3 == 26:
                    counter2 += 1
                    position2 = self.shift_dict(position2, 1)
                    counter3 = 0
                if counter2 == 26:
                    counter1 += 1
                    position1 = self.shift_dict(position1, 1)
                    counter2 = 0
                if counter1 == 26:
                    counter1 = 0

            return cipher
        else:
            print("Invalid Key")
            return self.plainText
        
        
    def decryption(self, cipherText):
        global plain, position1, position2, position3, counter1, counter2, counter3, Success
        self.cipherText = cipherText

        if Success:
            for char in self.cipherText:
                z = position3.keys()[position3.values().index(char)]
                z = position2.keys()[position2.values().index(z)]
                plain += position1.keys()[position1.values().index(z)]
                counter3 += 1
                position3 = self.shift_dict(position3, 1)
                if counter3 == 26:
                    counter2 += 1
                    position2 = self.shift_dict(position2, 1)
                    counter3 = 0
                if counter2 == 26:
                    counter1 += 1
                    position1 = self.shift_dict(position1, 1)
                    counter2 = 0
                if counter1 == 26:
                    counter1 = 0

            return plain
        else:
            print("Invalid Key")
            return self.cipherText