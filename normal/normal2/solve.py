from base64 import b16decode, b64encode
from Crypto.Cipher import AES

ciphertext = '934d8706bed74cd6eea683c7be86b2eb32616562363039383965386433333531'
flag2 = b16decode(ciphertext[32:].upper())

key = [0x1B, 0x2E, 0x35, 0x46, 0x58, 0x6E, 0x72, 0x86,
       0x9B, 0xA7, 0xB5, 0xC8, 0xD9, 0xEF, 0xff, 0x0C]

aes = AES.new(bytes(key), AES.MODE_ECB)
to_decrypt = b16decode(ciphertext[:32].upper())

flag1 = aes.decrypt(to_decrypt)

flag = flag1 + flag2
print(flag.decode())