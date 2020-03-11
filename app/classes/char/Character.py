# -*- coding: utf-8 -*-
import json
import random
from classes.engine.Apitator import Apitator


class Character(Apitator):

    def __init__(self, charType):
        if charType == 'monster':
            with open('/app/settings/monsters.json') as f:
                data = json.load(f)
            monster = random.choice(data)
            self.type = 'monster'
            self.name = monster['name']
            self.hp = random.randint(monster['minHp'], monster['maxHp'])
            self.maxHp = self.hp
            self.atk = random.randint(monster['minAtk'], monster['maxAtk'])
            self.acr = random.randint(monster['minAcr'], monster['maxAcr'])
            self.defc = monster['def']
            self.spe = monster['spell']
            self.xp = random.randint(monster['expMin'], monster['expMax'])
        else:
            with open("/app/settings/classes.json", "r") as f:
                self.charClass = json.load(f)
            this = self.charClass[charType]
            self.type = 'player'
            self.id = charType
            self.name = this['name']
            self.hp = this['hp']
            self.maxHp = this['hp']
            self.atk = this['atk']
            self.defc = this['def']
            self.acr = this['acr']
            self.spe = this['spe']
