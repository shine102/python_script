import requests, csv, bs4

# Get the list alerts
list_alerts = requests.get('https://www.cisa.gov/uscert/ncas/alerts/2022')
soup = bs4.BeautifulSoup(list_alerts.text, 'html.parser')

# Get the number of alerts
num_of_alerts = soup.findAll('span', {'class': 'field-content'})

alert_header = ['Alert ID', 'Alert Name', 'Release Date', 'Last Revived', 'Alert Link']
alerts_details = []


for alert in num_of_alerts:
    page = requests.get('https://www.cisa.gov/uscert/' + alert.find('a').get('href'))
    soup2 = bs4.BeautifulSoup(page.text, 'html.parser')
    alert_id = soup2.find('h1', {'id': 'page-title'}).text
    alert_name = soup2.find('h2', {'id': 'page-sub-title'}).text
    original_release = soup2.find('div', {'class': 'submitted meta-text'}).text[22:]
    # if (soup2.find('div'))

with open('alerts.csv', 'w') as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)
    writer.writerow(alert_header)
    writer.writerows(alerts_details)
