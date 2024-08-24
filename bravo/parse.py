import csv
from bs4 import BeautifulSoup

# Load the HTML content
with open('bravo.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all articles
articles = soup.find_all('article')

# Extract and clean the required data
locations = []
for article in articles:
    lat = article.get('data-lat')
    lng = article.get('data-lng')
    name = article.find('h3').text.strip()
    
    # Extract all li elements under ul and ensure correct order and assignment
    location_type = ''
    phone = ''
    address = ''
    working_hours = ''
    
    li_elements = article.find_all('li')
    
    for li in li_elements:
        if 'location' in li.get('class', []):
            if location_type == '':
                location_type = li.span.text.strip()
            else:
                address = li.span.text.strip()
        elif 'phone' in li.get('class', []):
            phone = li.span.text.strip()
        elif 'time' in li.get('class', []):
            working_hours = li.span.text.strip()
    
    # Extract map link
    map_link_tag = article.find('div', class_='map_link')
    map_link = map_link_tag.a['href'] if map_link_tag and map_link_tag.a else ''
    
    # Store the data in a dictionary
    location_data = {
        'name': name.replace('\n', '').replace('\r', ''),
        'lat': lat.strip() if lat else '',
        'lng': lng.strip() if lng else '',
        'location_type': location_type.replace('\n', '').replace('\r', ''),
        'phone': phone.replace('\n', '').replace('\r', ''),
        'address': address.replace('\n', '').replace('\r', ''),
        'working_hours': working_hours.replace('\n', '').replace('\r', ''),
        'map_link': map_link.strip() if map_link else ''
    }
    
    # Append the dictionary to the list
    locations.append(location_data)

# Define CSV file name
csv_file = 'locations_cleaned.csv'

# Write data to CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=locations[0].keys())
    writer.writeheader()
    writer.writerows(locations)

print(f"Data saved to {csv_file}")
