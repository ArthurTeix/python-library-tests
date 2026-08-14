from rich import print
from rich.panel import Panel # panel: módulo  |  Panel: classe

caixa = Panel("Painel usando rich")
print(caixa)

# No meu panel posso adicionar outros parâmetros
# :title: msg no topo do panel
# :style: cor do panel
title = Panel("[red]Aqui vai seguir meu texto[/]", title='Título no topo', style="cyan")
print(title)
