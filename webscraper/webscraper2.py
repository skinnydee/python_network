import requests
from bs4 import BeautifulSoup

url = 'https://itsfoss.com/'
page = requests.get(url)
text = page.text
soup = BeautifulSoup(text, 'html.parser')

#site = soup.find('div', class_='ugb-block-content')
page =  soup.find_all('article',class_='ugb-blog-posts__item ugb--shadow-5')

for pages in page:
    print(pages.text)

#for page in site:
#     if page.select('div', class_='ugb-blog-posts__content'):
#         print(page.text)
        
        

