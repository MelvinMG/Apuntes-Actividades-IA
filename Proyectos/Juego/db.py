import sqlite3
from datetime import datetime

DB_PATH = "eventos.db"

def crear_tabla_si_no_existe():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos_eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            velocidad_bala REAL,
            distancia REAL,
            salto INTEGER,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insertar_evento(velocidad_bala, distancia, salto):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO datos_eventos (velocidad_bala, distancia, salto, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (velocidad_bala, distancia, salto, datetime.now().isoformat()))
    conn.commit()
    conn.close()
