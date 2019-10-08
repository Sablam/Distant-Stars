from Entities.entities import Entities

class Ship_Obj(Entities):

    def __init__(self,owner, type):
        self.owner = owner
        self.type=type

        self.travel = 1
        self.firepower = 0
        self.hull = 1
        self.shield = 0

    def IsMovable(self,pos):

        test=0

    def Move(self, pos):
        test=0

