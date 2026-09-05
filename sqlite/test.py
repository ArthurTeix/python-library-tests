import sqlite3

conexao = sqlite3.connect("sqlite/banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
                )""")

cursor.execute("""
DELETE FROM contas_bancarias
WHERE id = 2
""")

conexao.commit()
