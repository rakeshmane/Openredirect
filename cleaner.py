import json
import requests,sys,time,os
import urllib2,urllib
import urlparse
import warnings
from colorama import Fore, Back, Style



if len(sys.argv)<=2:
	print "Usage : python Open_Redirect_Scanner.py URLsListFile ProjectName"
	exit()


warnings.filterwarnings("ignore") # To hide the Warning Messages

f=open(sys.argv[1])
project_name=sys.argv[2]



with open('payload', 'r') as p:
    payloadsfromfile = p.readlines()

data = json.load(f)
f.close()
urlwithparameter=[]

def writeToFile(file_name,content): # Write result to file
	f_name=file_name+"_"+project_name+".txt"
	if os.path.exists(f_name):
		open(f_name,"a").write(content+"\n") # Append
	else:
		open(f_name,"w").write(content+"\n") # Write

def fetch(z,payload):
	try:
		response = requests.get(z, allow_redirects=False, verify=False) # SSL verification set to False bcz script won't work if SSL certification verification fails. 		
	except:
		print "Connection Issues"

		#Add logic of "Refresh" header 
	if "location" in response.headers: #Check location header in response
		if response.headers['location'].strip() == payload.strip():
			print Fore.BLUE+"Confirmed : "+Fore.RED+response.url+" : "+Fore.BLUE+response.headers['location'].strip()+Style.RESET_ALL
			writeToFile("confirmed",response.url+" : "+response.headers['location'].strip()) #  http://site?x=/\google.com : /\google.com [URL:Location_Header_Value]
		elif payload.strip() in response.headers['location'].strip():
			print payload.strip()+":"+response.headers['location'].strip()
			print Fore.BLUE+"Possible : "+Style.RESET_ALL+response.url+" : "+Fore.BLUE+response.headers['location'].strip()+Style.RESET_ALL
			writeToFile("possible",response.url+" : "+response.headers['location'].strip()) #  http://site?x=/\google.com : /\google.com [URL:Location_Header_Value]


global tmp,counter,why,why1
counter=0

tmp=""
## New code begins 
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
					fetch(finalurl+payload,payload)
				





	for payload in payloadsfromfile:
		if ("?" not in singleurl):
			z=singleurl+"/"+payload
		else:
			z=singleurl+"="+payload
		fetch(z,payload)




