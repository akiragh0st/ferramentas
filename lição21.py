nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
try:
    media = (nota1 + nota2 + nota3) / 3
    with open("pessoa.txt", "a") as nota:
        nota.write(nome + " | " + str(nota1) + " | " + str(nota2) + " | " + str(nota3) + " | " + f"{media:.2f}" + "\n")
except TypeError:
    print(f"Digite corretamente as notas")