from entities import Case_Terrain
from lxml import etree
import random
import os
import re



class Planet_obj():

    def __init__(self,width,heigh):
        self.entitie_type="planet"
        self.size = (width, heigh)
        planets_list = etree.parse("Data/planets.xml")

        #selection aléatoire du type de planete
        planet_type=[]
        for planet in planets_list.xpath("/planets/planet/type"):
            if planet.text not in planet_type:
                planet_type.append(planet.text)

        self.type=planet_type[random.randint(0,len(planet_type)-1)]

        #selection aléatoire de sa classe
        planet_class=[]
        for planet in planets_list.xpath("/planets/planet[type='{0}']/classe".format(self.type)):
            if planet.text not in planet_class:
                planet_class.append(planet.text)

        self.classe=planet_class[random.randint(0,len(planet_class)-1)]

        #print("{0} {1}".format(self.type,self.classe))

        #selection aléatoire de son apparence
        number=0
        for file in os.listdir('Ressources Graphiques/Espace/planets'):
            if re.match("continental", file):
                number=number+1
        print(number)

        self.appearence="{0}{1}".format(self.classe,random.randint(1,number))


        self.hexaGrid = [[Case_Terrain.Case_Terrain_obj()] * width for _ in range(heigh)]