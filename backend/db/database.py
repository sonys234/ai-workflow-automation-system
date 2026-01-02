import sqlite3
from datetime import datetime

DB_PATH = "data/leave_requests.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leave_requests (
            id INTEGER PRIMARY KEY
            AUTOINCREMENT,
            employee_name TEXT,
            start_date TEXT,
            end_date TEXT,
            reason TEXT,
            decision TEXT,
            decision_comment TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_leave_request(leave_data, decision_data, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leave_requests (
            employee_name,
            start_date,
            end_date,
            reason,
            decision,
            decision_comment,
            status,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        leave_data.get("employee_name"),
        leave_data.get("start_date"),
        leave_data.get("end_date"),
        leave_data.get("reason"),
        decision_data.get("decision"),
        decision_data.get("comment"),
        status,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
