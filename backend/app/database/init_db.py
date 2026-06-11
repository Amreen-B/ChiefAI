from app.database.db import get_connection


def init_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS startup_reports (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   
        report_json TEXT,

        filename TEXT,

        opportunity_score REAL,
        risk_score REAL,
        market_score REAL,
        execution_score REAL,
        investor_readiness REAL,
        overall_score REAL,

        research TEXT,
        strategy TEXT,
        risk TEXT,
        execution TEXT,

        investor TEXT,
        funding TEXT,
        swot TEXT,
        pitchdeck TEXT,
        summary TEXT,
        competitors TEXT

    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_database()