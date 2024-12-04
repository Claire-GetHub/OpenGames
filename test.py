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


    # steam, epic games, battlenet, riot
    #all games you can choose
        # "gameName" : games application id 
    steam = {"wolfQuest":431180, "Terraria": 105600}
    epicGames = {}
    battleNet = {}
    riot = {}

    options = [steam, epicGames, battleNet, riot]

    #list box. 
        #root, cant be changed how its connected to the window
        #font, (*the font*, *the font size*)
    optionBox = Listbox(root, font= ("Arial", 25))

    #adding all the options to the listbox
    for platform in options:
        index = 0
        for option in platform:
            optionBox.insert(index, option)
            index += 1


    #what runs when the button is clicked
    def runGame():
        for i in optionBox.curselection():
            game = optionBox.get(i)   

        #if game in steam ect.
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

    #full screen without exit buttons
    #root.attributes("-fullscreen", True)

    root.mainloop()




if __name__ == "__main__":
    main()
