import json


class Settings():

    validateTurns = [
        2,
        4,
        6,
        8,
        10,
        12,
        14,
        16,
        18,
        20,
        22,
        24,
        28,
        30,
        32,
        34,
        38,
        40,
        42,
        44,
        48,
        50,
        52,
        54,
        58,
        60
    ]
    protect = 0
    lastAtk = 0

    def debug(*values):
        return print(values)

    def loadSave():
        with open('save/save.json', 'r') as save:
            load_save = json.load(save)
        return load_save

    def loadClass(self):
        with open('settings/classes.json', 'r') as f:
            load_class = json.load(f)
        return load_class

    def Addspace(self, nbrSpace):
        for i in range(nbrSpace):
            print('')
        return

    def showMainTitle(self, name, charClass, level):
        print('-------------------------------------------')
        print('| RPY GAME - THE PYTHON ROLE PLAYING GAME |')
        print('| _______________________________________ |')
        self.Addspace(self, 2)
        print('Name  : ' + name)
        print('Class : ' +
              self.loadClass(self)[int(charClass)]['name'])
        print('Level : ' + str(level))
        self.Addspace(self, 2)

    def mainMenu():
        menu = [
            'Quick battle',
            'Campagne',
            'Options',
            'Save',
            'Exit'
        ]
        return menu

    def options():
        options = [
            'Delete save',
            'Back'
        ]
        return options

    def calcAtk(self, atk, hp):
        if self.protect == 0:
            res = hp - atk
            self.lastAtk = atk
            self.protect = 0
        else:
            if self.protect > 100:
                reduceAtk = 0
            else:
                reduceAtk = round(atk * (int(self.protect) / 100))
            res = hp - reduceAtk
            self.lastAtk = reduceAtk
            self.protect = 0
        return int(res)

    def checkLevel(level, xp):
        with open('settings/levels.json') as jsonLevel:
            levels = json.load(jsonLevel)
        key = level - 1
        xpNeed = levels[key]['toUp']
        if xp >= xpNeed:
            return True
        else:
            return False
    
    # def calcSpeAtk(self, target, speFocus, speAlt, speValue):
    #     res = target.atk

    def calcSpeHp(self, target, speAlt, speValue):
        res = str(target.hp) + str(speAlt) + str(speValue)
        return eval(res)