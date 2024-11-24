import sqlite3


def get_all():
    db = sqlite3.connect("app/utils/database.db")
    cursor = db.cursor()
    entity = cursor.execute("SELECT * FROM prophecy").fetchall()
    for i in entity:
        yield i[1]
    
