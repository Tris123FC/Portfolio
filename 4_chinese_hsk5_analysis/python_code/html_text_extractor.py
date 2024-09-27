from selenium import webdriver
from bs4 import BeautifulSoup
from docx import Document
from datetime import datetime
import re
import time
from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Regular expression to match Chinese characters
chinese_char_pattern = re.compile(r'[\u4e00-\u9fff0-9]+')

# URL of the page to scrape
base_url = 'https://hskreading.com/intermediate/page/2/'

# Initialize the Selenium WebDriver
driver = webdriver.Safari()

# Open the page
driver.get(base_url)

# Get the page source after JavaScript has rendered the content
html = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <article> elements and extract links within them
links = set()  # Use a set to avoid duplicate links
for art in soup.find_all('article'):
    for a in art.find_all('a', href=True):
        href = a['href']
        if href.startswith('#') or href == '':
            continue
        full_url = urljoin(base_url, href)
        links.add(full_url)

# To hold the extracted text from all pages
all_chinese_texts = []

# Iterate through all valid links and extract <ruby> tags' text from each page
for link in sorted(links):  # Sort links to ensure consistent order
    try:
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_html = driver.page_source
        page_soup = BeautifulSoup(page_html, 'html.parser')

        # Collect texts from ruby tags in the order they appear
        ruby_texts = []
        for ruby in page_soup.find_all('rb'):
            text = ruby.get_text()
            chinese_chars = ''.join(chinese_char_pattern.findall(text))
            if chinese_chars:
                ruby_texts.append(chinese_chars)

        # Append the texts in the order they were found on the page
        if ruby_texts:
            all_chinese_texts.extend(ruby_texts)
    except Exception as e:
        print(f"Error processing link {link}: {e}")


# Export the extracted text to a Word document
def export_characters_to_word(char_list, base_filename):
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{base_filename}_{timestamp}.docx"
        doc = Document()
        text = ''.join(char_list)
        doc.add_paragraph(text)
        doc.save(filename)
        print(f"Document saved as {filename}")
    except Exception as e:
        print(f"Error exporting document: {e}")


# Export the extracted Chinese text from all pages
export_characters_to_word(all_chinese_texts, 'hsk_chinese_text')

# Close the browser
driver.quit()
print(links)
print("Chinese text extraction and export completed successfully.")