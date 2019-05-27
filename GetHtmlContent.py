import urllib.request, urllib.parse

url = r"https://www.365yg.com/a6683694961021570317#mid=1591658738445325"
# url1 = r"https://www.163.com"

req = urllib.request.Request(url)


#Add request header
req.add_header("User-Agent"," Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")


def getHtml():
    data = urllib.request.urlopen(req).read().decode('utf-8')
    return data

if __name__ == '__main__':

    getHtml()
