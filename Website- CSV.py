#Used to extract data from website
import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[0]									#Which table to select

    rows = table.select('tbody > tr')

    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    with open('World Power Consumption(2012).csv', 'w') as csv_file:	#Creates a file to save data
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)


if __name__=="__main__":
    url = "https://en.wikipedia.org/wiki/Electric_energy_consumption"	#Website
    scrape_data(url)
