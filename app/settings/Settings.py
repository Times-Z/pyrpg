# -*- coding: utf-8 -*-
import sys
import json


class Settings:
    """
        Set some settings
    """

    protect = 0
    lastAtk = 0

    def validateTurn(self, turn):
        if (turn%2) == 0:
            return True
        else:
            return False

    def resize(self):
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=50))

    def mainMenu(self):
        menu = [
            'Quick battle',
            'LAN',
            'Options',
            'Save',
            'Exit'
        ]
        return menu

    def options(self):
        options = [
            'Delete save',
            'Back'
        ]
        return options

