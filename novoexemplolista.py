LISTA = ["maça", "banana", "laranja"]

def atualizar_lista():
    antigo = input(f"item que deseja substituir: ")
    if antigo in LISTA:
        novo = input("novo item:")
        index = LISTA.index(antigo)
        LISTA[index] = novo
        print("Lista atualizada:", LISTA)
    else:
        print(f"{antigo} não está na lista.")
atualizar_lista()