# Exercicio para aceitar somente valores maiores que 0 para N.
# Caso o valor informado (para N) não seja maior que 0, número tem que ser inválido.
num = int(input("Digite um número: "))
if num <= 0:
     print("Número inválido!")
else:
    for N in range(1,num+1,1):
         print(N, end=" ")