LISTA_COMPRAS = []
opçoes = 432
while opçoes != 5:
    opçoes = int(input(f"1- Fazer lista de comprar \n2- Colocar item na lista \n3- Tirar o item da lista \n4- Limpar toda a lista \n5- Jogar lista fora \n"))
    if opçoes == 1:
        fazer_lista = int(input(f"1-Tomate \n2-Molho de tomate \n3-Salgadinho de tomate \n4-Sal \n"))
        if fazer_lista == 1:
            LISTA_COMPRAS.append(f"Tomate")
            print(LISTA_COMPRAS)
        elif fazer_lista == 2:
            LISTA_COMPRAS.append(f"Molho de tomate")
            print(LISTA_COMPRAS)
        elif fazer_lista == 3:
            LISTA_COMPRAS.append(f"Salgadinho de tomate")
            print(LISTA_COMPRAS) 
        else:
            LISTA_COMPRAS.append(f"Sal")
            print(LISTA_COMPRAS)       
    elif opçoes == 2:
        fazer_lista2 = int(input(f"1-Sal grosso \n2-Açucar \n"))
        if fazer_lista2 == 1:
            LISTA_COMPRAS.append(f"Sal grosso")
            print(LISTA_COMPRAS)
        else:
            LISTA_COMPRAS.append(f"Açucar")
            print(LISTA_COMPRAS)
    elif opçoes == 3:
        tirar_da_lista = int(input(f"Tirar \n1-Tomate \n2-Molho de tomate \n3-Salgadinho de tomate \n4-Sal \n5-Sal grosso \n6-Açucar\n"))
        if tirar_da_lista == 1:
            LISTA_COMPRAS.remove(f"Tomate")
            print(LISTA_COMPRAS)
        elif tirar_da_lista == 2:
            LISTA_COMPRAS.remove(f"Molho de tomate")
            print(LISTA_COMPRAS)
        elif tirar_da_lista == 3:
            LISTA_COMPRAS.remove(f"Salgadinho de tomate")
            print(LISTA_COMPRAS)
        elif tirar_da_lista == 4:
            LISTA_COMPRAS.remove(f"Sal")
            print(LISTA_COMPRAS)
        elif tirar_da_lista == 5:
            LISTA_COMPRAS.remove(f"Sal grosso")
            print(LISTA_COMPRAS)
        else:
            LISTA_COMPRAS.remove(f"Açucar")
            print(LISTA_COMPRAS)
    elif opçoes == 4:
        LISTA_COMPRAS.clear()
        print(LISTA_COMPRAS)
    else:
        print("Jogou a lista no lixo com uma enterrada, THE LEBRON JAMES")