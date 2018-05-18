import requests



url="https://pic4.zhimg.com/80/v2-a2619db4605c37d19f5437bcd430e107_hd.jpg"

path=url.split('/')[-1]

r=requests.get(url)

with open(path,'wb') as f:
    f.write(r.content)
