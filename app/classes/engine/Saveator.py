# -*- coding: utf-8 -*-
import os
import json
from classes.engine.Printator import Printator
from settings.Settings import Settings
from classes.char.Character import Character
from classes.engine.Configator import Configator
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
        data = Configator.getSave(Configator)
        if data != False:
            save = json.loads(str(data['save']['save_json']))
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
        data = Configator.getSave(Configator)
        if data != False:
            save = json.loads(str(data['save']['save_json']))
            action = Printator.saveFound(Printator, save, 1)
            if action == True:
                rm = Configator.removeSave(Configator)
                if rm == True:
                    self.save(self)
                else:
                    Printator.success(Fore.RED + 'Error on delete save')
            else:
                Settings.Addspace(Settings, 2)
                Printator.success(Fore.RED + 'Aborted')
                Settings.Addspace(Settings, 2)
                return False
        else:
            json_data = {
                "charName": "{0}".format(self.charName),
                "charClassId": self.charClassId,
                "charClass": self.classes[self.charClassId],
                "charLevel": self.charLevel,
                "charExp": self.charExp,
                "score": self.score,
            }
            data = json.dumps(json_data)
            saved = Configator.save(Configator, data)
            if saved == True:
                Printator.saved()
            else:
                Printator.success(str(saved))
            # json.dump(json_data, fp=file, indent=4, sort_keys=False)
            return False

    def removeSave():
        remove = Printator.removeSave()
        if remove == True:
            if os.path.exists("save/save.json"):
                os.remove("save/save.json")
                Printator.success(Fore.GREEN + 'removing save file success')
                Printator.showMainMenu(Printator)
            else:
                Printator.success('No save file exist')
                Printator.showMenuOption()
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
