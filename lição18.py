Jogos = []
opçoes = 512
while opçoes != 4:
    opçoes = int(input("O'que você deseja fazer? \n 1-Ver jogos \n 2-Comprar jogos \n 3-Reembolsar jogos \n 4-Sair"))
    if opçoes == 1:
        print(f"Jogos atuais: {Jogos}")
    elif opçoes == 2:
        adicionar = int(input(f"Quais jogos você deseja comprar? \n 1-Resident evil 4 remake \n 2-Call of duty black ops 6 \n 3-Sally face \n 4-Doki doki literature club: \n"))
        if adicionar == 1:
            Jogos.append(f"Resident evil 4 remake")
            print(f"Jogo adicionado a pasta Jogos. \n Jogos atuais: {Jogos}")
        elif adicionar == 2:
            Jogos.append(f"Call of duty black ops 6")
            print(f"Jogo adicionado a pasta Jogos. \n Jogos atuais: {Jogos}")
        elif adicionar == 3:
            Jogos.append(f"Sally face")
            print(f"Jogo adicionado a pasta Jogos. \n Jogos atuais: {Jogos}")
        else:
            Jogos.append(f"Doki doki literature club")
            print(f"Jogo adicionado a pasta Jogos. \n Jogos atuais: {Jogos}")
    elif opçoes == 3:
        reembolso = int(input(f"Quais jogos você deseja reembolsar? \n 1-Resident evil 4 remake \n 2-Call of duty black ops 6 \n 3-Sally face \n 4-Doki doki literature club: \n"))
        if reembolso == 1:
            Jogos.remove(f"Resident evil 4 remake")
            print(f"Jogo reembolsado da pasta Jogos. \n Jogos atuais: {Jogos}")
        elif reembolso == 2:
            Jogos.remove(f"Call of duty black ops 6")
            print(f"Jogo reembolsado da pasta Jogos. \n Jogos atuais: {Jogos}")
        elif reembolso == 3:
            Jogos.remove(f"Sally face")
            print(f"Jogo reembolsado da pasta Jogos. \n Jogos atuais: {Jogos}")
        else:
            Jogos.remove(f"Doki doki literature club")
            print(f"Jogo reembolsado da pasta Jogos. \n Jogos atuais: {Jogos}")
    else:
        print(f"mete o pé seu bosta")