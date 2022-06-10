from tkinter import *

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)
file = Menu(mymenu)
mymenu.add_cascade(label='File',menu=file)
root.mainloop()