import urllib
import urllib2

# response=urllib2.urlopen("http://www.google.com")
# print response.read()

# A better version
request = urllib2.Request("http://www.google.com")
response=urllib2.urlopen(request)
print response.read()


