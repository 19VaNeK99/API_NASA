from tkinter import *


class show_astr():
    def __init__(self):
        self.wind_list = Tk()
        self.wind_list.geometry("200x500")
        self.wind_list.title("Список астеройдов")

    def show(self, l_astr):
        list_astr = Label(self.wind_list, text=l_astr)
        list_astr.grid(column=0, row=0)
        #list_astr.configure(text = l_astr)



