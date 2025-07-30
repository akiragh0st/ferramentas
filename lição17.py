def te_jogaram_na_rua():
    print(f"Pegaram{Nome} e jogaram no meio da rua")
def Você_aceita():
    print(f"Você aceita a corrida")
def corrida():
    opçoes2 = int(input(f"{Nome}, Você vai para a largada? \n 1-Sim \n 2-Não \n digite:"))
    if opçoes2 == 1:
        print(f"{Nome} vai para a largada e se prepara para a corrida")
    else:
        Obrigado_a_correr()
def começo_corrida():
    opçoes3 = int(input(f"Corrida começou e tem um corredor na sua frente, {Nome}, O'que você faz? \n 1-Ultrapassar \n 2-Tenta derrubar o adversario \n Digite: "))
    if opçoes3 == 1:
        ultrapassar()
    else:
        chutar()
def Obrigado_a_correr():
    print(f"{Nome}, Você é obrigado a correr após te baterem com um rádio")
def ultrapassar():
    print(f"Você ultrapassou e venceu a corrida")
def chutar():
    print(f"Você tentou chutar o adversario e caiu de cara no chão")
    print(f"Você perdeu a corrida e apanhou de um rádio")

Nome = input(f"Qual seu nome? ")
opçoes = int(input(f"{Nome}, Você deseja correr uma corrida? \n 1-Sim \n 2-Não \n 3-Nem ferrando \n Resposta: ")) 
if opçoes == 1:
    Você_aceita()
    print(f"-------------------------------")
    corrida()
    print(f"-------------------------------")
    começo_corrida()
elif opçoes == 3:
    Obrigado_a_correr()
    print(f"-------------------------------")
    corrida()
    print(f"-------------------------------")
    começo_corrida()
else:   
    te_jogaram_na_rua()