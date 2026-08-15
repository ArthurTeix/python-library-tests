from rich.traceback import install # exibe os erros mais bem organizados
install()

def div(x, y):
    return x / y

print(div(4, 2))

idade = int(input("Digite sua idade: ")) # uma variável int

# vou inputar string e o erro será mostrado de uma ótima forma visual
print(idade) 
