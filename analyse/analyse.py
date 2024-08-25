import pandas as pd
import os

# Define the directory where the files are stored
directory = 'data/'

# List of file names to process
files = [
    'abb.csv', 'araz.csv', 'bravo.csv', 'emanat.csv', 'express.csv', 
    'kb.csv', 'million.csv', 'oba.csv', 'ub.csv'
]

# Initialize an empty list to hold the standardized dataframes
dataframes = []

# Mapping of columns to the standardized format
columns_map = {
    'abb.csv': {'Store': 'name', 'Location': 'address', 'Lat': 'latitude', 'Lng': 'longitude'},
    'araz.csv': {'MarketName': 'name', 'AddressLine': 'address', 'Latitude': 'latitude', 'Longitude': 'longitude'},
    'bravo.csv': {'name': 'name', 'address': 'address', 'lat': 'latitude', 'lng': 'longitude'},
    'emanat.csv': {'Name': 'name', 'Address': 'address', 'Latitude': 'latitude', 'Longitude': 'longitude'},  # Missing Latitude & Longitude
    'express.csv': {'name': 'name', 'address': 'address', 'latitude': 'latitude', 'longitude': 'longitude'},
    'kb.csv': {'name': 'name', 'address': 'address', 'lat': 'latitude', 'lng': 'longitude'},
    'million.csv': {'id': 'name', 'address': 'address', 'latitude': 'latitude', 'longitude': 'longitude'},  # Using id as Name placeholder
    'oba.csv': {'Name': 'name', 'Address': 'address', 'Latitude': 'latitude', 'Longitude': 'longitude'},
    'ub.csv': {'Name': 'name', 'Address': 'address', 'Latitude': 'latitude', 'Longitude': 'longitude'},  # Missing Latitude & Longitude
}

# Loop through the files, standardize each one, and add a 'company' column
for file in files:
    # Determine the company name based on the file name
    company_name = os.path.splitext(file)[0].upper()  # Using the file name as the company name
    
    # Load the CSV file into a dataframe
    df = pd.read_csv(os.path.join(directory, file))
    
    # Convert columns to lowercase for consistent handling
    df.columns = df.columns.str.lower()
    
    # Log the columns found in the file before renaming
    print(f"Processing {file}: columns found -> {df.columns.tolist()}")
    
    # Map the columns to the standardized format
    if file in columns_map:
        df = df.rename(columns=columns_map[file])
        # Log the columns after renaming
        print(f"After renaming {file}: columns -> {df.columns.tolist()}")
    
    # Check if the required columns are present
    required_columns = ['name', 'address', 'latitude', 'longitude']
    if all(column in df.columns for column in required_columns):
        # Ensure only the standardized columns are selected
        df = df[required_columns]
        
        # Add the 'Company' column
        df['company'] = company_name
        
        # Append the standardized dataframe to the list
        dataframes.append(df)
    else:
        missing_columns = [col for col in required_columns if col not in df.columns]
        print(f"Skipping {file}: required columns missing -> {missing_columns}")

# Concatenate all dataframes into a single dataframe
if dataframes:  # Ensure there is at least one dataframe
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the combined dataframe to a new CSV file
    output_file = os.path.join(directory, 'combined_data.csv')
    combined_df.to_csv(output_file, index=False)
    
    print(f"Data has been combined and saved to {output_file}")
else:
    print("No dataframes were combined due to missing columns.")
