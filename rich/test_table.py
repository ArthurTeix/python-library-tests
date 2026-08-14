from rich import print
from rich.table import Table

# Saber como e onde usar os parâmetros é o mais importante para dar vida e estilo ao projeto, principalmente enquanto estiver apenas no terminal

# Os parâmetros são os mesmos e a forma de usar também (height não funciona, pois a altura é definida pela quantidade de linhas)
table = Table(title="Tabela de Preços", style="Red", width=40)

# Posso tranquilamente misturar as libs e estilizar como quiser
table.add_column("[cyan]Nome[/]", style='blue')
table.add_column("[green]Preço[/]", style='yellow')

table.add_row("Caneta", "R$ 1.50")
table.add_row("Corretivo", "R$ 7.00")

print(table)
