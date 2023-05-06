import os
from time import sleep


command = ""
choiceOutcome = 0

def startMenu(GameTitle = "Title", GameAuthor = "Author", hasOptions = False):
    """
    The TextAdventureSYS start menu. Must be called otherwise the start menu won't be used.
    """
    typewriter(GameTitle + " by " + GameAuthor, 0.1)
    typewriter("Type start to enter the adventure", 0.1)
    typewriter("Type help for commands", 0.1)
    if hasOptions == True:
        typewriter("Type options to change your settings", 0.1)
    typewriter("Made with TextAdventureSYS by Ender", 0.1)
    command = input(">>")
    if command == "start":
        typewriter("Starting the adventure", 0.5)
        os.system("cls")
    if command == "help":
        typewriter("Help currently unaveable", 0.05)
        os.system("cls")
        startMenu(GameTitle, GameAuthor, hasOptions)

def typewriter(text = "Defualt Text", delay = 300, endLine = True):
    """
    Prints {text} with a delay of {delay} between each character
    """
    i = 0
    while i < len(text):
        print(text[i], end=text[i], flush=True)
        i += 1
        sleep(delay/1000)
    if endLine == True:
        print("")

def wait(delay = 1000):
    """
    Waits fot {delay} milliseconds
    """
    sleep(delay/1000)

def choice(text: str, choices: list):
    """
    Gives the player a choice.
    """
    print(choices)
    command = input(">> ")
    return choices.index(command) + 1
        
def main():
    typewriter("This is a module and is not meant to be ran directly, please import it first.", 50)
    wait(2000)

if __name__ == '__main__':
    main()