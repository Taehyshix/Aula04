""" Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (incluindo 0s valores 10 e 20
no intervalo) e quantos deles estão fora deste intervaslo."""
dentro = 0
fora = 0
for x in range (10):
    num = int(input("Digite o número: "))
    if num>= 10 and num<=20:
        fora=fora+1
dentro = 5-fora
print(f"Encontrei {dentro} números  no intervalo\n"
      f" {fora} números fora do intervalo")