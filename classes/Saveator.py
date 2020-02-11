# -*- coding: utf-8 -*-
import os
from classes.Printator import Printator
from settings.Settings import Settings
from classes.char.Class import Rogue, Warrior, Gunner, Developer, Admin
from colorama import Fore, Style, Back


class Saveator():

    classes = Settings.loadClass(Settings)

    def __init__(self):
        if os.path.isfile("save/save.json"):
            save = Settings.loadSave()
            Printator.saveFound(Printator, save)
            loadsave = input("> ")
            if loadsave == "y":
                self.charName = save["charName"]
                self.charClass = save["charClassId"]
                self.charLevel = save["charLevel"]
                self.charExp = save["charExp"]
                self.score = save["score"]
                if self.charClass == 0:
                    self.me = Rogue()
                elif self.charClass == 1:
                    self.me = Warrior()
                elif self.charClass == 2:
                    self.me = Gunner()
                elif self.charClass == 3:
                    self.me = Developer()
                elif self.charClass == 4:
                    self.me = Admin()
                return True
            else:
                return False
        else:
            return False

    def choseName(self):
        Printator.choseName()
        name = input("> ")
        confirm = Printator.confirm(name, "as name")
        if confirm == True:
            self.charName = name
            print("Your name is " + Fore.GREEN + "%s" %
                  self.charName + Fore.RESET)
            self.choseClass(self)
        else:
            self.choseName()

    def choseClass(self):
        Settings.Addspace(Settings, 4)
        for i in range(len(self.classes)):
            Printator.classChose(i, self.classes)
        Settings.Addspace(Settings, 2)
        print("Choose your class : ")
        classChose = input("> ")
        # HERE
         if (
              classChose == "0"
              or classChose == "1"
              or classChose == "2"
              or classChose == "3"
              or classChose == "4"
              ):
              confirm = Printator.confirm(
                  self.classes[int(classChose)]["name"], "")
               if confirm == True:
                    self.charClass = int(classChose)
                    if self.charClass == 0:
                        self.me = Rogue()
                    elif self.charClass == 1:
                        self.me = Warrior()
                    elif self.charClass == 2:
                        self.me = Gunner()
                    elif self.charClass == 3:
                        self.me = Developer()
                    elif self.charClass == 4:
                        self.me = Admin()
                    self.showInformation(self)
                else:
                    self.choseClasse(self)
        else:
            self.choseClasse(self)
