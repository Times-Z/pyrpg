# -*- coding: utf-8 -*-
import os
import json
from classes.char.Character import Character
from colorama import Fore, Style, Back


class Saveator:

    def __init__(self, printator, classes, api):
        self.me = False
        self.charName = False
        self.charLevel = 1
        self.charExp = 0
        self.charClassId = 0
        self.charClass = False
        self.score = 0
        self.printator = printator
        self.classes = classes
        self.apitator = api

    def loadSave(self):
        data = self.apitator.getSave()
        if data != False:
            save = json.loads(str(data['save']['save_json']))
            self.printator.saveFound(save)
            loadsave = input("> ")
            if loadsave == "y":
                self.charName = save["charName"]
                self.charClassId = save["charClassId"]
                self.charClass = save["charClass"]
                self.charLevel = save["charLevel"]
                self.charExp = save["charExp"]
                self.score = save["score"]
                self.me = Character(self.apitator, self.charClassId)
                return True
            else:
                return False
        else:
            return False

    def choseName(self):
        self.printator.choseName()
        name = input("> ")
        confirm = self.printator.confirm(name, "as name")
        if confirm == True:
            self.charName = name
            self.printator.success(
                "Your name is " + Fore.GREEN + "{name}".format(name=self.charName))
            return True
        else:
            self.choseName()

    def choseClass(self):
        self.printator.addSpace(4)
        for i in range(len(self.classes)):
            self.printator.classChose(i, self.classes)
        self.printator.addSpace(2)
        self.printator.success('Choose your class : ')
        classChose = input("> ")
        if (
            classChose == "0"
            or classChose == "1"
            or classChose == "2"
            or classChose == "3"
            or classChose == "4"
        ):
            confirm = self.printator.confirm(
                self.classes[int(classChose)]["name"], "")
            if confirm == True:
                self.charClassId = int(classChose)
                self.me = Character(self.apitator, self.charClassId)
                return True
            else:
                self.choseClass()
        else:
            self.choseClass()

    def updateStats(self):
        levels = json.loads(self.apitator.getLevels())
        key = self.charLevel - 1
        addHp = levels[key]['hp']
        addAtk = levels[key]['atk']
        self.me.hp += int(addHp)
        self.me.maxHp += int(addHp)
        self.me.atk += int(addAtk)
        return True

    def save(self):
        data = self.apitator.getSave()
        if data != False:
            save = json.loads(str(data['save']['save_json']))
            action = self.printator.saveFound(save, 1)
            if action == True:
                rm = self.apitator.removeSave()
                if rm == True:
                    self.save()
                else:
                    self.printator.success(Fore.RED + 'Error on delete save')
            else:
                self.printator.addSpace(2)
                self.printator.success(Fore.RED + 'Aborted')
                self.printator.addSpace(2)
                return False
        else:
            json_data = {
                "charName": "{name}".format(name=self.charName),
                "charClassId": self.charClassId,
                "charClass": self.classes[self.charClassId],
                "charLevel": self.charLevel,
                "charExp": self.charExp,
                "score": self.score,
            }
            data = json.dumps(json_data)
            saved = self.apitator.save(data)
            if saved == True:
                self.printator.saved()
            else:
                self.printator.success(str(saved))
            return False

    def removeSave(self):
        remove = self.printator.removeSave()
        if remove == True:
            data = self.apitator.getSave()
            if data != False:
                rm = self.apitator.removeSave()
                if rm == True:
                    self.printator.success(
                        Fore.GREEN + 'removing save file success')
                    return True
                else:
                    self.printator.success(Fore.RED + 'An error encountered')
                self.printator.showMainMenu()
            else:
                self.printator.success('No save file exist')
                self.printator.showMenuOption()
        else:
            self.printator.showMainMenu()

    def checkLevel(self, level, xp):
        levels = json.loads(self.apitator.getLevels())
        key = level - 1
        xpNeed = levels[key]['toUp']
        if xp >= xpNeed:
            return True
        else:
            return False
