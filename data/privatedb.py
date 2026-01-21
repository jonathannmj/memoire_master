import sqlite3

def create_db(database):
  connection = sqlite3.connect(database)
  cursor = connection.cursor()
  cursor.executescript(
    '''
    CREATE TABLE IF NOT EXISTS image(
    image_id INTEGER PRIMARY KEY CHECK (image_id = 0),
    image_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS equipment(
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    equipment_type TEXT,
    equipment_name TEXT
    );

    CREATE TABLE IF NOT EXISTS interface(
    interface_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER,
    FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id)
    );

    CREATE TABLE IF NOT EXISTS configuration(
    config_id INTEGER PRIMARY KEY AUTOINCREMENT,
    config_name TEXT
    )
    '''
  )
  connection.close()