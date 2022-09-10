import requests
import bs4

# Get the page
page = requests.get('https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales')
# Parse the page
soup =  bs4.BeautifulSoup(page.text, 'html.parser')

imageList = soup.findAll('img')
# print(imageList)
i = 1
for image in imageList:
    img = requests.get('https:'+image.get('src'))
    with open('./image/' + str(i) + '.png', 'wb') as f:
        f.write(img.content)
        i+=1

