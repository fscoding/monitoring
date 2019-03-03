import socket
import requests
import os
import json

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

    def addToMonitoring(self, name, link, port=80):
        self.data = self._databaseLoader()
        self.data.append({'name': name, 'link' : link, 'port' :port})

    def deleteFromMonitoring(self, name):
        if name in self.data:
            self.data.pop(name)
            return f'message: {name} was deleted from monitoring.'
        else:
            return f'message: {name} not found'

    def startMonitoring(self):
        while True:
            for i in seld.data:
                resp = requests.get(i['link'])
            time.sleep(2)

    def commitToFile(self):
        fileName='app/Database/data.json'
        with open(fileName, 'w') as file:
            json.dump(self.data, file, indent=2)
