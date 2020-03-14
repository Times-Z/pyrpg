# -*- coding: utf-8 -*-
import sys
import requests
import time
import json
import os
import getpass
from colorama import Fore, Back, Style
from classes.engine.Printator import Printator

class Apitator:
    """
        Get data from api
    """

    def __init__(self):
        self.printator = Printator()
        self.token = ''
        self.onlineApi = "http://5.196.72.181:8080/"
        self.localApi = "http://api:8080/"
        self.printator.success('Checking API')
        try:
            r = requests.post(self.onlineApi + 'ping')
            if r.status_code == 200:
                self.env = 'online'
                self.ip = self.onlineApi
                self.printator.success(Fore.GREEN + 'API online status ok')
        except Exception as e:
            self.printator.success(Fore.RED + 'API online not responding')
            time.sleep(0.5)
            try:
                r = requests.post(self.localApi + 'ping')
                if r.status_code == 200:
                    self.env = 'local'
                    self.ip = self.localApi
                    self.printator.success(Fore.GREEN + 'API local status ok')
            except Exception as e:
                self.printator.success(Fore.RED + "API local not responding")
                time.sleep(0.5)
                self.printator.success('To start the local API refer you to https://github.com/Crash-Zeus/pyrpgApi')
                self.printator.success('If your local API is started and the problem persists checked ip of API container')
                self.printator.success('The default ip for local API in the program is ' + Fore.GREEN + self.localApi)
                sys.exit()
    
    def login(self, log = False):
        if log == False:
            logs = self.printator.logMenu()
        elif log == 1:
            logs = 'signin'
        else:
            logs = 'signup'
        if logs == 'signin':
            if log == False:
                self.printator.success('Create an account')
            email = input('Email > ')
            username = input('Pseudo > ')
            passw = self.registeryPass()
            if passw == False:
                self.login(1)
            data = {
                "username" : username,
                "email" : email,
                "password": passw
            }
            r = requests.post(self.ip + 'signup', data)
            if r.status_code == 200:
                self.printator.success(Fore.GREEN + 'Your account have successfully created')
                self.login(2)
            elif r.status_code == 401:
                self.printator.success(Fore.RED + str(r.json()['message']))
                self.login(1)
            else:
                self.printator.success(Fore.RED + str(r.json()['message']))
                self.login(True)
        elif logs == 'signup':
            self.printator.success('Connect to your account')
            email = input('Email > ')
            password = getpass.getpass(prompt='Password > ', stream=None)
            data = {
                "email" : email,
                "password" : password
            }
            r = requests.post(self.ip + 'login', data)
            if r.status_code == 200:
                self.token = str(r.json()['data'])
                self.printator.success(Fore.GREEN + 'Logged')
            else:
                sys.exit(Fore.RED + str(r.json()['message']) + Fore.RESET)
        else:
            self.login()

    def registeryPass(self):
        password = getpass.getpass(prompt='Password > ', stream=None)
        confirmpass = getpass.getpass(prompt='Confirm password > ', stream=None)
        if password == confirmpass:
            return password
        else:
            self.printator.success(Fore.RED + 'Password not match')
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

    def requestClass(self):
        r = requests.get(self.ip + 'classes')
        if r.status_code == 200:
            return r.json()['classes']
        else:
            return r.json()['message']

    def getClass(self, cID = False):
        apiClass = self.requestClass()
        if cID == False:
            write = False
            with open('/app/settings/tmp.json', 'a') as f:
                f.write('[')
                for x in range (0,len(apiClass)):
                    toDict = json.loads(apiClass[x]['class_json'])
                    toJson = json.dump(toDict, f)
                    if x != (len(apiClass) - 1):
                        f.write(',')
                f.write(']')
                f.close()
                write = True
            if write == True:
                with open('/app/settings/tmp.json', 'r') as f:
                    loads = json.load(f)
                os.remove('/app/settings/tmp.json')
                return loads
        else:
            toDict = json.loads(apiClass[cID]['class_json'])
            return loads
    
    def getLevels(self):
        r = requests.get(self.ip + 'levels')
        if r.status_code == 200:
            levels = json.dumps(r.json()['levels'])
            return levels
        else:
            return r.json()['message']
    
    def requestMonster(self):
        r = requests.get(self.ip + 'monsters')
        if r.status_code == 200:
            return r.json()['monsters']
        else:
            return r.json()['message']

    def getMonster(self):
        apiMonster = self.requestMonster()
        write = False
        with open('/app/settings/tmp.json', 'a') as f:
            f.write('[')
            for x in range (0,len(apiMonster)):
                toDict = json.loads(apiMonster[x]['monster_json'])
                toJson = json.dump(toDict, f)
                if x != (len(apiMonster) - 1):
                    f.write(',')
            f.write(']')
            f.close()
            write = True
        if write == True:
            with open('/app/settings/tmp.json', 'r') as f:
                loads = json.load(f)
            os.remove('/app/settings/tmp.json')
            return loads