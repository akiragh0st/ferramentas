nome = str(input(f"Qual seu nome parça?"))
temperatura = float(input(f"{nome}, qual é temperatura?"))
if temperatura >= 20 and temperatura <=40:
    print(f"tá calor {nome}")
elif temperatura >= 6 and temperatura <=19:
    print(f"Tá frio pacas {nome}")
elif temperatura >= 0 and temperatura <=5:
    print(f"{nome}, Tá nevando!")
else:
    print(f"{nome}, nois morreu")