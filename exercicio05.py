"Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS"
neg = 0
for N in range (1,11):
    num = int(input("Digite o número: "))
    if num < 0:
        neg += 1
print(f"A quantidade de números negativos são: {neg}")
