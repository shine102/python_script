import requests

session = requests.Session()

url = "http://web.chal.csaw.io:5010/"

next_link = "stuff"

cookie = ""

for i in range(100):
    req_url = url + next_link
    page = session.get(req_url)
    print(len(page.text))
    next_link = page.text[page.text.find("href=\"/")+7:page.text.find("href=\"/")+7+page.text[page.text.find("href=\"/")+7:].find('"')]
    if (len(page.text) < 100):
        print(page.text)
        break
