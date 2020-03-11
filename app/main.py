#!/usr/bin/python3
# -*- coding: utf-8 -*-

# My classes
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from classes.engine.Fightator import Fightator
from classes.engine.Lantator import Lantator
from classes.engine.Apitator import Apitator

class Game():
    """
        Game class
    """

    def __init__(self):
        self.apitator = Apitator()
        self.classes = self.apitator.getClass()
        self.apitator.login()
        printator = Printator()
        printator.resolution(60,40)
        # Printator.resolution(60, 40)
        # Goes wrong with some console : include kde konsole, fix exist ?
        # Settings.resize()
        Printator.init(Printator, self.classes)
        Printator.loading(0, 20)
        if Saveator.init(Saveator) == True:
            self.showInformation()
        else:
            Saveator.choseName(Saveator)
            Saveator.choseClass(Saveator)
            self.showInformation()

    def showInformation(self):
        Printator.showInformations()
        Printator.showMainTitle(
            Saveator.charName, Saveator.me, Saveator.charLevel)
        Saveator.updateStats(Saveator)
        self.mainMenu()

    def mainMenu(self, jump = False):
        if jump == False:
            choice = Printator.showMainMenu(Printator)
        else:
            choice = jump
        if choice == 0:
            Fightator.quickBattle(Fightator, Saveator.me)
            self.mainMenu()
        elif choice == 1:
            lan = Lantator.init(Lantator)
            if lan == False:
                self.mainMenu(1)
            else:
                self.mainMenu()
        elif choice == 2:
            option = Printator.showMenuOption()
            if option == 0:
                Saveator.removeSave()
            else:
                self.mainMenu()
        elif choice == 3:
            save = Saveator.save(Saveator)
            if save != True:
                self.mainMenu()
        elif choice == 10:
            self.mainMenu()


if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        exit
