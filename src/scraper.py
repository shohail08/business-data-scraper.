import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Step 1: Create the 'data' folder if it doesn't exist
if not os.path.exists("../data"):
    os.makedirs("../data")

# Step 2: Base URL of the website (example website for demo purposes)
base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page="

# Step 3: Initialize lists to store the scraped data
names = []
prices = []
descriptions = []

# Step 4: Loop through multiple pages (pagination)
for page in range(1, 6):  # Adjust range for the number of pages to scrape
    print(f"Scraping page {page}...")
    url = f"{base_url}{page}"
    response = requests.get(url)

    # Check for a valid response
    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract data from each product listing
    for product in soup.find_all("div", class_="thumbnail"):
        name = product.find("a", class_="title").text.strip()
        price = product.find("h4", class_="price").text.strip()
        description = product.find("p", class_="description").text.strip()

        names.append(name)
        prices.append(price)
        descriptions.append(description)

# Step 5: Create a DataFrame to store the cleaned data
data = pd.DataFrame({
    "Business Name": names,
    "Price": prices,
    "Description": descriptions
})

# Step 6: Data Cleaning
print("Cleaning the data...")
data.drop_duplicates(inplace=True)  # Remove duplicate entries
data.dropna(inplace=True)           # Remove missing values

# Step 7: Save the cleaned data to a CSV file
output_file = "../data/business_data.csv"
data.to_csv(output_file, index=False)
print(f"Data saved successfully to {output_file}")
