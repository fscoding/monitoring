import socket
import requests
import os
import json
import time

import socket
from contextlib import closing

def check_port(host, port):
    """ Function for checking the ports on remote system. """

    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False


class Monitoring():
    def _databaseLoader(self, file='app/Database/data.json'):
        if os.path.isfile(file):
            try:
                with open(file) as file:
                   return json.load(file)
            except:
                return list()
        else:
            return list()

    def __init__(self, token):
        self.token = token

    def addToMonitoring(self, name, host, port=80):
        self.data = self._databaseLoader()
        self.data.append({'name': name, 'host' : host, 'port' :port})

    def deleteFromMonitoring(self, name):
        if name in self.data:
            self.data.pop(name)
            return f'message: {name} was deleted from monitoring.'
        else:
            return f'message: {name} not found'

    def startMonitoring(self):
        while True:
            for i in self.data:
                try:
                    check_port(i['host'], i['port'])
                    print('Server is up')
                except:
                    print('Server is down')
            time.sleep(2)



    def commitToFile(self):
        fileName='app/Database/data.json'
        with open(fileName, 'w') as file:
            json.dump(self.data, file, indent=2)
