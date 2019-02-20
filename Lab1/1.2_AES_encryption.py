from Crypto.Cipher import AES
import codecs


key_file=open('aes_key.hex','r')
key_file=key_file.read()
print("Key : "+key_file)
key=codecs.decode(key_file,'hex')

iv_file=open('aes_iv.hex','r')
iv_file=iv_file.read()
print("IV : "+iv_file)
iv=codecs.decode(iv_file,'hex')

encrypted_file=open('aes_ciphertext.hex','r')
encrypted_file=encrypted_file.read()
print("Encrypted file : "+encrypted_file)
encrypted=codecs.decode(encrypted_file,'hex')

cipher=AES.new(key,AES.MODE_CBC,iv)
decrypted=cipher.decrypt(encrypted)

print(decrypted)