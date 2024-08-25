from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
with open('terminals.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Initialize lists to hold the extracted data
names = []
addresses = []

# Find all relevant sections containing the place information
place_items = soup.find_all('div', class_='TerminalMap_place_item__i7JSK')

# Loop through each place item and extract the name and address
for item in place_items:
    name = item.find('h3').text.strip()
    address = item.find('p').text.strip()
    names.append(name)
    addresses.append(address)

# Create a DataFrame
df = pd.DataFrame({
    'Name': names,
    'Address': addresses,
})

# Save the DataFrame to a CSV file
df.to_csv('emanat.csv', index=False)

print("Location data extracted and saved to extracted_locations.csv")
