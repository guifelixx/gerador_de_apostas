import random
from tkinter import *


#Função:
def aposta():
    numeros_sorte = random.sample(range(1, 61), 6)
    texto_sorteio["text"] = "    ".join(map(str, numeros_sorte))

#Configs janela Tkinter
janela = Tk()
janela.title("Sorteio para Mega-sena")
janela.geometry("500x300")

#Configuração de redimensionamento proporcional
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(3, weight=1)  # Adiciona uma linha extra para empurrar o botão para cima

#Texto que orienta ao usuario oque ele deve fazer + Configs:
texto_orientacao = Label(janela, text="Clique no botão para gerar seus números da Mega-sena:")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

#Botão que executa a função:
botao = Button(janela, text="Sortear números", command=aposta)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_sorteio =  Label(janela, text="", font="Impact")
texto_sorteio.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

