import sqlite3 as lite

con = lite.connect('dados.db')

# Categoria
with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
    """)

# Receitas
with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Receitas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        adicionado_em DATE,
        valor DECIMAL
    )
    """)

# Gastos
with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Gastos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        retirado_em DATE,
        valor DECIMAL
    )
    """)