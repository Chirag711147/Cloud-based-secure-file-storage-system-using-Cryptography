import time
from securefile import Encrypt
from securefile.keyset import RSA_KEY

rsa_public_key = RSA_KEY.public_key_genrate(18285, 57067)
rsa_private_key = RSA_KEY.private_key_genrate(6861, 57067)
chiper_shift = 3

enc = Encrypt('test.md', delimiter=':')
enc.open()

start_time = time.time()

enc.base64_encrypt()
encry=enc.rsa_encrypt(rsa_private_key, commit=True)
encryptedtext=""
encryptedtext=encryptedtext.join(encry)
enc.caesar_cipher(key_shift=chiper_shift, commit=True)

encode_time = time.time() - start_time
print("--- %s seconds ---" % str(encode_time))

enc.caesar_decipher(key_shift=chiper_shift, commit=True)
enc.rsa_decrypt(rsa_public_key, commit=True)
d1=enc.base64_decrypt(commit=True)
decrypted_message=""
decrypted_message=decrypted_message.join(d1)
decode_time = time.time() - start_time
print("--- %s seconds ---" % (decode_time))

div="\n-----------------------------------------------------------------------------------\n"
with open("outputRSA.txt", "a", encoding="utf8") as file:
    file.write("Stringlength=" + str(len(enc.get_text())) + div + "Encode time="+
            str(encode_time) + div+"Decode time="+ str(decode_time) + div + "Encrypted text="
             + str(encryptedtext) +div + "Decrypted message= "+str(decrypted_message) + div)
    file.close()

enc.close()
