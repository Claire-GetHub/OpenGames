from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("OpenSteam")

root.geometry("300x300")
options = ["game1", "game2"]
optionBox = Listbox(root, height=10, width= 15)
#for future
#root.attributes('-fullscreen',True)

root.mainloop()

