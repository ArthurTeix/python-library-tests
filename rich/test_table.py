from rich import print
from rich.table import Table

table = Table(title="Tabela de Preços", style="Red")

table.add_column("[cyan]Nome[/]")
table.add_column("[green]Preço[/]")

table.add_row("Caneta", "R$ 1.50")
table.add_row("Corretivo", "R$ 7.00")

print(table)
