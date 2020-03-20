# -*- coding: utf-8 -*-
import socket
import time
import select
from classes.engine.Printator import Printator


class Lantator:

    def __init__(self, printator):
        self.printator = printator
        self.host = '127.0.0.1'
        self.port = '8000'

    def choice(self):
        menu = self.printator.lanMenu()
        return menu

    def hoster(self):
        self.printator.success('Choose port number :')
        self.port = input('> ')
        self.mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mainConnection.bind(('', int(self.port)))
        self.printator.success('Hosting lan, wainting for client')
        self.mainConnection.listen(10)
        (self.connection, self.port) = self.mainConnection.accept()
        servUp = True
        while servUp == True:
            try:
                serverInput = input('> ')
                request = self.connection.recv(2048)
                if request:
                    data = request.decode()
                    if data == 'exit':
                        Printator.success('Client exiting game, closing session')
                        servUp = False
                        return True
                    print(data)
            except Exception as e:
                print(e)

    def joiner(self):
        self.printator.success('Enter port number :')
        self.port = input('> ')
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connection.connect((self.host, int(self.port)))
            self.printator.success('Connection etablished on port {port}'.format(port=self.port))
            self.connection = True
            while connection:
                data = input('>>> ')
                self.connection.send(data.encode())
                if data == 'exit':
                    self.connection = False
                    return True
        except Exception as e:
            print(e)
            exit
