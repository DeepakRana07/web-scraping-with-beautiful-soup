import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'

# Send a GET request and parse the HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the desired information
books = []
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    link = url + article.h3.a['href']
    books.append({'title': title, 'link': link})

# Save the data to a CSV file
filename = 'books.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for book in books:
        writer.writerow({'Title': book['title'], 'Link': book['link']})

print('Data saved to', filename)
