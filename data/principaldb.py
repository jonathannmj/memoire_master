import sqlite3

connection = sqlite3.connect("principalDB.db")
cursor = connection.cursor()

def create_db():
  cursor.executescript(
    """CREATE TABLE IF NOT EXISTS destination_paths(
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_path TEXT NOT NULL UNIQUE
    )
  """
  )
  connection.close()
