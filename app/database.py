import os
import sqlite3
from pathlib import Path


# Database location can be configured through an environment variable.
# Defaults to /data/tasks.db for Docker deployments.
DATABASE = Path(
    os.environ.get(
        "DATABASE_PATH",
        "/data/tasks.db"
    )
)


def get_db_connection():
    # Ensure the database directory exists.
    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

