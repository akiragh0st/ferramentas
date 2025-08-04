nome = input("Qual seu nome?")
try:
    peso = float(input("Qual seu peso?"))
    altura = float(input("Qual sua altura?"))
    if altura <= 0 or peso <= 0:
        print("Altura e peso devem ser maiores que zero.")
    else:
        IMC = peso / (altura * altura)
        print(f"Seu IMC é: {IMC:.2f}")
        print(IMC)
        if IMC <= 18.5:
            print(f"{nome} está abaixo do peso!")
        elif IMC <= 24.9:
            print(f"{nome} está no peso normal")
        elif IMC <= 29.9:
            print(f"{nome} está com Sobrepeso")
        elif IMC <= 34.9:
            print(f"{nome} está com obesidade grau 1")
        elif IMC <= 39.9:
            print(f"{nome} está com obesidade grau 2")
        else:
            print(f"{nome} está com obesidade grau 3(mórbida)")
except ValueError:
    print(f"Peso ou altura escrito errado, por favor, refaça")