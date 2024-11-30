import os
import requests
import json

# Folder where the data will be stored
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# Base URL for SpaceX API
BASE_URL = "https://api.spacexdata.com/v5/launches"


# Function to fetch and save data from SpaceX API
def fetch_and_save_data(endpoint, filename):
    print(f"Fetching data from {BASE_URL}{endpoint}...")

    # Send a GET request to the API
    response = requests.get(f"{BASE_URL}{endpoint}")

    if response.status_code != 200:
        print(f"Failed to retrieve data from {BASE_URL}{endpoint}")
        return None

    # Parse the response as JSON
    data = response.json()

    # Save the data to a JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data saved to {filename}")
    return data


# Function to scrape the latest launch data
def scrape_latest_launch():
    # Fetch latest launch data from the API
    latest_launch_data = fetch_and_save_data(
        "/latest", os.path.join(DATA_FOLDER, "spacex_data.json")
    )
    return latest_launch_data


# Main function to execute the scraper
def main():
    # Scrape data for the latest launch
    scrape_latest_launch()
    print("SpaceX launch data scraping complete!")


if __name__ == "__main__":
    main()
