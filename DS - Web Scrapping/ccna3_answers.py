import bs4
import requests

# Scrape answers from strong tags inside <li><span style="color: rgb(255, 0, 0);"><strong>...</strong></span></li>
link = "https://itexamanswers.net/ccna-3-v7-modules-3-5-network-security-exam-answers.html"
response = requests.get(link)
html_content = response.text

soup = bs4.BeautifulSoup(html_content, 'html.parser')
# Find all <li> tags
answers = soup.find_all('li')
# print(soup)
# print(answers)
for answer in answers:
    # Look for a <span> with a style containing the red color, and a <strong> inside it
    span = answer.find('span', style=lambda s: s and 'color: rgb(255, 0, 0)' in s)
    print(span)
    if span:
        strong_tag = span.find('strong')
        if strong_tag:
            print(strong_tag.text.strip())
