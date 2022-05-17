import time
from securefile import Encrypt
from securefile.keyset import AES_KEY

aes_key = AES_KEY.genrate('900102045505060704090a1b0c0d0e0f')
chiper_shift = 3

enc = Encrypt('test.md', delimiter=':')
enc.open()

start_time = time.time()

enc.base64_encrypt()
encry=enc.aes_encrypt(aes_key, commit=True)
encryptedtext=""
encryptedtext=encryptedtext.join(encry)
enc.caesar_cipher(key_shift=chiper_shift, commit=True)

encode_time = time.time() - start_time
print("--- %s seconds ---" % str(encode_time))

enc.caesar_decipher(key_shift=chiper_shift, commit=True)
enc.aes_decrypt(aes_key, commit=True)
d1=enc.base64_decrypt(commit=True)
decrypted_message=""
decrypted_message=decrypted_message.join(d1)
decode_time = time.time() - start_time
print("--- %s seconds ---" % (decode_time))

div="\n-----------------------------------------------------------------------------------\n"
with open("outputAES.txt", "a", encoding="utf8") as file:
    file.write("Stringlength=" + str(len(enc.get_text())) + div + "Encode time="+
            str(encode_time) + div+"Decode time="+ str(decode_time) + div + "Encrypted text=" 
            + str(encryptedtext) +div + "Decrypted message= "+str(decrypted_message) + div)
    file.close()

enc.close()
