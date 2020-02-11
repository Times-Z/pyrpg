# -*- coding: utf-8 -*-
import json


class Class:
    def __init__(self):
        with open("settings/classes.json", "r") as f:
            self.charClass = json.load(f)

# Cree une class unique pour chaque perso
# construct nom de class
# 
class Rogue(Class):
    def __init__(self):
        self.id = 0
        self.name = Class().charClass[0]["name"]
        self.hp = Class().charClass[0]["hp"]
        self.maxHp = Class().charClass[0]["hp"]
        self.atk = Class().charClass[0]["atk"]
        self.defc = Class().charClass[0]["def"]
        self.acr = Class().charClass[0]["acr"]
        self.spe = Class().charClass[0]["spe"]
        super().__init__()


class Warrior(Class):
    def __init__(self):
        self.id = 1
        self.name = Class().charClass[1]["name"]
        self.hp = Class().charClass[1]["hp"]
        self.maxHp = Class().charClass[1]["hp"]
        self.atk = Class().charClass[1]["atk"]
        self.defc = Class().charClass[1]["def"]
        self.acr = Class().charClass[1]["acr"]
        self.spe = Class().charClass[1]["spe"]
        super().__init__()


class Gunner(Class):
    def __init__(self):
        self.id = 2
        self.name = Class().charClass[2]["name"]
        self.hp = Class().charClass[2]["hp"]
        self.maxHp = Class().charClass[2]["hp"]
        self.atk = Class().charClass[2]["atk"]
        self.defc = Class().charClass[2]["def"]
        self.acr = Class().charClass[2]["acr"]
        self.spe = Class().charClass[2]["spe"]
        super().__init__()


class Developer(Class):
    def __init__(self):
        self.id = 3
        self.name = Class().charClass[3]["name"]
        self.hp = Class().charClass[3]["hp"]
        self.maxHp = Class().charClass[3]["hp"]
        self.atk = Class().charClass[3]["atk"]
        self.defc = Class().charClass[3]["def"]
        self.acr = Class().charClass[3]["acr"]
        self.spe = Class().charClass[3]["spe"]
        super().__init__()


class Admin(Class):
    def __init__(self):
        self.id = 4
        self.name = Class().charClass[4]["name"]
        self.hp = Class().charClass[4]["hp"]
        self.maxHp = Class().charClass[4]["hp"]
        self.atk = Class().charClass[4]["atk"]
        self.defc = Class().charClass[4]["def"]
        self.acr = Class().charClass[4]["acr"]
        self.spe = Class().charClass[4]["spe"]
        super().__init__()
