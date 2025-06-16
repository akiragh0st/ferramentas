pergunta = 12
while pergunta != 4:
    pergunta = int(input(f"O'que deseja fazer?\n 1- Faz um pix \n 2- Mostra o extrato \n 3- Deposita \n 4- Saia do sistema \n digite o numero:"))
    Saldo = 100
    valor = 0
    if pergunta == 1:
        nome = input(f"Para quem você deseja fazer o pix?")
        valor = float(input(f"Qual o valor?")) 
        print(f"Pix de {valor}R$ feito com sucesso para {nome}")
    elif pergunta ==2:
        Saldo = 100
        extrato = Saldo - valor
        print(f"seu saldo é {extrato}R$")
    elif pergunta ==3:
        deposito = float(input(f"Quanto você deseja colocar no deposito?"))
        print(f"Deposito de {deposito}R$ concluido")
    else:
        print(f"Concluido")

