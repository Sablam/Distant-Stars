import graphic.Window
from entities import Starmap
from Core import Player
from lxml import etree

class GameSession:

    def __init__(self,fenetre):

        # chargement des ressources collectables
        self.ressourcesDict = {}
        ressources_list = etree.parse("Data/ressources.xml")
        for ressource in ressources_list.xpath("/ressources/ressource/name"):
            if ressource.text not in self.ressourcesDict:
                self.ressourcesDict[ressource.text] = 0

        #creation des joueurs
        self.P1 = Player.Player("P1",self.ressourcesDict)

        #Initiation de la carte
        self.game_starmap = Starmap.Starmap_obj(20, 20)


        #affichage de la carte
        graphic.Window.affichage(self.game_starmap, fenetre, 20, [0, 0])

