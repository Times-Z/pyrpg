import sys
import requests
import time
import getpass
from colorama import Fore, Back, Style
from classes.engine.Printator import Printator

class Configator:

    onlineApi = "http://5.196.72.181:8080/"
    localApi = "http://api:8080/"
    env = ''
    ip = ''
    token = ''

    def init(self):
        Printator.success('Checking API')
        try:
            r = requests.post(self.onlineApi + 'ping')
            if r.status_code == 200:
                self.env = 'online'
                self.ip = self.onlineApi
                Printator.success(Fore.GREEN + 'API online status ok')
                return True
        except Exception as e:
            time.sleep(0.5)
            Printator.success(Fore.RED + 'API online not responding')
            time.sleep(0.5)
            try:
                r = requests.post(self.localApi + 'ping')
                if r.status_code == 200:
                    self.env = 'local'
                    self.ip = self.localApi
                    Printator.success(Fore.GREEN + 'API local status ok')
                    time.sleep(0.5)
                    return True
            except Exception as e:
                Printator.success(Fore.RED + "API local not responding")
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
        elif log == 1:
            logs = 'signin'
        else:
            logs = 'signup'
        if logs == 'signin':
            if log == False:
                Printator.success('Create an account')
            email = input('Email > ')
            username = input('Pseudo > ')
            passw = self.registeryPass(self)
            if passw == False:
                self.login(self, 1)
            data = {
                "username" : username,
                "email" : email,
                "password": passw
            }
            r = requests.post(self.ip + 'signup', data)
            if r.status_code == 200:
                Printator.success(Fore.GREEN + 'Your account have successfully created')
                self.login(self, 2)
            elif r.status_code == 401:
                Printator.success(Fore.RED + str(r.json()['message']))
                self.login(self, 1)
            else:
                Printator.success(Fore.RED + str(r.json()['message']))
                self.login(self, True)
        elif logs == 'signup':
            Printator.success('Connect to your account')
            email = input('Email > ')
            password = getpass.getpass(prompt='Password > ', stream=None)
            data = {
                "email" : email,
                "password" : password
            }
            r = requests.post(self.ip + 'login', data)
            if r.status_code == 200:
                self.token = str(r.json()['data'])
                Printator.success(Fore.GREEN + 'Logged')
            else:
                sys.exit(Fore.RED + str(r.json()['message']) + Fore.RESET)
        else:
            self.login(self)

    def registeryPass(self):
        password = getpass.getpass(prompt='Password > ', stream=None)
        confirmpass = getpass.getpass(prompt='Confirm password > ', stream=None)
        if password == confirmpass:
            return password
        else:
            Printator.success(Fore.RED + 'Password not match')
            return False

    def getSave(self):
        header = {'Authorization':'Bearer ' + self.token}
        r = requests.post(self.ip + 'getSave', headers=header)
        if r.json()['save'] != None:
            return r.json()
        else:
            return False
    
    def removeSave(self):
        header = {'Authorization':'Bearer ' + self.token}
        r = requests.post(self.ip + 'delSave', headers=header)
        if r.status_code == 200:
            return True
        else:
            return r.json()

    def save(self, raw):
        header = {'Authorization':'Bearer ' + self.token}
        data = {"save":raw}
        r = requests.post(self.ip + 'save', data, headers=header)
        if r.status_code == 200:
            return True
        else:
            return r.json()['message']