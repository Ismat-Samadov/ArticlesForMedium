import csv
from bs4 import BeautifulSoup

# Load the HTML content
with open('araz.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all relevant divs that contain store information
stores = soup.find_all('div', class_='js-slide')

# Create a list to hold all the extracted data
data = []

# Iterate through each store and extract the necessary information
for store in stores:
    lat = store.find('div', class_='js-slide-header')['data-lat']
    lng = store.find('div', class_='js-slide-header')['data-lng']
    name = store.find('h4').text.strip()
    category = store.find('span', class_='radius-6').text.strip()
    address = store.find('span', class_='js-address').text.strip()

    # Attempt to find the working hours and phone number, handle missing elements
    working_hours_tag = store.find('span', string="İş vaxtı")
    working_hours = working_hours_tag.find_next('span').text.strip() if working_hours_tag else "N/A"

    phone_tag = store.find('span', string="Telefon")
    phone = phone_tag.find_next('span').text.strip() if phone_tag else "N/A"

    # Append the extracted information to the data list
    data.append([name, lat, lng, category, address, working_hours, phone])

# Define the CSV file name
csv_file = 'araz.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Name', 'Latitude', 'Longitude', 'Category', 'Address', 'Working Hours', 'Phone'])
    # Write the data
    writer.writerows(data)

print(f"Data has been successfully saved to {csv_file}.")
