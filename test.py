from tkinter import *
import subprocess


def main():
    root = Tk()

    root.geometry("500x500")
 
    #specify grid
    Grid.rowconfigure(root,0,weight=1)
    Grid.columnconfigure(root,0,weight=1)
    
    Grid.rowconfigure(root,1,weight=5)

    #games label
        #root, cant be changed how its connected to the window
        #text, what the label says
        #font, (*the font*, *the font size*)      
    label = Label(root, text='Games', font= ("Arial", 25))


    #all games you can choose
        # "gameName" : games application id 
    options = {"wolfQuest":431180, "Terraria": 105600}

    #list box. 
        #root, cant be changed how its connected to the window
        #font, (*the font*, *the font size*)
    optionBox = Listbox(root, font= ("Arial", 25))

    #adding all the options to the listbox
    for option in options:
        index = 0
        optionBox.insert(index, option)
        index += 1


    #what runs when the button is clicked
    def runGame():
        for i in optionBox.curselection():
            game = optionBox.get(i)   

        subprocess.run(f"start steam://run/{options[game]}", shell=True)

    #the countinue button
        #root, cant be changed how its connected to the window
        #text, what the button says
        #font, (*the font*, *the font size*)
        #command, the function that runs when the button is clicked
    button = Button(root, text= "continue", font= ("Arial", 25), command= runGame)

    #placing everything on the grid
    label.grid(row=0,column=0,sticky="NSEW")      
    optionBox.grid(row=1,column=0,sticky="NSEW")
    button.grid(row=2,column=0,sticky="NSEW")


    root.mainloop()




if __name__ == "__main__":
    main()
