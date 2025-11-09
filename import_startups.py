"""
Helper script to import startups from CSV or manually add them.
You can export your Notion page as CSV and use this script to format the data.
"""

import csv
import json

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

def format_for_app_py(startups):
    """
    Format startups list as Python code for app.py
    """
    output = "STARTUPS = [\n"
    for i, startup in enumerate(startups):
        output += "    {\n"
        output += f'        "name": "{startup["name"]}",\n'
        if startup.get("tagline"):
            output += f'        "tagline": "{startup["tagline"]}",\n'
        output += f'        "description": "{startup["description"]}",\n'
        output += f'        "sector": "{startup["sector"]}",\n'
        output += f'        "stage": "{startup["stage"]}",\n'
        output += f'        "year": {startup["year"]},\n'
        output += f'        "location": "{startup["location"]}",\n'
        output += f'        "website": "{startup["website"]}"\n'
        output += "    }"
        if i < len(startups) - 1:
            output += ","
        output += "\n"
    output += "]"
    return output

# Example usage:
# 1. Export your Notion page as CSV
# 2. Run: python import_startups.py
# 3. Copy the output and paste into app.py

if __name__ == "__main__":
    # Update this path to your exported CSV file
    csv_path = "startups.csv"
    
    print("Importing startups from CSV...")
    startups = import_from_csv(csv_path)
    
    if startups:
        print(f"\nFound {len(startups)} startups!\n")
        print("=" * 50)
        print("Copy this code into app.py (replace the STARTUPS list):\n")
        print(format_for_app_py(startups))
    else:
        print("No startups found. Please check your CSV file path and format.")


