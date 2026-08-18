"""
Helper script to import startups from CSV or manually add them.
You can export your Notion page as CSV and use this script to format the data.
"""

import csv
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "startups.json"

def import_from_csv(csv_file_path):
    """
    Import startups from a CSV file exported from Notion.
    Expected CSV columns: Name, Description, Sector, Stage, Location, Website
    """
    startups = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                startup = {
                    "name": row.get('Name', '').strip(),
                    "tagline": row.get('Tagline', '').strip(),
                    "description": row.get('Description', '').strip(),
                    "sector": row.get('Sector', '').strip(),
                    "stage": row.get('Stage', '').strip(),
                    "year": int(row.get('Year', 2024)) if row.get('Year', '').strip().isdigit() else 2024,
                    "location": row.get('Location', '').strip(),
                    "website": row.get('Website', '').strip() or row.get('URL', '').strip()
                }
                if startup['name']:  # Only add if name exists
                    startups.append(startup)
        
        return startups
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def write_to_data_file(startups):
    """
    Write the startups list to data/startups.json.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(startups, f, indent=2, ensure_ascii=False)
        f.write("\n")

# Example usage:
# 1. Export your Notion page as CSV
# 2. Run: python import_startups.py
# 3. data/startups.json is updated automatically - restart the app to see changes

if __name__ == "__main__":
    # Update this path to your exported CSV file
    csv_path = "startups.csv"

    print("Importing startups from CSV...")
    startups = import_from_csv(csv_path)

    if startups:
        write_to_data_file(startups)
        print(f"\nSaved {len(startups)} startups to {DATA_FILE}")
    else:
        print("No startups found. Please check your CSV file path and format.")


