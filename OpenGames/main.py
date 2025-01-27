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


    # steam, epic games, battlenet, riot, minecraft bedrock
        #minecraft 

    #all games you can choose
        # "gameName" : *games url* (found in properties) 
    steam = {
        "Halo": "steam://rungameid/1240440",
        "BrawlHalla": "steam://rungameid/291550",
        "Counter Strike 2": "steam://rungameid/730",
        "Apex Legends": "steam://rungameid/1172470"
        }
        #"gameName" : *games url* (remove "&silent=true") 
    epicGames = {
        "Rocket League": 'com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch',
        "Fortnite": "com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch"
    }
    #battle net game id is found diffrently.
    battleNet = {
        "Overwatch": ["G:\Games\Overwatch\_retail_\Overwatch.exe"],
        "Hearthstone": ["G:\Games\Hearthstone\Hearthstone.exe"]
    }
    # "gameName": *desktops shortcuts target* (found in properties) (seperate and put into a list)
    riot = {
        "Valorant": ["G:\Games\Riot Games\Riot Client\RiotClientServices.exe", '--launch-product=valorant', '--launch-patchline=live'],
        "League of Legends": ["G:\Games\Riot Games\Riot Client\RiotClientServices.exe", '--launch-product=league_of_legends', '--launch-patchline=live']
    }

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

        for engine in options:
            if game in engine:
                platform = engine
                break

        #actual code to open game
        if game in steam or game in epicGames:
            subprocess.run(f"start {platform[game]}", shell=True)
        elif game in battleNet or game in riot:
            subprocess.run(platform[game], shell=True)

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