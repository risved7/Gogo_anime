
print('''
  ___          _                     ______                          _             _             
 / _ \        (_)                    |  _  \                        | |           | |            
/ /_\ \ _ __   _  _ __ ___    ___    | | | |  ___  __      __ _ __  | |  ___    __| |  ___  _ __ 
|  _  || '_ \ | || '_ ` _ \  / _ \   | | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _ \| '__|
| | | || | | || || | | | | ||  __/   | |/ / | (_) | \ V  V / | | | || || (_) || (_| ||  __/| |   
\_| |_/|_| |_||_||_| |_| |_| \___|   |___/   \___/   \_/\_/  |_| |_||_| \___/  \__,_| \___||_|   

    ## Programmed By :
\u001b[31m.______      \u001b[32m __ \u001b[33m      _______.\u001b[34m __    __  \u001b[35m __  
\u001b[31m|   _  \     \u001b[32m|  |\u001b[33m     /       |\u001b[34m|  |  |  | \u001b[35m|  | 
\u001b[31m|  |_)  |    \u001b[32m|  |\u001b[33m    |   (----`\u001b[34m|  |__|  | \u001b[35m|  | 
\u001b[31m|      /     \u001b[32m|  |\u001b[33m     \   \    \u001b[34m|   __   | \u001b[35m|  | 
\u001b[31m|  |\  \----.\u001b[32m|  |\u001b[33m .----)   |   \u001b[34m|  |  |  | \u001b[35m|  | 
\u001b[31m| _| `._____|\u001b[32m|__|\u001b[33m |_______/    \u001b[34m|__|  |__| \u001b[35m|__| 
\u001b[30m
''')

# from builtins import print

import requests
from pySmartDL import SmartDL
import sys
import os
import re
from clint.textui import progress
from bs4 import BeautifulSoup
def download(url,dest):
    obj=SmartDL(url, dest)
    obj.start()
    if obj.isSuccessful():
        print(f"\tDownloaded file to : {obj.get_dest()}")
        print(f"\tDownload task took : {obj.get_dl_time(human=True)}")
        print(f"\tDownload task size : {obj.get_dl_size(human=True)}")
    return
# ex = "https://www1.gogoanime.ai/boruto-naruto-next-generations-episode-1" [ episode 1-200 ]
qualities = ['HDP','360P','480P','720P','1080P']
q_rev = qualities[::-1]
# u=input("Enter URL of first episode> " )
# u=u.replace(" ","")
# u="https://www1.gogoanime.ai/death-note-episode-1"
# u="https://www1.gogoanime.ai/naruto-shippuuden-dub-episode-1"
u="https://www1.gogoanime.ai/hige-wo-soru-soshite-joshikousei-wo-hirou-episode-1"
# u="https://www1.gogoanime.ai/boruto-naruto-next-generations-episode-1"
url=u[:-1]
try:
    rq=requests.get(url)
    if rq.status_code == 200:
        # f=input("Enter episode to start with > ")
        # l=input("Enter episode to end with > ")
        # quality = input(f"Choose the quality > \n\t1:'HDP'\n\t2:'360P'\n\t3:'480P'\n\t4:'720P'\n\t5:'1080P'] \n\u001b[35m Enter the respective no for quality > ")
        # print("\u001b[31mNote the entered quality will be as enterd or lower if not avilable at server!")
        # n=input("\u001b[30mEnter name to be saved as > ")
        # d=input("Enter full path to destination folder > ")
        # s=input("Shut Down when downloaded?(y/n) > ")
        f="1"
        l="30"
        quality="2"
        n="joshikousei_"
        d="/home/sunbeam/Documents/rishi/Project/WebScraping_proj/death_note"
        s="n"

except:
    print ("Wrong URL biro")
    sys.exit()
while quality != "1":
    print("\u001b[31mSorry temporary limited to HD quality only pls select quality='1' !\u001b[30m")
    quality = input(f"Choose the quality > \n\t1:'HDP'\n\t2:'360P'\n\t3:'480P'\n\t4:'720P'\n\t5:'1080P'] \n\u001b[35m Enter the respective no for quality >\u001b[31m ")
for i in range(int(f),int(l)+1):
    u=url+str(i)
    r=requests.get(u)
    soup=BeautifulSoup(r.text,'html.parser')
    links=soup.find_all(target='_blank')
    for link in links:
        l=link.get('href')
        if 'download' in l:
            r1=requests.get(l)
            s1=BeautifulSoup(r1.text,'html.parser')
            l1=s1.find_all('a') #Download page array list with different quality
            # for q1 in qualities[::-1][qualities.index(qualities[int(quality) - 1]):]: #q1 = 480,360,HD
            end_ind = q_rev.index(qualities[int(quality)-1])
            for q1 in q_rev[end_ind:]:  # q1 = 480,360,HD
                flag=0
                for l2 in l1[::-1]:
                    if q1 in l2.text:
                        des = d + '/' + n + str(i) + '.mp4'
                        print(f"Download : Episode[{i}] {des} at quality : {q1} \n\tLink : \u001b[34m{l2.get('href')}\u001b[30m")
                        flag = 1
                        dwn_link = l2.get('href')
                        if dwn_link[-4:] == ".mp4":   #Restriccted to HD only until now
                            download(dwn_link, des)
                        break
                    else:
                        continue
                if flag:
                    break
import platform
if s == "y":
    if os.name == 'nt': #ntos - kernel name for windows 7
        os.system("shutdown /s /t 3")
    elif os.name == 'posix' or platform.system() == "Linux": #ubuntu
        os.system("init 0")
    elif platform.system() == "Darwin": #mac
        os.system("poweroff")
