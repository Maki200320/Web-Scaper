import csv
import requests
from bs4 import BeautifulSoup

# URL = "http://www.values.com/inspirational-quotes"
# response = requests.get(URL)

# soup = BeautifulSoup(response.content, 'html5lib')

# quotes = []

# table = soup.find('div', attrs={'id': 'all_quotes'})

# for row in table.findAll('div',
#                          attrs={'class': 'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
#     quote = {}
#     quote['theme'] = row.h5.text
#     quote['url'] = row.a['href']
#     quote['img'] = row.img['src']
#     quote['lines'] = row.img['alt'].split(" #")[0]
#     quote['author'] = row.img['alt'].split(" #")[1]
#     quotes.append(quote)

# # Debugging: Print out the scraped quotes
# print(quotes)

# filename = 'inspirational_quotes.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
#     w.writeheader()
#     for quote in quotes:
#         # Debugging: Print out the quote before writing to CSV
#         print(quote)
#         w.writerow(quote)


# for row in table.findAll('div',
#                          attrs={'class': 'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
#     quote = {}
#     quote['theme'] = row.h5.text
#     quote['url'] = row.a['href']
#     quote['img'] = row.img['src']
#     quote['lines'] = row.img['alt'].split(" #")[0]
#     quote['author'] = row.img['alt'].split(" #")[1]
#     quotes.append(quote)

# Debugging: Print out the scraped quotes
# print(quotes)

# filename = 'inspirational_quotes.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
#     w.writeheader()
#     for quote in quotes:
#         # Debugging: Print out the quote before writing to CSV
#         print(quote)
#         w.writerow(quote)

URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/?ref=lbp"
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html5lib')

article_title_tag = soup.find('div', class_='article-title')
article_title = article_title_tag.h1.text if article_title_tag else "Title not found"

# Find the div with class 'text' to get paragraphs and list items
text_div = soup.find('div', class_='text')
if text_div:
    paragraphs = [p.text.strip() for p in text_div.find_all('p')]
    ul_tag = text_div.find('ul')
    list_items = [li.text.strip() for li in ul_tag.find_all('li')] if ul_tag else []
else:
    paragraphs = []
    list_items = []

# Create a dictionary to store the extracted data
data_dict = {
    "Article Title": article_title,
    "Paragraphs": paragraphs,
    "List Items": list_items
}

print("Data Dictionary:", data_dict)

# Write the data dictionary to a CSV file
filename = 'webscraping.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, data_dict.keys())
    w.writeheader()
    w.writerow(data_dict)