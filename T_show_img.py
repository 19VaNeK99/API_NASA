from  tkinter import *
from PIL import Image


class show:
    def __init__(self):
        im = Image.open("img.png")
        im.show()
