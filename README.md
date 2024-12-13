# Business Data Scraper

## Overview
This tool scrapes business-related data from open-source platforms, processes it, and saves it in CSV format.

## Features
- Scrapes data (name, price, description) across multiple pages.
- Processes and cleans the data (removes duplicates and missing values).
- Saves the output to `data/business_data.csv`.

## Requirements
- Python 3.x
- Libraries: requests, BeautifulSoup4, pandas

## How to Run
1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas

# Run the script:
python src/scraper.py

# Output:
Processed data will be saved in data/business_data.csv.

  # Notes
Currently scrapes 5 pages but can be scaled easily.
Modify this line to scrape more pages:
python
Copy code
for page in range(1, 6):