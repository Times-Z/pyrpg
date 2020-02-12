# -*- coding: utf-8 -*-
import os
import time
from colorama import Fore, Back, Style
from settings.Settings import Settings
from classes.engine.Fightator import Fightator

# Only print & choice class
class Printator():

    classes = Settings.loadClass(Settings)

    def __init__(self):
        print(Fore.GREEN + "R" + Fore.YELLOW + "py")
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
              "The python game" + Fore.RESET)
        return True

    def loading(valmin, valmax, *mess):
        os.system('setterm -cursor off')
        begin = "["
        close = "]"
        bar = [
            " =     ",
            "  =    ",
            "   =   ",
            "    =  ",
            "     = ",
            "      =",
            "     = ",
            "    =  ",
            "   =   ",
            "  =    ",
        ]
        while valmin != valmax:
            print(
                Fore.WHITE
                + begin
                + Fore.RED
                + bar[valmin % len(bar)]
                + Fore.WHITE
                + close,
                end="\r",
            )
            time.sleep(0.1)
            valmin += 1
        else:
            if mess:
                print(Fore.GREEN + mess + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "                        " + Style.RESET_ALL)
        os.system('setterm -cursor on')
        return True

    def saveFound(self, save, *action):
        print("Save file found for :")
        print(
            save["charName"]
            + " "
            + self.classes[int(save["charClassId"])]["name"]
            + " level "
            + str(save["charLevel"])
        )
        if action:
            print("This action will be replace the save file with your actual game")
            action = input("Continue ? y/n ")
            if action == 'y':
                return True
            else: 
                return False
        else:
            print("Continue with this game ? y/n")
            return True

    def saved():
        Settings.Addspace(Settings, 20)
        print(Fore.GREEN + "Game saved" + Fore.RESET)
        Settings.Addspace(Settings, 2)
        return True

    def choseName():
        Settings.Addspace(Settings, 2)
        print("- New game -")
        Settings.Addspace(Settings, 2)
        print("Choose your name : ")
        return True

    def confirm(param, string):
        confirm = input(
            'Do you really want "'
            + Fore.RED
            + "%s" % param
            + Fore.RESET
            + '"'
            + " %s ? y/n " % string
        )
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            return False

    def classChose(i, classes):
        print(
            str(i)
            + " -> "
            + Fore.GREEN
            + classes[i]["name"]
            + " - Special spell : "
            + classes[i]["spe"]["name"]
            + Fore.RESET
        )
        return True

    def showInformations():
        Settings.Addspace(Settings, 10)
        return True

    def showMainTitle(name, me, level):
        print('-------------------------------------------')
        print('|                                         |')
        print('| RPY   --   THE PYTHON ROLE PLAYING GAME |')
        print('|                                         |')
        print('-------------------------------------------')
        Settings.Addspace(Settings, 2)
        print('Name  : ' + name)
        print('Class : ' + me.name)
        print('Level : ' + str(level))
        Settings.Addspace(Settings, 2)
        return True
    
    def showMainMenu(self, *space):
        if space:
            Settings.Addspace(Settings, 20)
        print("------------")
        print("| MAIN MENU |")
        print("------------")
        Settings.Addspace(Settings, 2)
        for i in range(len(Settings.mainMenu())):
            print(str(i) + " -> " + Settings.mainMenu()[i])
        Settings.Addspace(Settings, 2)

        action = input("> ")

        if action == "0":
            return 0
        elif action == "1":
            return 1
        elif action == "2":
            return 2
        elif action == "3":
            return 3
        elif action == "4":
            exit
        else:
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)

    def showMenuOption():
        Settings.Addspace(Settings, 20)
        print("-----------")
        print("| OPTIONS |")
        print("-----------")
        options = Settings.options()
        for i in range(len(options)):
            print(str(i) + " -> " + options[i])
        action = input("> ")

        if action == "0":
            return 0
        elif action == "1":
            return 99

    def removeSave():
        print(Fore.RED + "/!\ " + Fore.RESET + " WARNING " + Fore.RED + " /!\ ")
        print(
            Fore.RESET
            + "This action will be "
            + Fore.RED
            + "remove"
            + Fore.RESET
            + " the save file"
        )
        confirm = input("Are you sure ? y/n ")
        if confirm == 'y':
            return True
        else:
            return False

    def success(string):
        print(string)
        return True