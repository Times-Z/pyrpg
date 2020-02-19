import socket
import time
import select
from classes.engine.Printator import Printator

class Lantator:

    def init(self):
        self.host = '127.0.0.1'
        menu = Printator.lanMenu(Printator)
        if menu == 'host':
            print('Choose port number :')
            self.port = input('> ')
            self.mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mainConnection.bind(('', int(self.port)))
            print('Hosting lan, wainting for client')
            self.mainConnection.listen(10)
            (self.connection, self.port) = self.mainConnection.accept()
            servUp = True
            while servUp == True:
                try:
                    request = self.connection.recv(2048)
                    if request:
                        data = request.decode()
                        print(data)
                except Exception as e:
                    print(e)
        elif menu == 'join':
            print('Enter port number :')
            self.port = input('> ')
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.host, int(self.port)))
            print('Connection etablished on port {0}'.format(self.port))
            data = input('>>> ')
            self.connection.send(data.encode())
        elif menu == False:
            return False
        # si select == host
        # selectionner le port pour la lan et crée le serveur d'écoute?
        # else selectionner le port sans crée de serveur d'écoute?
        # choice hoster or not
        # if hoster -> choice port of lan game
        # if not hoster -> enter port of lan game
        # 