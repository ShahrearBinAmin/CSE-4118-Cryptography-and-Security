import binascii
plaintext='10010011001010011001010010000110101001010001010110100111010101010101011010010101011000111100110100111010110100101010110100101000101011101101011101011010'
key ='11100111010000011111000110100110110101010111010011010100001001100010000111111010000100011010100100011010101110111101111000001000110011001011111000110100'
decode=''
for i in range(len(plaintext)):
    out=int(plaintext[i]) ^ int(key[i])
    decode+=str(out)

print decode
print binascii.unhexlify('%x' % int(decode, 2))