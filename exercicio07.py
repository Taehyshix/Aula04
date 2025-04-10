# Ler 5 valores, calcular e escrever a média aritmética desses valores lidos.
soma = 0
quant = int(input("Digite a quantidade de notas: "))
for x in range (quant):
    nota = int(input("Digite o número: "))
    soma=soma+nota
media = soma /quant
print(f"A média é {media}")
