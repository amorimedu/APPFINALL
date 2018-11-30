from tkinter import *
from Second_Window import Second


# Classe Janela_Principal
class Main_Window(Tk):
    # Metodo construtor
    def __init__(self, concessionaire):

        self.concessionaire = concessionaire

        # Executar o metodo da classe mae
        super().__init__()
        # Ajustar tamanho
        self.geometry('300x300+500+500')
        # Colocar um titulo na janela
        self.title('Library Cars')

        self.lbl = Label(self, text = 'Welcome!', font = 'Verdana 25 bold').grid(row = 0, column = 1, padx = 1, pady = 1)
        self.btn = Button(self, text = 'Exit', command = self.destroy).grid(row=1, column=1, padx = 1, pady = 1)

        self.btn1 = Button(self, text = 'Add Cars', command = self.second_window).grid(row = 1, column = 2, padx = 1, pady = 1)


    def second_window(self):

        Second(self.concessionaire)

