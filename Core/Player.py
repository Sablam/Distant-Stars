
class Player():

    def __init__(self, name,ressourcesDict):

        #id
        self.name=name

        #ressources
        self.ressourcesDict = dict(ressourcesDict)
        for ressource in self.ressourcesDict:
            print(ressource)
            self.ressourcesDict[ressource] = 100