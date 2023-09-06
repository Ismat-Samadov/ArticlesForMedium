import requests
import pandas as pd

# Define the URL of the API
api_url = "https://www.kapitalbank.az/locations/region?is_nfc=false&weekend=false&type=branch"

try:
    # Send an HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Create a list to store all the data
        all_data = []

        # Iterate through the data and extract all fields
        for item in data:
            all_data.append(item)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(all_data)

        # Save the DataFrame to an Excel file
        df.to_excel("kapital_bank_locations.xlsx", index=False)

        print("All data has been saved to kapital_bank_locations.xlsx")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
