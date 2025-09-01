import os
import flet as ft

def main(page: ft.Page):
    def criar_pasta(e):
        nome_pasta = text_entrada.value
        os.mkdir(nome_pasta)
        resultado.value = f"Pasta {nome_pasta} criada!"
        resultado.color = "GREEN"
        page.update
    
    def remover_pasta(e):
        nome_pasta = text_entrada.value
        os.rmdir(nome_pasta)
        resultado.value = f"Pasta {nome_pasta} removida!"
        resultado.color = "RED"
        page.update  
    botão_criar_pasta = ft.ElevatedButton("Criar pasta", on_click= criar_pasta, color="WHITE", bgcolor= "GREEN", width= 300)
    text_entrada = ft.TextField(label = "Escreva algo")
    botão_apagar_pasta = ft.ElevatedButton("Apagar pasta", on_click= remover_pasta, color="WHITE", bgcolor= "RED", width= 300)
    resultado = ft.Text("", size = 25, color= "GREEN")
    page.add(ft.Row([text_entrada], alignment = "center"),
             ft.Row([botão_criar_pasta], alignment = "center"),
             ft.Row([botão_apagar_pasta], alignment = "center"),
             ft.Row([resultado], alignment = "center"))
ft.app(target = main)






# os.mkdir(f"Projeto")
# print(f"Pasta criada!")
# open("Projeto/matematica.txt", "w").close()
# open("Projeto/portugues.txt", "w").close()
# open("Projeto/ciencias.txt", "w").close()
# Projeto_listt = os.listdir("Projeto")
# for item in Projeto_listt:
#   print(item)
# os.rename("Projeto/portugues.txt", "Projeto/historia.txt")
# if os.path.exists("Projeto/matematica.txt"):
#     os.remove("Projeto/matematica.txt")
#     print(f"Arquivo apagado")
# else:
#     print(f"Arquivo não existente")