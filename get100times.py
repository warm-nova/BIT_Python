import requests
import time


def getHTMLText(url):
    try:
        r=requests.get(url , timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生了异常"


if __name__=="__main__":
    url = "http://www.taobao.com"
    starttime = time.time()
    for i in range(100):
        getHTMLText(url)
    endtime = time.time()
    print("花费时间为:"+format(endtime-starttime))