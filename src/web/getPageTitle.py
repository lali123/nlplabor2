import requests
from bs4 import BeautifulSoup

def get_page_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [h1.get_text() for h1 in soup.find_all('h1')]
