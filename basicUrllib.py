import urllib
import urllib2

# response=urllib2.urlopen("http://www.google.com")
# print response.read()

# A better version
# request = urllib2.Request("http://www.google.com")
# response=urllib2.urlopen(request)
# print response.read()


#  Request: Post version

# values={"username:":"blahblah","password":"blahblah"}
# # coding the values(dictionary)
# data=urllib.urlencode(values)
# url="blahblah"
# request=urllib2.Request(url,data)
# response=urllib2.urlopen(request)
# print response.read()

# Request:Get version

values={"username:":"freddiesun95@gmail.com","password":"blahblahblah"}
data=urllib.urlencode(values)
url="https://www.google.com/"
geturl=url+"?"+data
request=urllib2.Request(geturl)
response=urllib2.urlopen(request)
print response.read()