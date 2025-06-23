maior=0
total=0
nome = input(f"Qual seu nome?")
for Dias in range(1,6):
    Dias_131 = int(input(f"{nome}, Quantos participantes teve no dia {Dias}? "))
    total += Dias_131
    media = total/5
    if Dias_131 > maior:
        maior = Dias_131
print(f"{nome}, O maior dia que teve participantes foi {maior}")
print(f"{nome}, O total de participantes é: {total}")
print(f"{nome}, A média de participantes de todos os dias são {media}")