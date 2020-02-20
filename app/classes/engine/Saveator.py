# -*- coding: utf-8 -*-
import os
import json
from classes.engine.Printator import Printator
from settings.Settings import Settings
from classes.char.Character import Character
from colorama import Fore, Style, Back


class Saveator():

    classes = Settings.loadClass(Settings)
    me = False
    charName = False
    charLevel = 1
    charExp = False
    charClassId = False
    charClass = False
    score = 0

    def init(self):
        if os.path.isfile("save/save.json"):
            save = Settings.loadSave()
            Printator.saveFound(Printator, save)
            loadsave = input("> ")
            if loadsave == "y":
                self.charName = save["charName"]
                self.charClassId = save["charClassId"]
                self.charClass = save["charClass"]
                self.charLevel = save["charLevel"]
                self.charExp = save["charExp"]
                self.score = save["score"]
                self.me = Character(self.charClassId)
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
            return True
        else:
            self.choseName(self)

    def choseClass(self):
        Settings.Addspace(Settings, 4)
        for i in range(len(self.classes)):
            Printator.classChose(i, self.classes)
        Settings.Addspace(Settings, 2)
        print("Choose your class : ")
        classChose = input("> ")
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
                self.me = Character(self.charClass)
                return True
            else:
                self.choseClass(self)
        else:
            self.choseClass(self)

    def updateStats(self):
        with open('/app/settings/levels.json') as jsonLevel:
            levels = json.load(jsonLevel)
        key = self.charLevel - 1
        addHp = levels[key]['hp']
        addAtk = levels[key]['atk']
        self.me.hp += int(addHp)
        self.me.maxHp += int(addHp)
        self.me.atk += int(addAtk)
        return True

    def save(self):
        if os.path.exists("save/save.json"):
            save = Settings.loadSave()
            action = Printator.saveFound(Printator, save, 1)
            if action == True:
                os.remove("save/save.json")
                self.save(self)
            else:
                Settings.Addspace(Settings, 2)
                Printator.success(Fore.RED + 'Aborted' + Fore.RESET)
                Settings.Addspace(Settings, 2)
                return False
        else:
            file = open("/app/save/save.json", "a")
            json_data = {
                "charName": "{0}".format(self.charName),
                "charClassId": self.charClass,
                "charClass": self.classes[self.charClass],
                "charLevel": self.charLevel,
                "charExp": self.charExp,
                "score": self.score,
            }
            json.dump(json_data, fp=file, indent=4, sort_keys=False)
            file.close()
            Printator.saved()
            return False

    def removeSave():
        remove = Printator.removeSave()
        print(remove)
        if remove == True:
            if os.path.exists("save/save.json"):
                os.remove("save/save.json")
                Printator.showMainMenu(Printator)
                Printator.success('removing save file success')
            else:
                Printator.showMenuOption()
                Printator.success('No save file exist')
        else:
            Printator.showMainMenu(Printator)

    def checkLevel(level, xp):
        with open('/app/settings/levels.json') as jsonLevel:
            levels = json.load(jsonLevel)
        key = level - 1
        xpNeed = levels[key]['toUp']
        if xp >= xpNeed:
            return True
        else:
            return False
