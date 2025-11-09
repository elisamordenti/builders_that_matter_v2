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

### Investment Thesis
Edit the `INVESTMENT_THESIS` variable in `app.py` to update the investment thesis paragraph.

### Startup Data
Edit the `STARTUPS` list in `app.py` to add, remove, or modify startup entries. Each startup should have:
- `name`: Company name
- `tagline`: Short tagline
- `description`: Detailed description
- `sector`: Industry sector
- `stage`: Funding stage (e.g., Pre-Seed, Seed, Series A)
- `year`: Year founded or invested
- `location`: City and country
- `website`: Company website URL (optional)

## Deployment

This Flask app can be deployed to:
- Heroku
- PythonAnywhere
- Railway
- Render
- Or any Python hosting service

