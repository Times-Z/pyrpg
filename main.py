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
from settings.Settings import Settings
from classes.Monster import Monster
from classes.Class import Rogue, Warrior, Gunner, Developer, Admin


class Game:

    classes = Settings.loadClass(Settings)
    charName = None
    charClass = None
    me = None
    charLevel = 1
    charExp = 0
    score = 0
    turn = 1

    def __init__(self):
        print(Fore.GREEN + "R" + Fore.YELLOW + "py")
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "The python game" + Fore.RESET)
        self.loading(0, 20, "")
        self.getSave(self)

    def getSave(self):
        if os.path.isfile("save/save.json"):
            save = Settings.loadSave()
            print("Save file found for :")
            print(
                save["charName"]
                + " "
                + self.classes[int(save["charClassId"])]["name"]
                + " level "
                + str(save["charLevel"])
            )
            print("Continue with this game ? y/n")
            game = input("> ")
            if game == "y":
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
                self.showInformation(self)
            else:
                self.choseName(self)
        else:
            self.choseName(self)

    def loading(valmin, valmax, mess):
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
            if mess != "":
                print(Fore.GREEN + mess + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "                        " + Style.RESET_ALL)
        os.system('setterm -cursor on')

    def confirm(self, param, string):
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

    def choseName(self):
        Settings.Addspace(Settings, 2)
        print("- New game -")
        Settings.Addspace(Settings, 2)
        print("Choose your name : ")
        name = input("> ")
        confirm = self.confirm(self, name, "as name")
        if confirm == True:
            self.charName = name
            print("Your name is " + Fore.GREEN + "%s" % self.charName + Fore.RESET)
            self.choseClasse(self)
        else:
            self.choseName(self)

    def choseClasse(self):
        Settings.Addspace(Settings, 4)
        for i in range(len(self.classes)):
            print(
                str(i)
                + " -> "
                + Fore.GREEN
                + self.classes[i]["name"]
                + " - Special spell : "
                + self.classes[i]["spe"]["name"]
                + Fore.RESET
            )
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
            confirm = self.confirm(self, self.classes[int(classChose)]["name"], "")
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

    def showInformation(self):
        Settings.Addspace(Settings, 100)
        Settings.showMainTitle(Settings, self.charName, self.charClass, self.charLevel)
        self.showMainMenu(self)

    def showMainMenu(self):
        self.updateStats(self, self.me, self.charLevel)
        print("------------")
        print("| MAIN MENU |")
        print("------------")
        Settings.Addspace(Settings, 2)
        for i in range(len(Settings.mainMenu())):
            print(str(i) + " -> " + Settings.mainMenu()[i])
        Settings.Addspace(Settings, 2)
        action = input("> ")

        if action == "0":
            self.quickBattle(self)
        elif action == "1":
            print("CAMPAGNE")
        elif action == "2":
            self.showOptionMenu(self)
        elif action == "3":
            self.save(self)
        elif action == "4":
            exit
        else:
            self.showMainMenu(self)

    def updateStats(self, obj, level):
        with open('settings/levels.json') as jsonLevel:
            levels = json.load(jsonLevel)
        key = level - 1
        addHp = levels[key]['hp']
        addAtk = levels[key]['atk']
        self.me.hp += int(addHp)
        self.me.maxHp += int(addHp)
        self.me.atk += int(addAtk)

    def showOptionMenu(self):
        Settings.Addspace(Settings, 100)
        print("-----------")
        print("| OPTIONS |")
        print("-----------")
        options = Settings.options()
        for i in range(len(options)):
            print(str(i) + " -> " + options[i])
        action = input("> ")

        if action == "0":
            self.removeSaveFile(self)
        elif action == "1":
            Settings.Addspace(Settings, 100)
            return self.showMainMenu(self)

    def removeSaveFile(self):
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
        if confirm == "y":
            if os.path.exists("save/save.json"):
                os.remove("save/save.json")
                print("removing save file success")
                Settings.Addspace(Settings, 5)
                self.showMainMenu(self)
            else:
                print("No save file exist")
                self.showOptionMenu(self)
        else:
            self.showOptionMenu(self)

    def save(self):
        if os.path.exists("save/save.json"):
            print("A save file already exist :")
            save = Settings.loadSave()
            print(save["charName"] + " level " + str(save["charLevel"]))
            print("This action will be replace the save file with your actual game")
            action = input("Continue ? y/n ")
            if action == "y":
                os.remove("save/save.json")
                self.save(self)
            else:
                Settings.Addspace(Settings, 100)
                self.showMainMenu(self)

        else:
            file = open("save/save.json", "a")
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
            Settings.Addspace(Settings, 100)
            print(Fore.GREEN + "Game saved" + Fore.RESET)
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)

    def createMonster(self):
        monster = Monster()
        return monster

    def quickBattle(self):
        self.turn = 1
        Settings.Addspace(Settings, 50)
        monster = self.createMonster(self)
        self.showBattleInfo(self, monster)
        self.showActions(self, self.me, monster)

    def showBattleInfo(self, monster):
        Settings.Addspace(Settings, 2)
        print('Turn : ' + str(self.turn))
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)
        print("You : ")
        print(
            "Hp : {0} / {1} | atk : {2} | def : {3} | acr : {4}".format(
                self.me.hp, self.me.maxHp, self.me.atk, self.me.defc, self.me.acr
            )
        )
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)
        print(monster.name + " :")
        print(
            "Hp : {0} / {1} | atk : {2} | def : {3} | acr : {4}".format(
                monster.hp, monster.maxHp, monster.atk, monster.defc, monster.acr
            )
        )
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)

    def showActions(self, me, monster):
        print("0 -> Attak")
        print("1 -> Special : %s " % self.me.spe['name'])
        print("2 -> Defend (%i %%)" % self.me.defc)
        print("3 -> Escape")
        Settings.Addspace(Settings, 1)
        action = input("> ")
        if action == "0":
            self.attak(self, monster)
        elif action == "1":
            self.specialSkill(self, monster)
        elif action == "2":
            self.protect(self, monster)
        elif action == "3":
            print("RUN")
        else:
            self.showActions(self, self.me, monster)

    def validate(self, me, monster):
        self.showBattleInfo(self, monster)
        self.showActions(self, me, monster)

    def attak(self, target):
        baseHp = target.hp
        hp = Settings.calcAtk(Settings,self.me.atk, target.hp)
        if hp > 0:
            target.hp = hp
            Settings.Addspace(Settings, 2)
            print("Hit ! You hurt " + target.name)
            print("Decrease hp from " + str(baseHp) + " to " + str(target.hp))
            print(Fore.RED + " - " + str(Settings.lastAtk) + " hp" + Fore.RESET)
            Settings.Addspace(Settings, 2)
            self.showBattleInfo(self, target)
            Settings.Addspace(Settings, 2)
            self.loading(0, 10, '')
            self.ennemyAction(self, target)
        else:
            self.win(self, target)

    def protect(self, monster):
        Settings.protect = self.me.defc
        self.ennemyAction(self, monster)

    def specialSkill(self, monster):
        print(json.dumps(self.me.spe, indent=4))

    def ennemyAction(self, monster):
        Settings.Addspace(Settings, 2)
        print(monster.name + ' playing...')
        self.loading(0, 10, '')
        action = random.randint(1, 3)
        if action == 1:
            self.turn += 1
            print(monster.name + ' attak !')
            Settings.Addspace(self, 2)
            self.monsterAttak(self, monster)
        elif action == 2:
            self.turn += 1
            print(monster.name + ' protect him')
            Settings.Addspace(self, 2)
            self.monsterProtect(self, monster)
        elif action == 3:
            if self.turn in Settings.validateTurns:
                self.turn += 1
                print(monster.name + ' use special spell')
                Settings.Addspace(self, 2)
                self.validate(self, self.me, monster)
            else:
                print(monster.name + ' bad entry')
                self.ennemyAction(self, monster)

    def monsterAttak(self, monster):
        hp = Settings.calcAtk(Settings, monster.atk, self.me.hp)
        if hp > 0:
            print('Hit ! ' + monster.name + ' hurt you')
            print(Fore.RED + ' - ' + str(Settings.lastAtk) + ' hp' + Fore.RESET)
            Settings.Addspace(self, 2)
            self.me.hp = hp
            self.validate(self, self.me, monster)
        else:
            self.gameOver(self, monster)
    
    def monsterProtect(self, monster):
        Settings.protect = monster.defc
        self.validate(self, self.me, monster)

    def win(self, monster):
        self.charExp += monster.xp
        up = Settings.checkLevel(self.charLevel, self.charExp)
        print("Exp win : " + Fore.GREEN + str(monster.xp) + Fore.RESET)
        print("Exp total : " + Fore.GREEN + str(self.charExp) + Fore.RESET)
        if up == True:
            self.charLevel += 1
            Settings.Addspace(Settings, 2)
            print(Fore.GREEN + "Level up !" + Fore.RESET)
            print("Level : " + str(self.charLevel))
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)
        else:
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)

    def gameOver(self, monster):
        print(monster.name + ' killed you')
        print(Fore.RED + 'GAME OVER' + Fore.RESET)
        Settings.Addspace(Settings, 4)
        exit

if __name__ == "__main__":
    try:
        Game.__init__(Game)
    except KeyboardInterrupt:
        exit
