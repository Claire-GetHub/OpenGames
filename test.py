from tkinter import *

def main3():
    root = Tk()

    root.geometry("500x500")
 
# Specify Grid
    Grid.rowconfigure(root,0,weight=1)
    Grid.columnconfigure(root,0,weight=1)
    
    Grid.rowconfigure(root,1,weight=5)

    label = Label(root, text='Games', font= ("Arial", 25))

    options = ["game1", "game2"]
    optionBox = Listbox(root, font= ("Arial", 25))
    for option in options:
        optionBox.insert(options.index(option) + 1, option)
    
    button = Button(root, text= "continue", font= ("Arial", 25))

    label.grid(row=0,column=0,sticky="NSEW")      
    optionBox.grid(row=1,column=0,sticky="NSEW")
    button.grid(row=2,column=0,sticky="NSEW")


    root.mainloop()




if __name__ == "__main__":
    main3()
