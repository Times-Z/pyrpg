# -*- coding: utf-8 -*-
import json


class Character():
    def __init__(self, charType):
        if charType == 'monster':
            self.monster(self, charType)
        else:
            self.character(self, charType)

    def character(self, charType):
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

    def monster(self, monster):
        with open('settings/monsters.json') as f:
            data = json.load(f)
        monster = random.choice(data)
        self.name = monster['name']
        self.hp = random.randint(monster['minHp'], monster['maxHp'])
        self.maxHp = self.hp
        self.atk = random.randint(monster['minAtk'], monster['maxAtk'])
        self.acr = random.randint(monster['minAcr'], monster['maxAcr'])
        self.defc = monster['def']
        self.xp = random.randint(monster['expMin'], monster['expMax'])
        return True
        # test = self.spell(monster['spel'])
