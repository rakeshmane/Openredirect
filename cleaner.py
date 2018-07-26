import json
import requests,sys,time,os
import urllib2,urllib
import urlparse

f=open('rakeshmane.com_ServerScripts_Links.json')

with open('payload', 'r') as p:
    payloadsfromfile = p.readlines()

data = json.load(f)
f.close()
urlwithparameter=[]
def fetch(z):
	print z
	response = requests.get(z, verify=False) # SSL verification set to False bcz script won't work if SSL certification verification fails. 		
	try:
		if response.history:
	                print "Request was redirected"
	                for resp in response.history:
	                    print "|"
	                    print resp.status_code, resp.url
	                    
	                print "Final destination:"
	                print "+"+"\x1b[6;30;42m"
	                print response.status_code, response.url
			print "\x1b[0m"
	      	else:
	                print "Request was not redirected"		         
  	except:
		print "connection error :("


global tmp,counter,why,why1
counter=0

tmp=""
## New code bigins 
urllist=[]
for allurl in data:
	url=data[allurl]
	for parameter in url:
		if ("&" not in parameter):
			single_parameter=parameter.split('=')
			singleurl=allurl+single_parameter[0]
			
		else:
			multiple_parameter=parameter
			parsed = urlparse.urlparse(multiple_parameter)
			params = urlparse.parse_qsl(parsed.query)
			Parameter=[]
			Values=[]
			multipleparamater=[]
			for x,y in params:
				Parameter.append(x)
				Values.append(y)
			counter=0
			for i in Parameter:
				tmp=""
				tmp1=""
				for ii in range(0,len(Parameter)):
					if(ii == counter):
						tmp1="&"+Parameter[ii]+"="
					else:
						tmp=tmp+"&"+Parameter[ii]+"="+Values[ii]
	     			counter=counter+1	
				tmp=tmp	+tmp1
				finalurl= allurl+"?"+tmp
				for payload in payloadsfromfile:
					fetch(finalurl+payload)
				





	for payload in payloadsfromfile:
		if ("?" not in singleurl):
			z=singleurl+"/"+payload
		else:
			z=singleurl+"="+payload
		fetch(z)




