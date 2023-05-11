import requests
from bs4 import BeautifulSoup
import hashlib
import csv
import sqlite3
from datetime import datetime

# set up a connection to SQLite database
conn = sqlite3.connect('articles.db')
c = conn.cursor()

# create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS articles
             (title text, link text, date text, hash text)''')

# define function to get the article data
def get_articles():
    url = 'https://www.theverge.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.h2.a.text
        link = article.h2.a['href']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # create hash of title and link to de-duplicate articles
        hash = hashlib.md5((title + link).encode('utf-8')).hexdigest()

         # create CSV file with header
        filename = datetime.now().strftime('%d%m%Y_verge.csv')
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'URL', 'headline', 'author', 'date'])

            for i, article in enumerate(articles):
                headline = article.h2.a.text
                link = article.h2.a['href']
                author = article.find('span', {'class': 'c-byline__item'}).a.text
                date = article.find('time')['datetime']

            # write article data to CSV file
            writer.writerow([i+1, link, headline, author, date])

        # check if article exists in database
        c.execute("SELECT * FROM articles WHERE hash=?", (hash,))
        result = c.fetchone()

        # if article doesn't exist, add it to database
        if not result:
            c.execute("INSERT INTO articles VALUES (?, ?, ?, ?)", (title, link, date, hash))
            conn.commit()

    # Note that this script assumes that each article on theverge.com has an author and a date.

# run the scraper daily on an AWS instance
get_articles()

#To run this script on aws we can create EC2 instance, run python script, shut it down.
# we can trigger the above process using lambda using the AWS boto3 library

# installation pre requisites
# pip install requests bs4 csv-reader