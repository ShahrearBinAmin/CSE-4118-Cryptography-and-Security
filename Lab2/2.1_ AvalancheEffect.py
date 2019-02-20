import hashlib

inputFile1=open('3.1_input_string.txt','r')
inputFile1=inputFile1.read()

inputFile2=open('3.1_perturbed_string.txt','r')
inputFile2=inputFile2.read()

hex1=hashlib.sha256(inputFile1).hexdigest()
hex2=hashlib.sha256(inputFile2).hexdigest()

scale=16
num_of_bits=256

binary1=bin(int(hex1,scale))[2:].zfill(num_of_bits)
binary2=bin(int(hex2,scale))[2:].zfill(num_of_bits)

cnt=0
for i in range(num_of_bits):
    if binary1[i]!=binary2[i]:
        cnt=cnt+1


print "Hammming Distance : (int)",cnt,"  ,(hex) : ",hex(cnt)

hexFile=open('solution31.hex','w')
hexFile.write(hex(cnt))

