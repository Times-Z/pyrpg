# -*- coding: utf-8 -*-
import os
import sys
import time
import random
from colorama import Fore, Back, Style
from classes.char.Character import Character
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from settings.Settings import Settings

# Fight engine
class Fightator:

    def __init__(self, api, me):
        self.end = 0
        self.turn = 1
        self.useSpe = 0
        self.protect = 0
        self.lastAtk = 0
        self.me = me
        self.me.hp = me.maxHp
        self.monster = Character(api,'monster')

    def quickBattle(self, me):
        self.init(self, me)
        Settings.Addspace(Settings, 20)
        Printator.battleInfo(self.turn, self.me, self.monster)
        self.battleAction(self)
        return 0

    # Add lanbattle function

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
            if self.useSpe == 0:
                self.spell(self, self.me)
                self.cpuTurn(self)
            else:
                Printator.success('Bad entry', 2)
                self.battleAction(self)
        elif action == 'escape':
            escape = self.escape(self)
            if escape == True:
                self.end = 1
                return 0
            else:
                self.cpuTurn(self)
        elif action == 'pass':
            self.cpuTurn(self)
        elif action == False:
            Printator.success('Bad entry', 2)
            self.battleAction(self)

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
                Printator.useSpell(self.monster.name, spellName, spellFocus,
                                   self.monster.name, spellAlterate, spellPower, True)
            else:
                Printator.useSpell(caster, spellName, spellFocus,
                                   Saveator.me, spellAlterate, spellPower)
        else:
            spellPower = caster.spe['effect']['value']
            if spellTarget == 'self':
                Printator.useSpell(Saveator.charName, spellName, spellFocus,
                                   Saveator.charName, spellAlterate, spellPower, True)
            else:
                Printator.useSpell(caster, spellName, spellFocus,
                                   self.monster, spellAlterate, spellPower)
            self.useSpe += 1

        if caster.type == 'monster':
            if spellTarget == 'self':
                self.calcSpell(self, caster, spellFocus, spellAlterate, spellPower)
                return True
            else:
                self.calcSpell(self, self.me, spellFocus,
                            spellAlterate, spellPower)
                return True
        else:
            if spellTarget == 'self':
                self.calcSpell(self, caster, spellFocus, spellAlterate, spellPower)
                return True
            else:
                self.calcSpell(self, self.monster, spellFocus,
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
                Printator.success('Healing cannot exceed max HP', 1)
                Printator.success(Fore.GREEN + 'Hp full', 1)
        setattr(target, focus, spell)
        return True

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
                self.spell(self, self.monster)
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

    def escape(self):
        Printator.success('Rolling dice...')
        Printator.loading(0, 5)
        dice = random.randint(1, 6)
        if dice == 6:
            Printator.success(Fore.GREEN + 'Escape success', 2)
            return True
        else:
            Printator.success(Fore.RED + 'Escape failed', 2)
            return False

    def win(self):
        Saveator.charExp += self.monster.xp
        level = Saveator.checkLevel(Saveator.charLevel, Saveator.charExp)
        Settings.Addspace(Settings, 2)
        Printator.success('Exp win : ' + Fore.GREEN +
                          str(self.monster.xp))
        Printator.success('Total exp : ' + Fore.GREEN +
                          str(Saveator.charExp))
        Settings.Addspace(Settings, 2)
        if level == True:
            Saveator.charLevel += 1
            Saveator.updateStats(Saveator)
            Printator.success(Fore.GREEN + 'Level up !')
            Printator.success('Level : ' + str(Saveator.charLevel), 2)
        return 0

    def gameOver(self):
        Printator.success(Fore.RED + ' GAME OVER ! ')
        self.end = 1
        sys.exit('Quit game, you die')
