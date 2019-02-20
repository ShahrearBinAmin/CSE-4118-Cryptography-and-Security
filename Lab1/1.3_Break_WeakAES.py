import codecs
from Crypto.Cipher import AES


encrypted_file=open('aes_weak_ciphertext.hex','r')
encrypted_file=encrypted_file.read()
print("Encrypted file : "+encrypted_file)
encrypted=codecs.decode(encrypted_file,'hex')

key=''
for i in range(31):
    key+=chr(0)

initialization_vec= ''
for i in range(16):
    initialization_vec+=chr(0)

for i in range(32):
    cipher = AES.new(key + chr(i), AES.MODE_CBC, initialization_vec)
    decrypted = cipher.decrypt(encrypted)
    print('Last 5 digit : ',i+1,' ',decrypted)

index=input('Enter index : ')
found_key="{0:#0{1}x}".format(int(index),66)
print(found_key)
file = open("Solution03.hex","w")
file.write(found_key)
file.close()
