from Crypto.Cipher import Blowfish
import binascii

def PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    appendage = chr(packingLength) * packingLength
    return string + appendage

def PandoraEncrypt(string):
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    packedString = PKCS5Padding(string)
    return c1.encrypt(packedString)



if __name__ == '__main__':
    s = 'This is blowfish algorithm testing'
    c = PandoraEncrypt(s)
    print(binascii.hexlify(c))
    