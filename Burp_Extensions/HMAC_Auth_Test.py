from datetime import datetime

import hashlib
import hmac
import base64


#Proof-of-concept to compare HMAC generation using known static attributes.
#Compare the result to expected header values.

#Change Key name if there is one. Always statically assigned.
Key = "KEYNAME"
#Change Secret/Key Value. Always statically assigned.
Secret = "S3cr3t-@p1-K3y"
Secret = bytes(Secret, 'utf-8')
#Statically assigned for testing. Change with 
urlpath = "https://test-api.com"
#Remove port from URL if present. Change if needed.
url = urlpath.replace(":443", "")

#Statically assigned for testing
method = "POST"

#Add content-type depending on request method used.
if method == "GET" or method == "DELETE":
    contentType = ""
else:
    contentType = "application/json"

#Statically assigned for testing
BodyStr = '''{
	"data"
	},
	"data2"
}'''

#If there is body content, generate a SHA256 sum of it. It not, leave it blank.
if BodyStr:
    BodyStr256 = hashlib.sha256(str(BodyStr).encode()).hexdigest()
else:
    BodyStr256 = str(BodyStr)

#Statically assigned timestamp for testing.    
timestamp = "2020-04-02T15:09:07.830Z"

#Generate the content string, encode it, and calculate HMAC value.
content = method + "\n" + contentType + "\n" + BodyStr256 + "\n" + timestamp + "\n" + url
content = bytes(content, 'utf-8')
_hmac = base64.b64encode(hmac.new(Secret, content, digestmod=hashlib.sha256).digest())

#Print content string and generated test headers.
print("content:" + str(content))
print
print("Authorization:" + Key + ":" + _hmac.decode("utf-8"))
print("Timestamp:" + timestamp)
