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
INSERT INTO contas_bancarias (titular, saldo, cpf)
VALUES ('Arthur', 100, '15975364525')
""")

conexao.commit()
