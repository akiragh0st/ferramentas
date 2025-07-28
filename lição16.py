taxa_cotaçãoEUA = 1
taxa_cotaçãoBR = 5.56
Nome = input(f"Qual seu nome? ")
opcoes = int(input(f"{Nome}, Oque você deseja fazer? \n 1- Ver a cotação \n 2- Converter dolar em real \n 3- Converter real em dolar \n Digite:"))
if opcoes == 1:
    print(f"{Nome}, A cada 1 Dolar é 5.56 Reais")
elif opcoes == 2:
    convertor_em_dolar_real= float(input(f"Quantos dolares você deseja converter?"))
    conversão_real = (convertor_em_dolar_real * taxa_cotaçãoBR )
    print(f"o valor convertido será {conversão_real}")
elif opcoes == 3:
    convertor_em_real_dolar= float(input(f"Quantos reais você deseja converter?"))
    conversão_dolar = (convertor_em_real_dolar / taxa_cotaçãoBR )
    print(f"o valor convertido será {conversão_dolar}")


    


