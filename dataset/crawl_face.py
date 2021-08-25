from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time
from bs4 import BeautifulSoup as bs

def urlopen_custom(req_custom):
    try:
        html = urlopen(req_custom)
    except HTTPError as e:
        print(e.headers["Retry-After"])
        if e.getcode() == 429:
            time.sleep(int(e.headers["Retry-After"]))
        html = urlopen(req_custom)
        print(e)

    return html


BASE_URL = "https://namu.wiki"
req = Request(BASE_URL+"/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD", headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen_custom(req)
bsObject = bs(html, "html.parser")

links = bsObject.find_all("a", {"class": "wiki-link-internal"})
print(len(links))
img_count = 0



for link in links:
    if link.get("title") == "배우" or link.get("class") == ["wiki-link-internal", "not-exist"]:
        continue
    req = Request(BASE_URL+link.get("href"), headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen_custom(req)


    bsObject = bs(html, "html.parser")
    img_div = bsObject.find("div", {"class": "wiki-table-wrap table-right"})
    try:
        img_link = img_div.find("img", {"class": "wiki-image"}).get("data-src")
        req = Request("https:"+img_link, headers={'User-Agent': 'Mozilla/5.0'})

        with urlopen_custom(req) as f:
            with open('./images/'+str(img_count)+'.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        img_count += 1
    except:
        pass
    time.sleep(0.84)
    #print(link.get("title"))
    #print(link.get("href"))
