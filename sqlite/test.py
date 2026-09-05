import sqlite3

conexao = sqlite3.connect("sqlite/banco.db")
cursor = conexao.cursor()

a = 'carro'

cursor.execute(f"""CREATE TABLE IF NOT EXISTS perguntas_{a} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                resposta INTEGER NOT NULL
                )""")

# cursor.execute("""
# INSERT INTO perguntas_carro (pergunta, resposta)
# VALUES ("O que faz o carro funcionar?", "motor")
# """)


# cursor.execute("SELECT * FROM perguntas_carro")
cursor.execute("SELECT id, pergunta, resposta FROM perguntas_carro")
res = cursor.fetchall()

for r in res:
    id, pergunta, resposta = r
    print(f"""
{id}º Pergunta: {pergunta}
Resposta: {resposta}
""")

conexao.commit()
