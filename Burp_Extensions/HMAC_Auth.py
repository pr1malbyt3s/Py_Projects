from burp import IBurpExtender
from burp import ISessionHandlingAction
from burp import IParameter
from java.io import PrintWriter
from datetime import datetime

import hashlib
import hmac
import base64

#Burp extension to generate HMAC header values for API testing.
#References: https://github.com/pentestpartners/snippets/blob/master/hmac.py

class BurpExtender(IBurpExtender, ISessionHandlingAction):
	#
	# implement IBurpExtender
	#
	def registerExtenderCallbacks(self, callbacks):
		stdout = PrintWriter(callbacks.getStdout(), True)
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.setExtensionName("HMAC Header")
		stdout.println("HMAC Header Registered OK")
		callbacks.registerSessionHandlingAction(self)
		stdout.println("Session handling started")
		return
	 
	def getActionName(self):
		return "HMAC Header"
	 
	def performAction(self, currentRequest, macroItems):
		#Update the Key name.
		Key = "KEYNAME"
    #Update the Key value.
    Secret = "S3cr3t-@p1-K3y"
    Secret = Secret.encode('utf-8')

		stdout = PrintWriter(self._callbacks.getStdout(), True)
		requestInfo = self._helpers.analyzeRequest(currentRequest)
		
		#Get URL object and convert it to string.
		urlpath = requestInfo.getUrl()
                u = str(urlpath)
                #Remove the port number from the URL. Adjust as needed.
                url = u.replace(":443", "")

                #Get request method.
                method = requestInfo.getMethod()

                #Set contentType (Content-Type) value depending on method.
                if method == "GET" or method == "DELETE":
                    contentType = ""
                else:
                    contentType = "application/json"
				
		#Get body and perform SHA256 sum if not empty.
		BodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]
		BodyStr = self._helpers.bytesToString(BodyBytes)
                if BodyStr:
                    BodyStr256 = hashlib.sha256(BodyStr.encode()).hexdigest()
                else:
                    BodyStr256 = BodyStr

		#Get time and convert it to specified format.
		timestamp = datetime.utcnow()
                timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' 
		 
		#Generate the content string using specified format.
		content = method + "\n" + contentType + "\n" + BodyStr256 + "\n" + timestamp + "\n" + url
		#Printed to Burp UI debugging.
                stdout.println(content)
                #Encode the body string.
                content = content.encode('utf-8')
		#Calculate the HMAC value.
                _hmac = base64.b64encode(hmac.new(Secret, content, digestmod=hashlib.sha256).digest())
		#Printed to Burp UI for debugging.
                stdout.println(_hmac)
		
		#Generate headers.
		headers = requestInfo.getHeaders()
                hmacauthheader = "Authorization:" + Key + ":" + _hmac.decode("utf-8")
                hmactimeheader = "Timestamp:" + timestamp
		headers.add(hmacauthheader)
                headers.add(hmactimeheader)

		#Build new HTTP message with the new HMAC headers.
		message = self._helpers.buildHttpMessage(headers, BodyStr)
		
		#Update request headers and send request.
		currentRequest.setRequest(message)
		return
