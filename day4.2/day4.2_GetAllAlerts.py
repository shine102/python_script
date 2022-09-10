import requests
import bs4

page = requests.get('https://www.cisa.gov/uscert/ncas/alerts/2022')
soup = bs4.BeautifulSoup(page.text, 'html.parser')

num_of_alerts = soup.findAll('span', {'class': 'field-content'})
print(num_of_alerts.__len__())
