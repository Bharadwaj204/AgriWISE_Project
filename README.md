# AgriWISE – AI for Sustainable Farming 🌾

## Problem Statement
To promote eco-friendly farming by helping farmers choose the best crops using weather, soil, market, and sustainability data.

## Solution
We built a multi-agent AI system with 4 simple expert agents:
- 👨‍🌾 Farmer Advisor – suggests best crops
- 📊 Market Researcher – finds profitable crops
- 🌦️ Weather Agent – checks if it’s good time to plant
- 🌱 Sustainability Agent – scores how eco-friendly the plan is

The results are stored in a SQLite database, and a Streamlit web app is provided for interaction.

## Folder Structure
- `agents/`: AI agent files
- `data/`: Sample farm and market data
- `database/`: SQLite DB (`agriwise.db`)
- `ui/`: Streamlit app
- `db_helper.py`: Handles DB operations

## How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
"# AgriWISE_Project" 
