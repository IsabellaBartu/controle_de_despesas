# Importando SQLite
import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')


# ================================
# Inserir dados
# ================================

# Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)


# Inserir receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


# Inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


# ================================
# Deletar dados
# ================================

# Deletar receita
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)


# Deletar gasto
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)


# ================================
# Visualizar dados
# ================================

# Ver categorias
def ver_categoria():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        return cur.fetchall()


# Ver receitas
def ver_receitas():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        return cur.fetchall()


# Ver gastos
def ver_gastos():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        return cur.fetchall()

