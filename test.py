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
        # "gameName" : *games url* (found by right clicking application > properties) 
    steam = {
        "wolfQuest": "steam://rungameid/431180",
        "Terraria": "steam://rungameid/105600"
        }
    epicGames = {
        "Rocket League": '"com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"'
    }
    #battle net game id is found diffrently.
    battleNet = {
        "Overwatch": '"C:\program files (x86)\overwatch\_retail_\overwatch.exe"'
    }
    riot = {}

    options = [steam, epicGames, battleNet, riot]

    #list box. 
        #root, cant be changed how its connected to the window
        #font, (*the font*, *the font size*)
    optionBox = Listbox(root, font= ("Arial", 25))

    #adding all the options to the listbox
    index = 0
    for platform in options:        
        for option in platform:
            optionBox.insert(index, option)
            index += 1

    #has to be here because it uses option box and all the platforms lists
    def runGame():
        for i in optionBox.curselection():
            game = optionBox.get(i)   


        if game in steam.keys():
            platform = steam
        elif game in epicGames.keys():
            platform = epicGames
        elif game in battleNet.keys():
            platform = battleNet
        elif game in riot:
            platform = riot

        #actual code to open game
        subprocess.run(fr"start {platform[game]}", shell=True)

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

    #what runs when the button is clicked


if __name__ == "__main__":
    pass #main()

game = '"com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"'
#subprocess.Popen(["explorer", game], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

subprocess.run('start "com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"', shell=True)
