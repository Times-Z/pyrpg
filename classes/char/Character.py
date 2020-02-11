# -*- coding: utf-8 -*-
import json


class Character():
    def __init__(self, charType):
        if charType == 'monster':
            print('monster')
        else:
            with open("settings/classes.json", "r") as f:
                self.charClass = json.load(f)
            this = self.charClass[charType]
            self.id = charType
            self.name = this['name']
            self.hp = this['hp']
            self.maxHp = this['hp']
            self.atk = this['atk']
            self.defc = this['def']
            self.acr = this['acr']
            self.spe = this['spe']
            return True