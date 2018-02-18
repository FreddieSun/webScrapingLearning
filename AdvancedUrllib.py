import urllib
import urllib2

url="http://www.zhihu.com/login"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values={'username':'卷米','password':'blahblah'}
headers={'User-agent':user_agent}
data=urllib.urlencode(values)
request=urllib2.Request(url,data,headers)
response=urllib2.urlopen(request)
page=response.read()

# add the header so that the website will accept your request

#