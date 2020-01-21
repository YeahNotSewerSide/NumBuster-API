# NumBuster-API
# So.. I fully reversed NumBuster app for android, and rewrited all requests for numbusters api in python.

# For working with that api you need access_token, there are 2 ways of getting it

# First way(PLS USE THAT):
  	Download NumBuster!_6.0.6.apk - I hope you can find it by yourself
	
	Download Genymotion and install Google Pixel 7.1 - API 25 in Genymotion  (Thats the easiest step, so...)
	
  	Download And Install https://github.com/MobSF/Mobile-Security-Framework-MobSF  (Thats not easy, but I believe in you)
	
  	Start emulator in Genymotion and start MobSF, open MobSF in your browser http://127.0.0.1:8000 (try that)
	
  	Drop NumBuster!_6.0.6.apk to MobSF in your browser
	
  	Go to DYNAMIC ANALYZER and press Start Dynamic Analysis
	
  	Then press button start instrumentation and go to emulator, wait for numbuster to load.
	
  	Then register new account and check any number in app(Numbuster) / or use alreay created account, for that just register new account for the same phone number, bdw you can use free online numbers, but tss....
	
  	After that, go to MobSF and press button Generate Report
	
  	In MobSF press StartHTTPTools find something like that https://api.numbuster.com/
	
  	In the https://api.numbuster.com/ menu look for that v6/old/search/ and in the parameters you will find your access_token
  
# Second way:
  	I have implemented all api requests in that api, so just find functions for registration use them and maybe you will get        access_token, but really, use first way. There is little help: most of functions for registration start with v6_auth, Good Luck!
  
  
# Now lets talk about api:
	Main api file with all api functions is NumbusterAPI.py, in file signatures.py functions for creating signaturs for different requests.
	
	And yes, user has only 30 free requests per day,
	BUT with that function: v6_old_phone you have unlimited free requests.
