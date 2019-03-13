import graphic.Window
from entities import Starmap

class GameSession:

    def __init__(self,fenetre):
        game_starmap = Starmap.Starmap_obj(20, 20)
        graphic.Window.affichage(game_starmap, fenetre, 20, [0, 0])