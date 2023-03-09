import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the GitHub page
url = 'https://github.com/public-api-lists/public-api-lists#public-api-lists'
response = requests.get(url)

# Create a BeautifulSoup object from the page source
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element and extract its rows
table = soup.find('table')
rows = table.find_all('tr')

# Create an empty list to store the data
data = []

# Loop through the rows and extract the data
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0:
        api_link = cells[0].find('a')['href']
        api_name = cells[0].text.strip()
        auth = cells[1].text.strip()
        https = cells[2].text.strip()
        cors = cells[3].text.strip()
        data.append([api_name, api_link, auth, https, cors])

# Create a pandas dataframe with clickable hyperlinks in the "API" column
df = pd.DataFrame(data, columns=['API', 'API Link', 'Auth', 'HTTPS', 'CORS'])
df['API'] = df.apply(lambda x: '<a href="' + x['API Link'] + '">' + x['API'] + '</a>', axis=1)
df.drop('API Link', axis=1, inplace=True)

# Display the dataframe
print(df.to_html(escape=False))
