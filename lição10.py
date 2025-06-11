pergunta = int(input("Qual numero você não sabe"))
numerocome = int(input("Qual numero você começa"))
numerofin = int(input("Qual numero você termina"))
for i in range(numerocome, numerofin):
    print(f"{i} x {pergunta} = {i * pergunta}")