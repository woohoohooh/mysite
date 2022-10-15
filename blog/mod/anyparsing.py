from bs4 import BeautifulSoup
import requests

def parsing(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    return results

