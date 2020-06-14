#Used to Extract Data from Website
import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

	response = requests.get(url, timeout=10)
	soup = BeautifulSoup(response.content, 'html.parser')

	table = soup.find_all('table')[0]										# Table Selection

	rows = table.select('tbody > tr')

	header = [th.text.rstrip() for th in rows[0].find_all('th')]
	header.pop()
	

	with open('Covid-19.csv', 'w') as csv_file:								#Creates a file to Save Data
		writer = csv.writer(csv_file)
		writer.writerow(header)
		for row in rows[1:-2]:
			header = [th.text.rstrip() for th in row.find_all('th')]
			data = [th.text.rstrip() for th in row.find_all('td')]
			data = header + data
			data.pop()
			data.pop(0)
			writer.writerow(data)


if __name__=="__main__":
    url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"	#Website
    scrape_data(url)
