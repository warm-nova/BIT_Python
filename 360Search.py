import requests

kv={'q':'挖掘机技术哪家强'}
r = requests.get("http://www.so.com/s",params=kv)

print(r.request.url)
print(len(r.text))