import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace the URL below with the web page that contains the table you want to extract
url = "https://example.com"

# Send a GET request to the webpage and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element using BeautifulSoup's find() method
table = soup.find('table', {'class': 'example-table'})

# Extract the table data into a list of rows, including hyperlinks
table_data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        # Extract the cell text
        cell_text = cell.get_text().strip()

        # Extract any hyperlinks in the cell
        cell_links = []
        for link in cell.find_all('a'):
            cell_links.append(link.get('href'))

        # Append the cell text and hyperlinks to the row data
        row_data.append((cell_text, cell_links))

    # Append the row data to the table data
    table_data.append(row_data)

# Convert the table data to a pandas DataFrame
df = pd.DataFrame(table_data)

# Save the DataFrame to a CSV file
df.to_csv('example.csv', index=False)

# Print a confirmation message
print('Table extracted and saved to example.csv')
