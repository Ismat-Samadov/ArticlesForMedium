import pandas as pd

# Load all the CSV files
abb = pd.read_csv('data/abb.csv')
express = pd.read_csv('data/express.csv')
kb = pd.read_csv('data/kb.csv')
araz = pd.read_csv('data/araz.csv')
bravo = pd.read_csv('data/bravo.csv')
million = pd.read_csv('data/million.csv')
oba = pd.read_csv('data/oba.csv')

# Add a column to each dataframe to specify the type of location and the company name
abb['type'] = 'competitor'
abb['company'] = 'abb'
abb['name'] = abb['Name']

express['type'] = 'competitor'
express['company'] = 'express'
express['name'] = express['Name']

kb['type'] = 'competitor'
kb['company'] = 'kb'
kb['name'] = kb['Name']

araz['type'] = 'potential'
araz['company'] = 'araz'
araz['name'] = araz['Name']

bravo['type'] = 'potential'
bravo['company'] = 'bravo'
bravo['name'] = bravo['Name']

million['type'] = 'company'
million['company'] = 'million'
million['name'] = million['Name']

oba['type'] = 'potential'
oba['company'] = 'oba'
oba['name'] = oba['Name']

# Select only the relevant columns
abb = abb[['lat', 'lon', 'type', 'company', 'name']]
express = express[['lat', 'lon', 'type', 'company', 'name']]
kb = kb[['lat', 'lon', 'type', 'company', 'name']]
araz = araz[['lat', 'lon', 'type', 'company', 'name']]
bravo = bravo[['lat', 'lon', 'type', 'company', 'name']]
million = million[['lat', 'lon', 'type', 'company', 'name']]
oba = oba[['lat', 'lon', 'type', 'company', 'name']]

# Combine all dataframes into one
combined_df = pd.concat([abb, express, kb, araz, bravo, million, oba], ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('data/data.csv', index=False)
