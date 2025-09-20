import requests
from bs4 import BeautifulSoup
import re

def get_gym_locations(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='BNeawe deIvCb AP7Wnd'):
            name = g.get_text()
            results.append(name)
        return results
    else:
        print(f"Error: {response.status_code}")
        return []



query = 'popular gyms in Setif Algeria'
gyms = get_gym_locations(query)
for gym in gyms:
    print(gym)