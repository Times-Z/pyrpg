#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random
import sys
import time
import json
import random
from colorama import Fore, Back, Style

# My classes
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from classes.engine.Fightator import Fightator
from settings.Settings import Settings
from classes.char.Character import Character


class Game():

    classes = Settings.loadClass(Settings)

    def __init__(self):
        # Goes wrong with some console : include kde konsole, fix exist ?
        # Settings.resize()
        Printator.__init__(Printator)
        Printator.loading(0, 20)
        if Saveator.init(Saveator) == True:
            self.showInformation(self)
        else:
            Saveator.choseName(Saveator)
            Saveator.choseClass(Saveator)
            self.showInformation(self)

    def showInformation(self):
        Printator.showInformations()
        Printator.showMainTitle(
            Saveator.charName, Saveator.me, Saveator.charLevel)
        Saveator.updateStats(Saveator)
        self.mainMenu(self)

    def mainMenu(self):
        choice = Printator.showMainMenu(Printator)
        if choice == 0:
            Fightator.quickBattle(Fightator, Saveator.me)
            self.mainMenu(self)
        elif choice == 1:
            print('CAMPAGN')
        elif choice == 2:
            option = Printator.showMenuOption()
            if option == 0:
                Saveator.removeSave()
            else:
                self.mainMenu(self)
        elif choice == 3:
            save = Saveator.save(Saveator)
            if save != True:
                self.mainMenu(self)
        elif choice == 10:
            self.mainMenu(self)


if __name__ == "__main__":
    try:
        Game.__init__(Game)
    except KeyboardInterrupt:
        exit
