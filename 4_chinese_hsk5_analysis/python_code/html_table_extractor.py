import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://mandarinbean.com/new-hsk-5-word-list/'  # Replace with the actual URL
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')  # Find the table element

data = []
for row in table.find_all('tr'):
    cells = row.find_all(['td', 'th'])
    cell_data = [cell.get_text(strip=True) for cell in cells]
    data.append(cell_data)

# Convert to DataFrame for easy handling
df = pd.DataFrame(data)

excel_filename = 'hsk5_voc.xlsx'  # Specify your desired filename
df.to_excel(excel_filename, index=False, header=False)  # Adjust header and index as needed

print(f'Data has been exported to {excel_filename}')

print(df)