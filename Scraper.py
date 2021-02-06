from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://coreyms.com").text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    print()

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    print()

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        youtube_link = f'http://youtube.com/watch?v={vid_id}'

    except Exception as e:
        youtube_link = None

    print(youtube_link)
    print("-----------------------------------------")

    csv_writer.writerow([headline, summary, youtube_link])


csv_file.close()
