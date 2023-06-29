#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "http://quotes.toscrape.com"

try:
    # Send a GET request to the webpage
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')

    # Extract the quote text and author from each quote element
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"Quote: {text}\nAuthor: {author}\n")

except Exception as e:
    print('Error:', str(e))


# In[2]:


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL of the webpage
url = "http://quotes.toscrape.com"

try:
    # Send a GET request to the webpage
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')

    # Extract the quote text and author from each quote element
    quote_texts = []
    quote_authors = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quote_texts.append(text)
        quote_authors.append(author)

    # Count the number of quotes by each author
    author_counts = {}
    for author in quote_authors:
        if author in author_counts:
            author_counts[author] += 1
        else:
            author_counts[author] = 1

    # Create a bar chart of the quote counts by author
    plt.figure(figsize=(8, 6))
    plt.bar(author_counts.keys(), author_counts.values())
    plt.title('Quote Counts by Author')
    plt.xlabel('Author')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

    # Create a pie chart of the quote counts by author
    plt.figure(figsize=(8, 6))
    plt.pie(author_counts.values(), labels=author_counts.keys(), autopct='%1.1f%%')
    plt.title('Quote Counts by Author')
    plt.show()

except Exception as e:
    print('Error:', str(e))

