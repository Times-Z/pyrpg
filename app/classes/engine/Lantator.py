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
                        if data == 'exit':
                            servUp = False
                            return True
                        print(data)
                except Exception as e:
                    print(e)
        elif menu == 'join':
            print('Enter port number :')
            self.port = input('> ')
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self.connection.connect((self.host, int(self.port)))
                print('Connection etablished on port {0}'.format(self.port))
                connection = True
                while connection == True:
                    data = input('>>> ')
                    self.connection.send(data.encode())
                    if data == 'exit':
                        connection == False
                        return True
            except Exception as e:
                print(e)
                exit
        elif menu == 'back':
            return True
        elif menu == False:
            return False
