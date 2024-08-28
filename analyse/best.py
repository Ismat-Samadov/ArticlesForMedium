import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
import random

np.random.seed(42)
random.seed(42)


# Load the newly provided combined CSV file
filtered_df = pd.read_csv('data/data.csv')

# Ensure that the latitude and longitude data are in numeric format
filtered_df['lat'] = pd.to_numeric(filtered_df['lat'], errors='coerce')
filtered_df['lon'] = pd.to_numeric(filtered_df['lon'], errors='coerce')

# Drop rows with invalid lat/lon values
filtered_df = filtered_df.dropna(subset=['lat', 'lon'])

# Extract latitude and longitude for competitors and company kiosks
competitor_coords = filtered_df[filtered_df['type'] == 'competitor'][['lat', 'lon']].values
company_coords = filtered_df[filtered_df['type'] == 'company'][['lat', 'lon']].values

# Build KD-Trees for fast nearest-neighbor lookup
competitor_tree = cKDTree(competitor_coords)
company_tree = cKDTree(company_coords)

# List to store final scores
final_scores = []

# Iterate through each potential location
for index, row in filtered_df[filtered_df['type'] == 'potential'].iterrows():
    potential_loc = [row['lat'], row['lon']]
    
    # Find the nearest competitor and company kiosk
    _, nearest_competitor_dist = competitor_tree.query(potential_loc)
    _, nearest_company_dist = company_tree.query(potential_loc)
    
    # Calculate scores based on distances
    score_competitor = nearest_competitor_dist  # further is better
    score_company = 1 / nearest_company_dist if nearest_company_dist > 0 else 0  # closer is better
    
    # Calculate weighted score
    weighted_score = (score_competitor * 0.6) + (score_company * 0.4)
    
    # Append the score with the location data
    final_scores.append((row['lat'], row['lon'], row['name'], row['company'], weighted_score))

# Convert the final scores into a DataFrame for easy viewing
scores_df_optimized = pd.DataFrame(final_scores, columns=['Latitude', 'Longitude', 'Location Name', 'Company', 'Weighted Score']).sort_values(by='Weighted Score', ascending=False)

# Select the top 3 results (highest scores)
top_3 = scores_df_optimized.head(3)
print(top_3)
top_3.to_csv('top_3_best_locations.csv', index=False)
