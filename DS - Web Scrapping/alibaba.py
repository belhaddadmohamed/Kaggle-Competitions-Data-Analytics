import requests
from bs4 import BeautifulSoup
import os

# Function to download images
def download_image(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)

# URL of the webpage
url = 'https://www.alibaba.com/product-detail/Home-Textile-Disposable-Shoe-Cover-PE_1600530709037.html?spm=a2700.galleryofferlist.normal_offer.d_image.7e8813a0VFgHDc'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Folder to save images
    folder = 'downloaded_images'
    
    # Loop through the image tags and download the images
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            # Handle relative URLs
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('/'):
                img_url = url + img_url
            download_image(img_url, folder)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")