#!/usr/bin/python3
#coding: utf-8
import os
import random
import sys
import time
import json
from colorama import Fore, Back, Style

# My classes
from settings.Settings import Settings


class Game():

    charName = None
    classes = Settings.loadClass(Settings)
    charClass = None
    charLevel = 0

    def __init__(self):
        print(Fore.GREEN+"R"+Fore.YELLOW+"py")
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"The python game"+Fore.RESET)
        self.loading(0, 20, "")
        self.getSave(self)

    def getSave(self):
        if os.path.isfile('save/save.json'):
            save = Settings.loadSave()
            self.charName = save[0]['charName']
            self.charClass = save[0]['charClass']
            self.charLevel = save[0]['charLevel']
            self.showInformation(self)
        else:
            self.choseName(self)

    def loading(valmin, valmax, mess):
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
            print(Fore.WHITE+begin+Fore.RED +
                  bar[valmin % len(bar)]+Fore.WHITE+close, end="\r")
            time.sleep(.1)
            valmin += 1
        else:
            if mess != '':
                print(Fore.GREEN + mess + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "                        " + Style.RESET_ALL)

    def confirm(self, param, string):
        confirm = input("Do you really want \""+Fore.RED+"%s" %
                        param + Fore.RESET + "\"" + " %s ? y/n " % string)
        if confirm == 'y':
            return True
        elif confirm == 'n':
            return False
        else:
            return False

    def choseName(self):
        print("Choose your name : ")
        name = input("> ")
        confirm = self.confirm(self, name, "as name")
        if confirm == True:
            self.charName = name
            print('Your name is ' + Fore.GREEN + '%s' %
                  self.charName + Fore.RESET)
            self.choseClasse(self)
        else:
            self.choseName(self)

    def choseClasse(self):
        Settings.Addspace(Settings, 4)
        for i in range(len(self.classes)):
            print(str(i) + ' -> ' + Fore.GREEN +
                  self.classes[i]['name'] + ' - Special spell : ' + self.classes[i]['spe'] + Fore.RESET)
        Settings.Addspace(Settings, 2)
        print("Choose your class : ")
        classChose = input("> ")

        if classChose == '0' or classChose == '1' or classChose == '2' or classChose == '3' or classChose == '4':
            confirm = self.confirm(
                self, self.classes[int(classChose)]['name'], "")
            if confirm == True:
                self.charClass = classChose
                self.showInformation(self)
            else:
                self.choseClasse(self)
        else:
            self.choseClasse(self)

    def showInformation(self):
        Settings.Addspace(Settings, 100)
        Settings.showMainTitle(Settings, self.charName,
                               self.charClass, self.charLevel)
        self.showMainMenu(self)

    def showMainMenu(self):
        print('------------')
        print('| MAIN MENU |')
        print('------------')
        Settings.Addspace(Settings, 2)
        for i in range(len(Settings.mainMenu())):
            print(str(i) + ' -> ' + Settings.mainMenu()[i])
        Settings.Addspace(Settings, 2)
        action = input("> ")

        if action == '0':
            print("QUICK BATTLE")
        elif action == '1':
            print("CAMPAGNE")
        elif action == '2':
            self.showOptionMenu(self)
        elif action == '3':
            print("SAVE")
        elif action == '4':
            exit
        else:
            self.showMainMenu(self)

    def showOptionMenu(self):
        Settings.Addspace(Settings, 100)
        print('-----------')
        print('| OPTIONS |')
        print('-----------')
        options = Settings.options()
        for i in range(len(options)):
            print(str(i) + ' -> ' + options[i])
        action = input('> ')

        if action == '0':
            print(Fore.RED+"/!\ "+Fore.RESET+" WARNING "+Fore.RED+" /!\ ")
            print(Fore.RESET+"This action will be "+Fore.RED+"remove"+Fore.RESET+" the save file")
            confirm = input("Are you sure ? y/n ")
            if confirm == 'y':
                print("DELETE")
            else:
                print("Not delete")
        elif action == '1':
            Settings.Addspace(Settings, 100)
            return self.showMainMenu(self)


if __name__ == "__main__":
    try:
        Game.__init__(Game)
    except KeyboardInterrupt:
        exit
