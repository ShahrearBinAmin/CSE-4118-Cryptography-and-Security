keys=open('sub_key.txt','r')
keys=keys.readline()
map={}
for c in range(0,26):
    map[keys[c]]=chr(c+65)

cipher_text=open('sub_ciphertext.txt','r')
plain_text=open('plain_text.txt','w')

plaint=''
for line in cipher_text.readlines():
    print(line)
    for char in line:
        if(char in map.keys()):
            char=map[char]
            plaint+=char
            plain_text.write(char)
        else:
            plaint += char
            plain_text.write(char)

print(plaint)
plain_text.close()
