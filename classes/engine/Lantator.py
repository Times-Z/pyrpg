import socket
import time
import select
from classes.engine.Printator import Printator

class Lantator:

    def init(self):
        menu = Printator.lanMenu(Printator)
        if menu == 'host':
            print('Choose port number :')
            self.port = input('> ')
            self.host = ''
            self.mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mainConnection.bind(('', int(self.port)))
            print('Hosting lan, wainting for client')
            self.mainConnection.listen(10)
            # no enought values to unpack ?
            (self.client, self.host, self.port) = self.mainConnection.accept()
        elif menu == 'join':
            print('join')
        elif menu == False:
            return False
        # si select == host
        # selectionner le port pour la lan et crée le serveur d'écoute?
        # else selectionner le port sans crée de serveur d'écoute?
        # choice hoster or not
        # if hoster -> choice port of lan game
        # if not hoster -> enter port of lan game
        # 