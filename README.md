# Builders That Matter

A minimalist, modern portfolio website showcasing early-stage European startups that are making a difference.

## Features

- Clean, minimalist design inspired by modern portfolio aesthetics
- Fully responsive (desktop and mobile)
- Investment thesis section
- Toggle between Grid and Table view
- Modern typography and spacing
- Smooth transitions and interactions

## Setup

1. Install Python 3.8 or higher

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Customization

All content lives in `data/` as JSON, separate from the app logic in `app.py`. Restart the app after editing to see changes.

### Investment Thesis
Edit `data/thesis.json` to update the heading and paragraphs:
```json
{
  "heading": "WHY THIS EXISTS",
  "paragraphs": ["First paragraph...", "Second paragraph..."]
}
```

### Startup Data
Edit `data/startups.json` to add, remove, or modify startup entries. Each entry should have:
- `name`: Company name
- `tagline`: Short tagline
- `description`: Detailed description
- `sector`: Industry sector
- `stage`: Funding stage (e.g., Pre-Seed, Seed, Series A)
- `year`: Year founded or invested
- `location`: City and country
- `website`: Company website URL (optional)

Alternatively, run `python import_startups.py` to import entries from a `startups.csv` file (e.g. exported from Notion) — it writes straight to `data/startups.json`.

## Deployment

This Flask app can be deployed to:
- Heroku
- PythonAnywhere
- Railway
- Render
- Or any Python hosting service

