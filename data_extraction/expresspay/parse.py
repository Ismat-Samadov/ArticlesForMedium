import requests
import csv

def fetch_terminal_data():
    url = "https://expresspay.az/terminals/points"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,az;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "expresspay.az",
        "Referer": "https://expresspay.az/terminals",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("Data retrieved successfully!")
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clean_data(item):
    # Remove or replace double quotes within the data
    for key in item:
        if isinstance(item[key], str):
            item[key] = item[key].replace('"', '')  # Replace double quotes with nothing
    return item

def save_to_csv(data, filename="terminal_data_cleaned.csv"):
    if not data or 'data' not in data:
        print("No data available to save.")
        return

    # Extract the list of terminal data
    terminals = data['data']

    # Clean the data
    terminals = [clean_data(item) for item in terminals]

    # Check if the terminal data is a list and contains dictionaries
    if isinstance(terminals, list) and all(isinstance(item, dict) for item in terminals):
        keys = terminals[0].keys()

        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(terminals)

        print(f"Data saved to {filename}")
    else:
        print("Expected data structure not found.")
        print(f"Actual data: {data}")

if __name__ == "__main__":
    data = fetch_terminal_data()
    if data:
        save_to_csv(data)
    else:
        print("No data to process.")
