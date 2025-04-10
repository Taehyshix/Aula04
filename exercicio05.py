"Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS"
neg = 0
for x in range (10):
    num = int(input("Digite o número: "))
    if num<0:
        neg=neg+1
print(f"A quantidade de números negativos são: {neg}")
