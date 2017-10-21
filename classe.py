class Personnage:
    """Classe définissant le personnage par sa potition (x,y)"""
    def __init__(self,x,y):
        self.positionX=x
        self.positionY=y
    def deplacer(self,map,dir):
        """méthode déplaçant le personnage dans une direction donnée dir€[0,1,2,3] <=> [gauche,droite,haut,bas]"""
        """map est une matrice np"""
        if dir==0:
            if self.positionX!=0:
                if map[self.positionX-1][self.positionY]==0:
                    map[self.positionX][self.positionY]=0
                    map[self.positionX-1][self.positionY]=4
        elif:
            if dir==1:
                if self.positionX!=n-1:
                    if map[self.positionX+1][self.positionY]==0:
                        map[self.positionX][self.positionY]=0
                        map[self.positionX+1][self.positionY]=4
            elif:
                if dir==2:
                    if self.positionY!=0:
                        if map[self.positionX][self.positionY-1]==0:
                            map[self.positionX][self.positionY]=0
                            map[self.positionX][self.positionY-1]=4
                elif:
                    if self.positionY!=p-1:
                        if map[self.positionX][self.positionY+1]==0:
                            map[self.positionX][self.positionY]=0
                            map[self.positionX][self.positionY+1]=4



class Gardien:
    """Classe définissant un gardien par sa position(x,y)"""
    def __init__(self,x,y):
        self.positionX=x
        self.positionY=y
    def deplacer(self,map,dir):
        """méthode déplaçant le gardien dans une direction donnée dir€[0,1,2,3] <=> [gauche,droite,haut,bas]"""
