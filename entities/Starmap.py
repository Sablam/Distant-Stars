
from entities import Planet
from entities import Case_Espace
import random



class Starmap_obj():


    def __init__(self,width,heigh):

        self.size=(width,heigh)
        self.hexaGrid = [[Case_Espace.Case_Espace_obj() for i in range(0,heigh-1)] for j in range(0,width-1)] #hexaGrid est un tableau d'objet Case_Espace
        #print(self.hexaGrid)



        #Création des planètes
        #print(self.hexaGrid[0][1].entities[0])
        for i in range(0,random.randint(4, width*heigh/50)):
            iteration=0 #mécanisme pour éviter d'écraser une entité pré-existante et réessayer de créer cette entities autre part
            while iteration<5:#au bout de 5 tentative on stop afin d'éviter les boucles infini
                x=random.randint(0,width-2)
                y=random.randint(0,heigh-2)
                print(x)
                print(y)
                if self.hexaGrid[x][y].entities[0].entitie_type ==  "void":
                    self.hexaGrid[random.randint(0,width-2)][random.randint(0,heigh-2)].entities[0]=Planet.Planet_obj(10, 5) #ligne,colonnes
                    iteration=5
                    print("creation planete")
                else:
                    iteration += 1

        #print(self.hexaGrid[0][1].entities[0])



        #debug: affiche une planete dans toute les cases
        #for i in range(0,width-1):
        #    for y in range(0,heigh-1):
        #       self.hexaGrid[i][y].entities[0]=Planet.Planet_obj(10, 5)
