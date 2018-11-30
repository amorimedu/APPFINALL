from tkinter import *
from Cars import Cars
from Control import Concessionaire

class Second(Toplevel):

    def __init__(self, concessionaire):

        self.concessionaire = concessionaire

        # Executar o metodo da classe mae
        super().__init__()
        # Ajustar tamanho
        self.geometry('300x300+200+200')
        # Colocar um titulo na janela
        self.title('Library Cars')

        self.model_var = StringVar()
        self.brand_var = StringVar()
        self.year_var = StringVar()
        self.price_var = StringVar()
        self.plate_var = StringVar()

        self.model = Entry(self, width = 10, textvariable = self.model_var).grid(row = 0, column = 1, padx = 1, pady = 1)
        self.brand = Entry(self, width = 10, textvariable = self.brand_var).grid(row = 1, column = 1, padx = 1, pady = 1)
        self.year = Entry(self, width = 10, textvariable = self.year_var).grid(row = 2, column = 1, padx = 1, pady = 1)
        self.price = Entry(self, width = 10, textvariable = self.price_var).grid(row = 3, column = 1, padx = 1, pady = 1)
        self.plate = Entry(self, width = 10, textvariable = self.plate_var).grid(row = 4, column = 1, padx = 1, pady = 1)


        self.lbl_model = Label(self, text = 'Model', width = 10).grid(row = 0, column = 0, padx = 1, pady = 1)
        self.lbl_brand = Label(self, text = 'Brand', width = 10).grid(row = 1, column = 0, padx = 1, pady = 1)
        self.lbl_year = Label(self, text = 'Year', width = 10).grid(row = 2, column = 0, padx = 1, pady = 1)
        self.lbl_price = Label(self, text = 'Price', width = 10).grid(row = 3, column = 0, padx = 1, pady = 1)
        self.lbl_plate = Label(self, text = 'Plate', width = 10).grid(row = 4, column = 0, padx = 1, pady = 1)


        self.btn_add = Button(self, text = 'Add', command = self.adc_car).grid(row = 5, column = 3, padx = 1, pady = 1)


    def adc_car(self):
         c = Cars(self.model_var.get(),self.brand_var.get(), self.year_var.get(), self.price_var.get(), self.price_var.get())

         self.concessionaire.concessionaire.add_car(c)


    def destroy(self):
        self.concessionaire.concessionaire.save_car()
        super().destroy()