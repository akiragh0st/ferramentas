def Calcular_imc():
    nome = input("Qual seu nome?")
    peso = float(input("Qual sua peso?"))
    altura = float(input("Qual sua altura?"))
    IMC = peso / (altura*altura)
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
Calcular_imc()