import urllib
from pymd5 import md5, padding

file=open('3.3_query.txt','r')
query=file.read()

append_file=open('3.3_command3.txt')
append_cmd=append_file.read()

orgHash = query[query.find("=")+1:query.find("&")]
message = query[query.find("&") + 1:]

print "Current hash: "+orgHash
print "Message : " + message

secret_key_length=8
message_length = len(message) + secret_key_length
bitNumber = (message_length + len(padding(message_length*8)))*8

md5_obj = md5(state=orgHash.decode("hex"), count=bitNumber)
md5_obj.update(append_cmd)

changedHash = md5_obj.hexdigest()
padding = urllib.quote(padding(message_length*8))
print "Padding : "+padding
print "New hash : "+changedHash
message = message + padding + append_cmd
query = "token=" + changedHash +"&" + message
print "Changed query : ",query

open('solution33.txt','w').write(query)