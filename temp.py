from pySmartDL import SmartDL
url='https://gogo-cdn.com/download.php?url=aHR0cHM6LyAdrefsdsdfwerFrefdsfrersfdsrfer363435349URASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfjZG4xM3guY2xvdWQ5eHguY29tL3VzZXIxMzQyL2RlNDhhMGViNjBmZmUwMGQ4YmMyNTM5YTg3NWEzNjVkL0VQLjEuMzYwcC5tcDQ/dG9rZW49aXlIWEt3OGdBOHFXZnpDQWE1endPUSZleHBpcmVzPTE2MjQyODUwNTgmaWQ9OTc2MzI='
obj = SmartDL(url,'/home/sunbeam/Documents/rishi/Project/WebScraping_proj/naruto1.mp4')
obj.start()

import urllib
url1 = "https://gogo-cdn.com/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertsdf9jZG4xMC5jbG91ZDl4eC5jb20vdXNlcjEzNDIvMmFmYjcxMTZhZDM3MzRiNDY3ZTQ5YjIwNmViMzgwZWQvRVAuMi43MjBwLm1wND90b2tlbj11SmFubmxkT0lKazJZX0FtOXpPZl9BJmV4cGlyZXM9MTYyNDM3ODg0NyZpZD0xMDcyNDQ="
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

