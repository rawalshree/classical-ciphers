'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Date - 28th February 2018
'''


from caesar import *
#from hillCipher import *
from rowTransposition import *
from railfence import *
from vigenre import *
from playfair import *
from monoalphabetic import *
import sys

cc = Caesar()
rt = RowTransposition()
rf = Railfence()
vg = Vigenre()
pf = PlayFair()
mc = Monoalphabetic()
#hc = HillCipher()
#tre = ThreeRotorEnigma()



def cipher(cipher_name, secret_key, enc_dec, input_file, output_file):
    intext = ""
    outtext = ""
    
    print("The cipher name is :", cipher_name)
    print("The secret key  is :", secret_key)
    print("The operation is :", enc_dec)
    print("The input file is :", input_file)
    print("The output file is :", output_file)

    options = {"CES" : (cc.setKey, {"ENC" : cc.encryption, "DEC" : cc.decryption}), 
               "PLF" : (pf.setKey, {"ENC" : pf.encryption, "DEC" : pf.decryption}),
               "RFC" : (rf.setKey, {"ENC" : rf.encryption, "DEC" : rf.decryption}),
               "VIG" : (vg.setKey, {"ENC" : vg.encryption, "DEC" : vg.decryption}),
               "RTS" : (rt.setKey, {"ENC" : rt.encryption, "DEC" : rt.decryption}),
               "MAC" : (mc.setKey, {"ENC" : mc.encryption, "DEC" : mc.decryption})}

    file = open(input_file, "r")
    for line in file:
        intext += line
    file.close()

    options[cipher_name][0](secret_key)
    outtext = options[cipher_name][1][enc_dec](intext)
    
    file = open(output_file, "w+")
    file.write(outtext)
    file.close


if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    c = str(sys.argv[3])
    d = str(sys.argv[4])
    e = str(sys.argv[5])
    cipher(a, b, c, d, e)
