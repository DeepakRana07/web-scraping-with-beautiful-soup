import requests
from bs4 import BeautifulSoup

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

# Print the book titles and links
for book in books:
    print('Title:', book['title'])
    print('Link:', book['link'])
    print()
