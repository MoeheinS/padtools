import urllib.request
import ssl

#had to disable SSL cert checking because it expired
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def request(url):
	response_object = urllib.request.urlopen(url, context=ctx)
	with response_object as response:
		return response.read()
	return None
