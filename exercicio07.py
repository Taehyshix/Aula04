# Ler 5 valores, calcular e escrever a média aritmética desses valores lidos.
soma = 0
for x in range (5):
    num = int(input("Digite o valor: "))
    soma=num+soma
media = soma /5
print(f"A média é {media}")
