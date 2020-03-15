# -*- coding: utf-8 -*-
import json
import random

class Character:
    """
        - Type : str "player" or "monster"
        - name : str
        - maxHp : int
        - hp : int
        - atk : int
        - acr : int
        - defc : int
        - spe : json string

        for monster only :
        - xp : int
    """

    def __init__(self, api, charType):
        if charType == 'monster':
            data = api.getMonster()
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
            self.charClass = api.getClass()
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
