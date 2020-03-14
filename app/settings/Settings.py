# -*- coding: utf-8 -*-
import sys
import json


class Settings:
    """
        Set some settings
    """

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

