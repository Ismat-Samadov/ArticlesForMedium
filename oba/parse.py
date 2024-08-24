import csv
from bs4 import BeautifulSoup

# Load the HTML content
with open("oba.html", "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Prepare the CSV file
with open("oba_market_locations.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ['Name', 'Address', 'Latitude', 'Longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find all the market divs
    market_divs = soup.find_all('div', class_='br_item border-bottom border-eaeaea px-4 pt-4 pb-3 cursor-p events-none js-map-coordinates')

    # Iterate over each market div and extract the data
    for market in market_divs:
        name = market.find('h3', class_='fs-16 lh-24 fw-600 mb-2').text.strip()
        address = market.find('p', class_='color-gray fs-15 lh-24 fw-400 mb-3').text.strip()
        latitude = market.get('data-lat')
        longitude = market.get('data-lng')

        # Write the extracted data to the CSV file
        writer.writerow({'Name': name, 'Address': address, 'Latitude': latitude, 'Longitude': longitude})

print("Data extraction and CSV creation completed.")
