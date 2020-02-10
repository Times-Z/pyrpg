# -*- coding: utf-8 -*-
import os
import time
from colorama import Fore, Back, Style
from settings.Settings import Settings


class Printator():

    classes = Settings.loadClass(Settings)

    def __init__(self):
        print(Fore.GREEN + "R" + Fore.YELLOW + "py")
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
              "The python game" + Fore.RESET)
        return True

    def loading(valmin, valmax, *mess):
        os.system('setterm -cursor off')
        begin = "["
        close = "]"
        bar = [
            " =     ",
            "  =    ",
            "   =   ",
            "    =  ",
            "     = ",
            "      =",
            "     = ",
            "    =  ",
            "   =   ",
            "  =    ",
        ]
        while valmin != valmax:
            print(
                Fore.WHITE
                + begin
                + Fore.RED
                + bar[valmin % len(bar)]
                + Fore.WHITE
                + close,
                end="\r",
            )
            time.sleep(0.1)
            valmin += 1
        else:
            if mess:
                print(Fore.GREEN + mess + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "                        " + Style.RESET_ALL)
        os.system('setterm -cursor on')
        return True

    def saveFound(self, save):
        print("Save file found for :")
        print(
            save["charName"]
            + " "
            + self.classes[int(save["charClassId"])]["name"]
            + " level "
            + str(save["charLevel"])
        )
        print("Continue with this game ? y/n")
        return True
