import re
from bs4 import BeautifulSoup

file_path = '/Users/gyanendrachaubey/.gemini/antigravity/brain/cbc398f2-51a5-43b2-9498-ceb3258e15cb/.system_generated/steps/164/content.md'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

papers = []
for item in soup.find_all('tr', class_='gsc_a_tr'):
    title_tag = item.find('a', class_='gsc_a_at')
    if not title_tag:
        continue
    title = title_tag.text.strip()
    
    # authors and venue are typically in divs with class gs_gray
    gray_divs = item.find_all('div', class_='gs_gray')
    authors = gray_divs[0].text.strip() if len(gray_divs) > 0 else ""
    venue = gray_divs[1].text.strip() if len(gray_divs) > 1 else ""
    
    year_tag = item.find('span', class_='gsc_a_h')
    year = year_tag.text.strip() if year_tag else ""
    
    papers.append({
        'title': title,
        'authors': authors,
        'venue': venue,
        'year': year
    })

for i, p in enumerate(papers):
    print(f"{i+1}. {p['title']} ({p['year']}) - {p['authors']} - {p['venue']}")
