from Crypto.PublicKey import RSA
import random

key = open("key.txt", "r").read()
keypub = open("key.txt.pub", "r").read()
private_key = RSA.importKey(key)
public_key = RSA.importKey(keypub)
message = "hello world"
rand_num=random.randint(1,101)
c = public_key.encrypt(message, rand_num)[0]
print "Encrypted :",c.encode("hex")
p = private_key.decrypt(c)
print "Decrypted :",p