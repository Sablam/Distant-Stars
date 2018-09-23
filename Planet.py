import Case_Terrain


class Planet_obj():

    def __init__(self,width,heigh):
        self.entitie_type="planet"
        self.size = (width, heigh)
        self.type="Classe M"
        self.hexaGrid = [[Case_Terrain.Case_Terrain_obj()] * heigh for _ in range(width)]