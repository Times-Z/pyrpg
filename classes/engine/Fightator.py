# -*- coding: utf-8 -*-
import os
import time
import random
from colorama import Fore, Back, Style
from classes.char.Character import Character
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from settings.Settings import Settings

# Fight engine
class Fightator():

    def init(self, me):
        self.end = 0
        self.me = me
        self.turn = 1
        self.useSpe = 0
        self.protect = 0
        self.lastAtk = 0
        self.monster = Character('monster')

    def quickBattle(self, me):
        self.init(self, me)
        Settings.Addspace(Settings, 20)
        Printator.battleInfo(self.turn, self.me, self.monster)
        self.battleAction(self)
        return 0

    def battleAction(self):
        action = Printator.showBattleAction(self.useSpe, self.me, self.monster)
        if action == 'attak':
            hp = self.attak(self, self.me, self.monster)
            if hp > 0:
                self.monster.hp = hp
                Printator.attak(self.lastAtk, self.monster)
                Settings.Addspace(Settings, 2)
                self.cpuTurn(self)
            else:
                self.end = 1
                win = self.win(self)
                return 0
        elif action == 'protect':
            self.protectAction(self, self.me)
            self.cpuTurn(self)
        elif action == 'spe':
            self.spell(self, self.me)
            # self.cpuTurn(self)
        elif action == False:
            Printator.success('Bad entry', 2)
            self.battleAction(self)

    def attak(self, caster, target):
        if self.protect == 0:
            res = target.hp - caster.atk
            self.lastAtk = caster.atk
            self.protect = 0
        else:
            if self.protect >= 100:
                atk = 0
            else:
                atk = round(caster.atk * (int(self.protect) / 100))
            res = target.hp - atk
            self.lastAtk = atk
            self.protect = 0
        return int(res)
    
    def protectAction(self, caster):
        self.protect = caster.defc
        return True

    def spell(self, caster):
        spellName = caster.spe['name']
        spellTarget = caster.spe['target']
        spellFocus = caster.spe['effect']['focus']
        spellAlterate = caster.spe['effect']['alterate']

        if caster.type == 'monster':
            spellPower = random.randint(caster.spe['effect']['minRange'], caster.spe['effect']['maxRange'])
        else:
            spellPower = caster.spe['effect']['value']
        # TODO

    def cpuTurn(self):
        Printator.success(self.monster.name + ' playing...')
        Printator.loading(0, 10)
        action = random.randint(1, 3)
        if action == 1:
            Printator.success(self.monster.name + ' attak !')
            hp = self.attak(self, self.monster, self.me)
            if hp > 0:
                self.me.hp = hp
                Printator.attak(self.lastAtk, self.me)
                self.protect = 0
            else:
                self.gameOver(self)
        elif action == 2:
            Printator.success(self.monster.name + ' protect him !')
            self.protectAction(self, self.monster)
        elif action == 3:
            if self.turn in Settings.validateTurns:
                Printator.success(self.monster.name + ' use a special spell !')
                self.protect = 0
                # TODO
            else:
                Printator.success('Bad entry')
                self.cpuTurn(self)
        if self.end == 1:
            return 0
        self.turn += 1
        Printator.battleInfo(self.turn, self.me, self.monster)
        self.battleAction(self)

    def win(self):
        Saveator.charExp += self.monster.xp
        level = Saveator.checkLevel(Saveator.charLevel, Saveator.charExp)
        Settings.Addspace(Settings, 2)
        Printator.success('Exp win : ' + Fore.GREEN + str(self.monster.xp) + Fore.RESET)
        Printator.success('Total exp : ' + Fore.GREEN + str(Saveator.charExp) + Fore.RESET)
        Settings.Addspace(Settings, 2)
        if level == True:
            Saveator.charLevel += 1
            Printator.success(Fore.GREEN + 'Level up !' + Fore.RESET)
            Printator.success('Level : ' + str(Saveator.charLevel), 2)
        return 0

    def gameOver(self):
        return True