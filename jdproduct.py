import requests

kv={'user-agent':'Mozilla/5.0'}

r=requests.get("https://www.amazon.cn/dp/B00V2Y0EA4" , headers=kv)
r.encoding = r.apparent_encoding
print(r.request.headers)
print(r.text)