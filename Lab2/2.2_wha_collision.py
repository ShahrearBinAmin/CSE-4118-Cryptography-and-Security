from itertools import permutations
def swap(string,index1,index2):
    string=list(string)
    temp=string[index1]
    string[index1]=string[index2]
    string[index2]=temp
    return ''.join(string)

def WHA(inputSting):
    Mask=0x3FFFFFFF
    outHash=0
    for byte in inputSting:
        byte=ord(byte)
        intermediate_value = ((byte ^ 0xCC) <<24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outHash = (outHash & Mask) + (intermediate_value & Mask)
    return outHash


file=open('3.2_input_string.txt','r')
file_string=file.read()
print file_string
#perms = [''.join(p) for p in permutations("Hello world!")]
print hex(WHA(file_string)),"\n"

#permutation of this string will generate same hash value
print "Hash Collision : "
output_file=open('solution32.txt','w')
file_string=swap(file_string,0,1)
print file_string
print hex(WHA(file_string)),"\n"
output_file.write(file_string)
output_file.close()

output_file=open('solution32.txt','a')
file_string=swap(file_string,0,2)
print file_string
print hex(WHA(file_string)),"\n"
output_file.write('\n'+file_string)
output_file.close()
