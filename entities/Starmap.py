
from entities import Planet
from entities import Case_Espace


class Starmap_obj():




    def __init__(self,width,heigh):

        self.size=(width,heigh)
        self.hexaGrid=[[Case_Espace.Case_Espace_obj()] * heigh for _ in range(width)]
        #print(self.hexaGrid)

        print(self.hexaGrid[0][1].entities[0])
        self.hexaGrid[0][0].entities[0]=(Planet.Planet_obj(10, 5))
        print(self.hexaGrid[0][1].entities[0])




