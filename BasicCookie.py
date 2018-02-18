#!/usr/bin/python
#coding:utf-8


# opener介绍： 一个urllib2.OpenerDirector实例， urlopen是一个特殊的opener
# 使用cookie的时候必须使用更一般的opneer来实现对cookie的设置

# Cookielib提供了可存储的cookie对象，
# 它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

import urllib2
import urllib
import cookielib

# # 一个cookiejar对象来存储cookie
# cookie=cookielib.CookieJar()
# # 创建cookieprocessor
# handler=urllib2.HTTPCookieProcessor(cookie)
#
# # 通过handler构建opener
# opener=urllib2.build_opener(handler)
#
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value
#
#
# # 如果想把cookie存到文件里呢
# filename='cookie.txt'
# # MozillaCookieJar对象保存Cookie
# cookie=cookielib.MozillaCookieJar(filename)
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener=urllib2.build_opener(handler)
# response=opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)
#
# # ignore_discard:save even cookies set to be discarded
# # ignore_expires:save even cookies that have expiredThe file is overwritten if it already exists


# obtain the cookie from the file

cookie1=cookielib.MozillaCookieJar()
cookie1.load('cookie.txt',ignore_expires=True,ignore_discard=True)
# 创建请求的request
req1=urllib2.Request("http://www.baidu.com")
opener1=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie1))
response1=opener1.open(req1)
print response1.read()