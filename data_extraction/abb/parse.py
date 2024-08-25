from bs4 import BeautifulSoup
import csv
import os

# List of files to process
files = [
    {'file': 'atm.html', 'type': 'atm'},
    {'file': 'branch.html', 'type': 'branch'},
    {'file': 'cashin.html', 'type': 'cashin'},
    {'file': 'division.html', 'type': 'division'},
    {'file': 'safe.html', 'type': 'safe'},
    {'file': 'terminals.html', 'type': 'terminals'}
]

# Prepare data for CSV
data = []

for item in files:
    file_path = item['file']
    location_type = item['type']
    
    # Load the HTML content from each file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all the location elements based on the provided example HTML structure
    locations = soup.find_all('div', class_='d-flex p-3 p-lg-4 border border-e4e4e4 mb-2 mr-2 hover-node js-slide')

    for location in locations:
        name = location.find('h4', class_='fw-600 fs-16 mt-0 mb-1').text.strip()
        address = location.find('span', class_='d-block fs-14 lh-18 mb-1').text.strip()
        lat = location.find('div', class_='d-flex align-items-center justify-content-between cursor-p mb-3 js-slide-header events-none').get('data-lat')
        lng = location.find('div', class_='d-flex align-items-center justify-content-between cursor-p mb-3 js-slide-header events-none').get('data-lng')

        # Append the extracted data to the list
        data.append([name, address, lat, lng, location_type])

# Define CSV file path
csv_file_path = 'abb.csv'

# Save data to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Address', 'Latitude', 'Longitude', 'Type'])
    writer.writerows(data)

print(f"Data extracted and saved to {csv_file_path}")
