#coding:utf8
import requests
import re
import os
import threading
import time
def download(html,path):
    reg = r'src="(.+?\.jpg)"'
    r=re.compile(reg)
    s=r.findall(html)
    for one in  s:
        # print(one)
        name=one.split('/')[-1]
        if 'http:'in one:
            downurl=one
        else:
            downurl='http:'+one
        try:
            j=requests.get(downurl,headers=header).content
            spath=path+'\\'+name
            f=open(spath,'wb')
            f.write(j)
            f.close()
        except:
            continue
if __name__ == '__main__':
    start = input('The initial page: ')
    end = input('The final page: ')
    url1='http://jandan.net/ooxx/page-%d#comments'
    header={'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
             }
    path='H:\\robit\\finaltest'
    now=time.clock()
    for i in range(int(start),int(end)):
        url=url1%i
        ipath = path + '\\' + str(i)
        if not os.path.exists(ipath):
            os.makedirs(ipath)
        try:
            html=requests.get(url,headers=header).text
            t=threading.Thread(target=download, args=(html, ipath))
            t.start()

        except:
            continue
    pre=time.clock()
    print(pre-now)




