# -*- coding: utf-8 -*-
import os
import time
from colorama import Fore, Back, Style
from classes.char.Character import Character

class Fightator():

    def __init__(self, me):
        self.turn = 1
        self.monster = Character('monster')

    def quickBattle(self, me):
        self.__init__(self, me)
        print('Monster ::::'+self.monster.name)
        print('Player ::::'+me.name)