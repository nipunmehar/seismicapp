from lora.crypto import loramac_decrypt
import base64

x = (base64.b64decode('QESufgGAAAABizI7/Kupf6U='))
payload = x
key = '283EFC8ED5A378712420CE8568A461D3'
sequence_counter = 2
dev_addr = '017EAE44'
print(loramac_decrypt(payload, sequence_counter, key, dev_addr))


#283EFC8ED5A378712420CE8568A461D3
#593AE59422E01E88ED8FF9584B632C89 
#514553756667474141414142697a49372f4b75706636553d
#514553756667474141414142697a49372f4b75706636553d

#QESufgGAAAABizI7/Kupf6U=


#247, 28, 213, 236, 58, 52, 99, 66, 128, 157, 71, 44, 18, 145, 99, 223, 147, 159, 88, 182, 186, 204, 168, 255


