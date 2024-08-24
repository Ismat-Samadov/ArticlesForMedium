from bs4 import BeautifulSoup
import csv

def clean_text(text):
    return text.replace('"', '').replace('\n', ' ').replace('“', '').replace('”', '').strip()

# Load and parse the branch HTML file
with open('branch.html', 'r', encoding='utf-8') as file:
    branch_html_content = file.read()
branch_soup = BeautifulSoup(branch_html_content, 'html.parser')

# Load and parse the UTM HTML file
with open('utm.html', 'r', encoding='utf-8') as file:
    utm_html_content = file.read()
utm_soup = BeautifulSoup(utm_html_content, 'html.parser')

# Function to extract location data
def extract_locations(soup, location_type):
    locations = []
    location_items = soup.find_all('div', class_='loc__item')
    for item in location_items:
        name = clean_text(item.find('p', class_='text--bold').text)
        address = clean_text(item.find('div', class_='text--14').text)
        locations.append([name, address, location_type])
    return locations

# Extract branch and UTM locations
branch_locations = extract_locations(branch_soup, 'branch')
utm_locations = extract_locations(utm_soup, 'utm')

# Combine the locations
all_locations = branch_locations + utm_locations

# Define CSV file path
csv_file_path = 'combined_cleaned_locations.csv'

# Save data to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Address', 'Type'])
    writer.writerows(all_locations)

print(f'Cleaned and combined locations have been saved to {csv_file_path}')
