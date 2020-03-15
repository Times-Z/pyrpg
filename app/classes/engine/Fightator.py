# -*- coding: utf-8 -*-
import os
import sys
import time
import random
from colorama import Fore, Back, Style
from classes.char.Character import Character
from settings.Settings import Settings

# Fight engine
class Fightator:

    def __init__(self, api, saveator, printator):
        self.printator = printator
        self.saveator = saveator
        self.settings = Settings()
        self.end = 0
        self.turn = 1
        self.useSpe = 0
        self.protect = 0
        self.lastAtk = 0
        self.me = self.saveator.me
        self.me.hp = self.me.maxHp
        self.monster = Character(api,'monster')

    def quickBattle(self):
        self.printator.addSpace(20)
        self.printator.battleInfo(self.turn, self.me, self.monster)
        self.battleAction()
        return 0

    def battleAction(self):
        action = self.printator.showBattleAction(self.useSpe, self.me, self.monster)
        if action == 'attak':
            hp = self.attak(self.me, self.monster)
            if hp > 0:
                self.monster.hp = hp
                self.printator.attak(self.lastAtk, self.monster)
                self.printator.addSpace(2)
                self.cpuTurn()
            else:
                self.end = 1
                win = self.win()
                return 0
        elif action == 'protect':
            self.protectAction(self.me)
            self.cpuTurn()
        elif action == 'spe':
            if self.useSpe == 0:
                self.spell(self.me)
                self.cpuTurn()
            else:
                self.printator.success("\x1B[3mBad entry\x1B[23m", 2)
                self.battleAction()
        elif action == 'escape':
            escape = self.escape()
            if escape == True:
                self.end = 1
                return 0
            else:
                self.cpuTurn()
        elif action == 'pass':
            self.cpuTurn()
        elif action == False:
            self.printator.success("\x1B[3mBad entry\x1B[23m", 2)
            self.battleAction()

    def attak(self, caster, target):
        if self.protect == 0:
            if caster.atk < 0:
                res = target.hp - 0
                self.lastAtk = 0
            else:
                res = target.hp - caster.atk
                self.lastAtk = caster.atk
            self.protect = 0
        else:
            if self.protect >= 100:
                atk = 0
            elif self.protect < 0:
                positif = abs(self.protect)
                add = round(caster.atk * (int(self.protect) / 100))
                atk = positif + add
            else:
                atk = round(caster.atk * (int(self.protect) / 100))
            res = target.hp - atk
            self.lastAtk = atk
            if caster.atk < 0:
                res = target.hp - 0
                self.lastAtk = 0
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
            spellPower = random.randint(
                caster.spe['effect']['minRange'], caster.spe['effect']['maxRange'])
            if spellTarget == 'self':
                self.printator.useSpell(self.monster.name, spellName, spellFocus,
                                   self.monster.name, spellAlterate, spellPower, True)
            else:
                self.printator.useSpell(caster, spellName, spellFocus,
                                   self.me, spellAlterate, spellPower)
        else:
            spellPower = caster.spe['effect']['value']
            if spellTarget == 'self':
                self.printator.useSpell(self.saveator.charName, spellName, spellFocus,
                                   self.saveator.charName, spellAlterate, spellPower, True)
            else:
                self.printator.useSpell(caster, spellName, spellFocus,
                                   self.monster, spellAlterate, spellPower)
            self.useSpe += 1

        if caster.type == 'monster':
            if spellTarget == 'self':
                self.calcSpell(caster, spellFocus, spellAlterate, spellPower)
                return True
            else:
                self.calcSpell(self.me, spellFocus,
                            spellAlterate, spellPower)
                return True
        else:
            if spellTarget == 'self':
                self.calcSpell(caster, spellFocus, spellAlterate, spellPower)
                return True
            else:
                self.calcSpell(self.monster, spellFocus,
                            spellAlterate, spellPower)
                return True

    def calcSpell(self, target, focus, alt, power):
        if focus == 'def':
            focus = 'defc'
        attr = getattr(target, focus)
        calc = str(attr) + str(alt) + str(power)
        spell = eval(calc)
        if focus == 'hp':
            if spell > target.maxHp:
                spell = target.maxHp
                self.printator.success('Healing cannot exceed max HP', 1)
                self.printator.success(Fore.GREEN + 'Hp full', 1)
        setattr(target, focus, spell)
        return True

    def cpuTurn(self):
        self.printator.success(self.monster.name + ' playing...')
        self.printator.loading(0, 10)
        action = random.randint(1, 3)
        if action == 1:
            self.printator.success(self.monster.name + ' attak !')
            hp = self.attak(self.monster, self.me)
            if hp > 0:
                self.me.hp = hp
                self.printator.attak(self.lastAtk, self.me)
                self.protect = 0
            else:
                self.gameOver(self)
        elif action == 2:
            self.printator.success(self.monster.name + ' protect him !')
            self.protectAction(self.monster)
        elif action == 3:
            if self.settings.validateTurn(self.turn) == True:
                self.printator.success(self.monster.name + ' use a special spell !')
                self.spell(self.monster)
                self.protect = 0
                # TODO
            else:
                self.printator.success("\x1B[3mBad entry\x1B[23m")
                self.cpuTurn()
        if self.end == 1:
            return 0
        self.turn += 1
        self.printator.battleInfo(self.turn, self.me, self.monster)
        self.battleAction()

    def escape(self):
        self.printator.success('Rolling dice...')
        self.printator.loading(0, 5)
        dice = random.randint(1, 6)
        if dice == 6:
            self.printator.success(Fore.GREEN + 'Escape success', 2)
            return True
        else:
            self.printator.success(Fore.RED + 'Escape failed', 2)
            return False

    def win(self):
        self.saveator.charExp += self.monster.xp
        level = self.saveator.checkLevel(self.saveator.charLevel, self.saveator.charExp)
        self.printator.addSpace(2)
        self.printator.success('Exp win : ' + Fore.GREEN +
                          str(self.monster.xp))
        self.printator.success('Total exp : ' + Fore.GREEN +
                          str(self.saveator.charExp))
        self.printator.addSpace(2)
        if level == True:
            self.saveator.charLevel += 1
            self.saveator.updateStats()
            self.printator.success(Fore.GREEN + 'Level up !')
            self.printator.success('Level : ' + str(self.saveator.charLevel), 2)
        return 0

    def gameOver(self):
        self.printator.success(Fore.RED + ' GAME OVER ! ')
        self.end = 1
        sys.exit('Quit game, you die')
