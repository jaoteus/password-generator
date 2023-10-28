from tkinter import *
import random

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.entrys()
        root.mainloop()
    def tela(self):
        self.root.title("Gerador de Senha")
        self.root.configure(background='gray')
        self.root.geometry('380x250')
        self.root.resizable(False, False) # Não irá permitir expandir a tela

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='white')
        self.frame_1.place(relx=0.05, rely=0.4, relheight=0.52, relwidth=0.9)

    def botoes(self):
        self.botao_gerar = Button(text='Gerar senha', command=self.gerar_senha) ##### RESOLVIDO
        self.botao_gerar.place(relx=0.42, rely=0.1, relheight=0.1, relwidth= 0.2)

    def labels(self):
        self.lb_senha_gerada = Label(text='Senha gerada:',bg='gray',fg='white')
        self.lb_senha_gerada.place(relx=0.05,rely=0.3, relheight=0.07, relwidth=0.2)
    def entrys(self):
        self.saida_de_dados = Entry()
        
    def gerar_senha(self):
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.simbolos = ['!', '@', '#', '$', '%', '&']
        self.quantidade_de_algarismo = 26
        self.senha_gerada = ''
        while len(self.senha_gerada) < self.quantidade_de_algarismo:
            '''
            1 - Alfabeto
            2 - Número
            3 - Símbolo
            '''
            self.qual_o_proximo = random.randrange(1, 4)
            if self.qual_o_proximo == 1:
                self.algarismo_aleatorio = random.choice(self.letras)
                self.senha_gerada = self.senha_gerada + self.algarismo_aleatorio
            elif self.qual_o_proximo == 2:
                self.algarismo_aleatorio = random.choice(self.numeros)
                self.senha_gerada = self.senha_gerada + self.algarismo_aleatorio
            elif self.qual_o_proximo == 3:
                self.algarismo_aleatorio = random.choice(self.simbolos)
                self.senha_gerada = self.senha_gerada + self.algarismo_aleatorio
            print(self.senha_gerada)
        
Aplication()