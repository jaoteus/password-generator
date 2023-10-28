from tkinter import *

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botoes()
        root.mainloop()
    def tela(self):
        self.root.title("Gerador de Senha")
        self.root.configure(background='gray')
        self.root.geometry('380x250')
        self.root.resizable(False, False) # Não irá permitir expandir a tela
    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='white')
        self.frame_1.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.8)
    def botoes(self):
        self.botaoGerar = Button(text='Gerar')
        self.botaoGerar.place(relx=0.45, rely=0.1, relheight=0.1, relwidth= 0.1)

    def gerar_senha(self):
        pass

Aplication()