# NumBuster API
# So.. I fully reversed NumBuster app for android, and rewrited all requests for numbusters api in python.

# For working with that api you need access_token, there are 2 ways of getting it (look at second way, don't spend your time on first way)

# First way(Not so easy):
  	Download NumBuster!_6.3.3.apk - I hope you can find it by yourself
	
	Download Genymotion and install Google Pixel 7.1 - API 25 in Genymotion  (Thats the easiest step, so...)
	
  	Download And Install https://github.com/MobSF/Mobile-Security-Framework-MobSF  (Thats not easy, but I believe in you)
	
  	Start emulator in Genymotion and start MobSF, open MobSF in your browser http://127.0.0.1:8000 (try that)
	
  	Drop NumBuster!_6.3.3.apk to MobSF in your browser
	
  	Go to DYNAMIC ANALYZER and press Start Dynamic Analysis
	
  	Then press button start instrumentation and go to emulator, wait for numbuster to load.
	
  	Then register new account and check any number in app(Numbuster) / or use alreay created account, for that just register 
	new account for the same phone number, bdw you can use free online numbers, but tss....
	
  	After that, go to MobSF and press button Generate Report
	
  	In MobSF press StartHTTPTools find something like that http://apikz2.nmb.st/api
	
  	In the http://apikz2.nmb.st/api menu look for that v6/old/search/ and in the parameters you will find your 
	access_token
  
# Second way (Why that's not the First way? BECAUSE):
  	So, First of all call function request_sms_code() with number for account
	Second, wait for sms, then call send_sms_code(phonenumber,code), 
	where phonenumber is phonenumber and, you won't believe, code is code,
	after that api will get access_token Numbuster.access_token and you'l
	be able to use all functionality of api. DON'T FORGET TO SAVE ACCESS_TOKEN,
	I won't do it for you, I'm not your mom or something...
  
# Now lets talk about api:
	Main api file with all api functions is NumbusterAPI.py, in file signatures.py functions for creating signaturs for 
	different requests.
	
	And yes, user has only 30 free requests per day for that function: v6_old_search,
	BUT with that function: v6_old_phone you have unlimited free requests.
