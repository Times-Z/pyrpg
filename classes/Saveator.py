# -*- coding: utf-8 -*-
import os
from classes.Printator import Printator
from settings.Settings import Settings
from classes.char.Class import Rogue, Warrior, Gunner, Developer, Admin


class Saveator():
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
