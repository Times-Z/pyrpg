import random
import json

class Monster():

    def __init__(self):
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
        test = self.spell(monster['spel'])
        # print(json.dumps(monster, indent=4))

    def spell(self, spell):
        self.spellName = spell['name']
        if spell['target'] == 'self':
            self.spellTarget = self.name
        else:
            self.spellName = 'no'


# test = Monster()