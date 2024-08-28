import pandas as pd

# Load all the CSV files
abb = pd.read_csv('data/abb.csv')
express = pd.read_csv('data/express.csv')
kb = pd.read_csv('data/kb.csv')
araz = pd.read_csv('data/araz.csv')
bravo = pd.read_csv('data/bravo.csv')
million = pd.read_csv('data/million.csv')
oba = pd.read_csv('data/oba.csv')

# Add a column to each dataframe to specify the type of location
abb['type'] = 'competitor'
express['type'] = 'competitor'
kb['type'] = 'competitor'
araz['type'] = 'potential'
bravo['type'] = 'potential'
million['type'] = 'company'
oba['type'] = 'potential'

# Select only the lat, lon, and type columns
abb = abb[['lat', 'lon', 'type']]
express = express[['lat', 'lon', 'type']]
kb = kb[['lat', 'lon', 'type']]
araz = araz[['lat', 'lon', 'type']]
bravo = bravo[['lat', 'lon', 'type']]
million = million[['lat', 'lon', 'type']]
oba = oba[['lat', 'lon', 'type']]

# Combine all dataframes into one
combined_df = pd.concat([abb, express, kb, araz, bravo, million, oba], ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('data/combined_kiosk_locations.csv', index=False)
