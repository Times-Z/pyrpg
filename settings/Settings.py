import json
# from main import Game


class Settings():

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
