import requests
from bs4 import BeautifulSoup

def scrape_data(url):
  try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <li> elements with class "correct_answer"
    data_list = soup.find_all('li', class_='correct_answer')

    if data_list:
      # Extract and return the text from all matching elements
      return [data.text.strip() for data in data_list]
    else:
      return ["No data found with class 'correct_answer'."]

  except requests.exceptions.RequestException as e:
    return [f"An error occurred: {e}"]


if __name__ == "__main__":
  url = "https://ccnareponses.com/modules-1-2-concepts-et-examen-de-configuration-de-lospf-reponses/"  # Replace with the target URL
  results = scrape_data(url)
  print(f"Found: {len(results)} answer")
  print("Scraped Data:")
  for result in results:
    print(result)
