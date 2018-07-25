import json
import requests,sys,time,os
import urllib2,urllib

f=open('dohabank.qa_Others_Links.json')

with open('temppayload.txt', 'r') as p:
    payloadsfromfile = p.readlines()

data = json.load(f)
f.close()

urlwithparameter=[]


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
			##print multiple_parameter
					


	for payload in payloadsfromfile:
		if ("?" not in singleurl):
			z=r""+singleurl+"/"+payload
		else:
			z=r""+singleurl+"="+payload
		print r""+z

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



	




