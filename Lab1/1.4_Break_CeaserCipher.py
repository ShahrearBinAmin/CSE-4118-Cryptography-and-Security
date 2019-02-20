from collections import Counter
import matplotlib.pyplot as plt

probability={'a':.08167,'b':.01492,'c':.02782,'d':.04253,'e':.12702,'f':.02228,'g':.02015,
             'h':.06094,'i':.06966,'j':0.00153,'k':0.00772,'l':.04025,'m':.02406,'n':.06749,
             'o':.07507,'p':.01929,'q':0.00095,'r':.05987,'s':.06327,'t':.09056,'u':.02758,
             'v':0.00978,'w':.02360,'x':0.00150,'y':.01974,'z':0.00074}

def distance(key, encrypted_str):
    squared_dist=0
    encrypted_string=''
    for i in range(len(encrypted_str)):
        encrypted_string+=chr(((ord(encrypted_str[i])-ord('a'))-key)%26+97)
    count = Counter(encrypted_string)
    encrypted_string=list(encrypted_string)
    text_length=len(encrypted_string)
    #unique characters
    encrypted_string=set(encrypted_string)
    unique_chars=len(encrypted_string)

    for i in range(unique_chars):
        chars = encrypted_string.pop()
        squared_dist+= (text_length * probability[chars] - count[chars]) ** 2
    return squared_dist

def Mapping(encrypted_org1):
    encrypted_string = ''
    for i in range(len(encrypted_org1)):
        if ord(encrypted_org1[i]) >= 97 and ord(encrypted_org1[i]) <= 122:
            encrypted_string = encrypted_string + chr(((ord(encrypted_org1[i]) - ord('a')) - shift_key) % 26 + 97)
        else:
            encrypted_string += encrypted_org1[i]
    return encrypted_string


encrypted_file=open('ceaser_cipher.txt','r')
orginal_encrypted=encrypted_file.read().lower()
org_encrypted_cpy=orginal_encrypted
orginal_encrypted=list(orginal_encrypted)
stop_chars={' ', '.', ','}
orginal_encrypted = [element for element in orginal_encrypted if element not in stop_chars]

#relative_frequency histogram of the characters
orginal_encrypted.sort()
plt.hist(orginal_encrypted)
plt.xlabel('Character')
plt.ylabel('Count')
plt.show()

MIN=1000000000000000000
shift_key=0

for i in range(26):
    squared_distance=distance(i, orginal_encrypted)
    if(squared_distance<MIN):
        MIN=squared_distance
        shift_key=i
print('Key : ', shift_key)
print(org_encrypted_cpy)

encrypted_string=Mapping(org_encrypted_cpy)
print(encrypted_string)
file1=open('ceaser_dechiperd.txt','w')
file1.write(encrypted_string)
file1.close()
