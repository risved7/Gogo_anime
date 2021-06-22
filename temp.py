from pySmartDL import SmartDL
url='https://gogo-cdn.com/download.php?url=aHR0cHM6LyAdrefsdsdfwerFrefdsfrersfdsrfer363435349URASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfjZG4xM3guY2xvdWQ5eHguY29tL3VzZXIxMzQyL2RlNDhhMGViNjBmZmUwMGQ4YmMyNTM5YTg3NWEzNjVkL0VQLjEuMzYwcC5tcDQ/dG9rZW49aXlIWEt3OGdBOHFXZnpDQWE1endPUSZleHBpcmVzPTE2MjQyODUwNTgmaWQ9OTc2MzI='
obj = SmartDL(url,'/home/sunbeam/Documents/rishi/Project/WebScraping_proj/naruto1.mp4')
obj.start()

import urllib
url1 = "http://www.google.com/translate_a/t?client=t&sl=zh-CN&tl=en&q=%E7%94%B7%E5%AD%A9"
# request = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
request = urllib.request.Request(url1,headers=headers)
data = urllib.request.urlopen(request).read()

