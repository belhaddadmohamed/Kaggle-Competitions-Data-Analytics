import requests
from bs4 import BeautifulSoup
import os

def download_images(query, num_images):
    url = f"https://www.alibaba.com/product-detail/baratas-one-piece-licuadora-para-batidos_1600902727904.html?spm=a2700.details.you_may_like.4.3b03c8364ANeap"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img', limit=num_images + 1)[1:]  # Skip the first image as it is a Google logo

    if not os.path.exists(query):
        os.makedirs(query)

    for i, img in enumerate(images):
        img_url = img['src']
        if img_url.startswith('http'):
            img_data = requests.get(img_url).content
            with open(f"{query}/{query}_{i + 1}.jpg", 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded {query}_{i + 1}.jpg")

if __name__ == "__main__":
    download_images('blender', 5)