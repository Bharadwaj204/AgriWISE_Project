import sqlite3

# Create the database and table (if not exists)
def create_database():
    conn = sqlite3.connect("agriwise.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farm_id TEXT,
            recommended_crop TEXT,
            market_crop TEXT,
            weather_status TEXT,
            sustainability_score REAL,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()

# Insert one row of data
def insert_result(farm_id, recommended_crop, market_crop, weather_status, sustainability_score, date):
    conn = sqlite3.connect("agriwise.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO results (farm_id, recommended_crop, market_crop, weather_status, sustainability_score, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (farm_id, recommended_crop, market_crop, weather_status, sustainability_score, date))

    conn.commit()
    conn.close()
    print("✅ Data inserted!")

# View all saved data
def fetch_all_results():
    conn = sqlite3.connect("agriwise.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM results")
    data = cur.fetchall()

    conn.close()
    return data
