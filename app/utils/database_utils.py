import sqlite3
import random

def random_from_count() -> int:
    db = sqlite3.connect("app/utils/database.db")
    cursor = db.cursor()
    count = cursor.execute("SELECT count(*) FROM prophecy").fetchone()[0]
    return random.randint(1, count) if count > 0 else 0 


