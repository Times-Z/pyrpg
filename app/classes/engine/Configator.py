import sys
import requests
from colorama import Fore, Back, Style
from classes.engine.Printator import Printator

class Configator:

    def init(self):
        Printator.success('Checking API')
        try:
            r = requests.get("http://2001:41d0:301::29:8080/")
            if r.status_code == 200:
                self.env = 'online'
                Printator.success(Fore.GREEN + 'API online status ok' + Fore.RESET)
        except Exception as e:
            Printator.success(Fore.RED + 'API online not responding' + Fore.RESET)
            try:
                r = requests.get("http://172.17.0.2:8080/")
                if r.status_code == 200:
                    self.env = 'local'
                    Printator.success(Fore.GREEN + 'API local status ok' + Fore.RESET)
            except Exception as e:
                Printator.success(Fore.RED + "API not responding, can't start game" + Fore.RESET)
                sys.exit()