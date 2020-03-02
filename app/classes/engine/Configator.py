import sys
import requests
import time
import getpass
from colorama import Fore, Back, Style
from classes.engine.Printator import Printator

class Configator:

    onlineApi = "http://2001:41d0:301::29:8080/"
    localApi = "http://172.18.1.1:8080/"
    env = ''
    ip = ''

    def init(self):
        Printator.success('Checking API')
        try:
            r = requests.post(self.onlineApi + 'ping')
            if r.status_code == 200:
                self.env = 'online'
                self.ip = self.onlineApi
                Printator.success(Fore.GREEN + 'API online status ok' + Fore.RESET)
                return True
        except Exception as e:
            time.sleep(0.5)
            Printator.success(Fore.RED + 'API online not responding' + Fore.RESET)
            time.sleep(0.5)
            try:
                r = requests.post(self.localApi + 'ping')
                if r.status_code == 200:
                    self.env = 'local'
                    self.ip = self.localApi
                    Printator.success(Fore.GREEN + 'API local status ok' + Fore.RESET)
                    time.sleep(0.5)
                    return True
            except Exception as e:
                Printator.success(Fore.RED + "API local not responding" + Fore.RESET)
                time.sleep(0.5)
                Printator.success('To start the local API refer you to https://github.com/Crash-Zeus/pyrpgApi')
                time.sleep(0.5)
                Printator.success('If your local API is started and the problem persists checked ip of API container')
                time.sleep(0.5)
                Printator.success('The default ip for local API in the program is ' + Fore.GREEN + self.localApi + Fore.RESET)
                time.sleep(0.5)
                sys.exit()
    
    def login(self, log = False):
        if log == False:
            logs = Printator.logMenu(Printator)
        else:
            logs = 'signup'
        if logs == 'signin':
            Printator.success('Create an account')
            email = input('Email > ')
            username = input('Pseudo > ')
            password = getpass.getpass(prompt='Password > ', stream=None)
            confirmpass = getpass.getpass(prompt='Confirm password > ', stream=None)
            if password != confirmpass:
                Printator.success('Passwords not matching')
                return False

            data = {
                "username" : username,
                "email" : email,
                "password": password
            }
            r = requests.post(self.ip + 'signup', data)
            if r.status_code == 200:
                Printator.success(Fore.GREEN + 'Your account have successfully created' + Fore.RESET)
            else:
                Printator.success(Fore.RED + 'An error was encountered' + Fore.RESET)
            self.login(self, True)
        elif logs == 'signup':
            Printator.success('Login')
        else:
            self.login(self)