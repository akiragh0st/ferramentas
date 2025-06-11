nome = input("Qual seu nome?:")
nota_1 = float(input("Qual sua nota?"))
nota_2 = float(input("segunda nota?"))
nota_3 = float(input("terceira nota?"))
media = (nota_1 + nota_2 + nota_3)/3
print(media)
if media >= 7:
    print(f"{nome} aprovado por {media}")
elif media >= 4:
    print(f"{nome} em recuperação por {media}")
else:
    print(f"{nome}, seu QI é negativo, por {media}")
