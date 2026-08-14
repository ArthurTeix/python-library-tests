from rich import print
from rich.panel import Panel # panel: módulo  |  Panel: classe

# No meu panel posso adicionar outros parâmetros
# :title: msg no topo do panel
# :style: cor do panel
# :width: largura (não exige aspas)
# :height: altura (não exige aspas)
title = Panel("[red]Aqui vai seguir meu like[/] :+1:", title='Título no topo', style="cyan", width=40, height=5)
print(title)
