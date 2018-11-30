from MainWindow import Main_Window
from Control import Concessionaire

class Control():

    def __init__(self):

        self.concessionaire = Concessionaire('Library Cars')
        self.wd = Main_Window(self)
        self.wd.mainloop()