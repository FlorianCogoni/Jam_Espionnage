"""Le "code" de la map est definit comme suivant : [0,1,2,3,4,5] <=> [libre,mur,arrivee,gardien,personnage,champ de vision]"""
n=5
p=5
class Personnage:
    """Classe definissant le personnage par sa potition (x,y)"""


    def __init__(self,x,y):
        self.positionX=x
        self.positionY=y


    def DeplacerPersonnage(self,map,dir):
        """methode deplacant le personnage dans une direction donnee dir appartient a [0,1,2,3] <=> [gauche,droite,haut,bas]
        et on tient compte de la presence eventuelle de murs et des effets de bords"""
        """map est une matrice np"""
        if dir==0:
            if self.positionY!=0:
                """on verifie que le personnage n'est pas sur le bord de la map"""
                if map[self.positionX][self.positionY-1]==0 & map[self.positionX][self.positionY-1]!=1:
                    """on verifie que la cas ou il veut aller est libre et n'est pas un mur"""
                    map[self.positionX][self.positionY]=0
                    map[self.positionX][self.positionY-1]=4
                    self.positionY-=1
        elif dir==1:
            if self.positionY!=p-1:
                """on verifie que le personnage n'est pas sur le bord de la map"""
                if map[self.positionX][self.positionY+1]==0 & map[self.positionX][self.positionY+1]!=1:
                    """on verifie que la cas ou il veut aller est libre et n'est pas un mur"""
                    map[self.positionX][self.positionY]=0
                    map[self.positionX][self.positionY+1]=4
                    self.positionY+=1
        elif dir==2:
            if self.positionX!=0:
                """on verifie que le personnage n'est pas sur le bord de la map"""
                if map[self.positionX-1][self.positionY]==0 & map[self.positionX-1][self.positionY]!=1:
                    """on verifie que la cas ou il veut aller est libre et n'est pas un mur"""
                    map[self.positionX][self.positionY]=0
                    map[self.positionX-1][self.positionY]=4
                    self.positionX-=1
        elif self.positionX!=n-1:
            """on verifie que le personnage n'est pas sur le bord de la map"""
            if map[self.positionX+1][self.positionY]==0 & map[self.positionX+1][self.positionY]!=1:
                """on verifie que la cas ou il veut aller est libre et n'est pas un mur"""
                map[self.positionX][self.positionY]=0
                map[self.positionX+1][self.positionY]=4
                self.positionX+=1



class Gardien:
    """Classe definissant un gardien par sa position(x,y)"""


    def __init__(self,x,y,pattern,view,pattleng):
        """pattern est le tableau de longueur r definissant la routine du gardien: pattern=[0,1,2,2,1,1,1,3] <=> [avancer a gauche d'un cran,...]"""
        """view est l'entier definissant le champ de vision du gardien"""
        """indice est l'entier definissant le deplacement effectue"""
        """pattleng est la longueur de la liste pattern"""
        """orientation est l'entier definissant la direction dans laquelle regarde le gardien"""
        self.positionX=x
        self.positionY=y
        self.pattern=pattern
        self.indice=0
        self.view=view
        self.pattleng=pattleng
        self.orientation=1
        self.cramer=0


    def DeplacerGardien(self,map):
        """methode deplacant le gardien dans une direction donnee dir appartient a [0,1,2,3] <=> [gauche,droite,haut,bas]"""
        if self.indice==self.pattleng-1:
            self.indice=0
        else:
            self.indice+=1
        if self.pattern[self.indice]==0:
            if map[self.positionX][self.positionY-1]!=4:
                map[self.positionX][self.positionY]=0
                map[self.positionX][self.positionY-1]=3
                self.positionY-=1
                if self.indice==self.pattleng-1:
                    self.orientation=self.pattern[0]
                else:
                    self.orientation=self.pattern[self.indice+1]
            else:
                self.cramer=1
        elif self.pattern[self.indice]==1:
            if map[self.positionX][self.positionY+1]!=4:
                map[self.positionX][self.positionY]=0
                map[self.positionX][self.positionY+1]=3
                self.positionY+=1
                self.orientation=1
                if self.indice==self.pattleng-1:
                    self.orientation=self.pattern[0]
                else:
                    self.orientation=self.pattern[self.indice+1]
            else:
                self.cramer=1
        elif self.pattern[self.indice]==2:
            if map[self.positionX-1][self.positionY]!=4:
                map[self.positionX][self.positionY]=0
                map[self.positionX-1][self.positionY]=3
                self.positionX-=1
                self.orientation=2
                if self.indice==self.pattleng-1:
                    self.orientation=self.pattern[0]
                else:
                    self.orientation=self.pattern[self.indice+1]
            else:
                self.cramer=1
        elif self.pattern[self.indice]==3:
            if map[self.positionX+1][self.positionY]!=4:
                map[self.positionX][self.positionY]=0
                map[self.positionX+1][self.positionY]=3
                self.positionX+=1
                self.orientation=3
                if self.indice==self.pattleng-1:
                    self.orientation=self.pattern[0]
                else:
                    self.orientation=self.pattern[self.indice+1]
            else:
                self.cramer=1


def arrivee(persoX,persoY):
    X_arrivee=4
    Y_arrivee=2
    fin=False
    if persoX==X_arrivee:
        if persoY==Y_arrivee:
            fin=True
    return(fin)

def InChamp(personnage,gardien,map):
    EstDansLeChamp=0
    ChampTemporaire=gardien.view
    curseur=1
    if gardien.orientation==0:
        """on verifie que le champ de vision ne sort pas de la map"""
        if gardien.positionY-gardien.view<0:
            ChampTemporaire+=gardien.positionY-gardien.view
        """on verifie si on a pas un mur dans le champ de vision pour eviter les "fausses" comparaisons"""
        while gardien.positionY-curseur>-1 & curseur<=ChampTemporaire:
            if map[gardien.positionX][gardien.positionY-curseur]==1:
                ChampTemporaire=gardien.view-curseur
            else:
                curseur+=1
        if personnage.positionY<=gardien.positionY-1:
            if personnage.positionY>=gardien.positionY-ChampTemporaire:
                if personnage.positionX==gardien.positionX:
                    EstDansLeChamp=1
    else:
        if gardien.orientation==1:
            """on verifie que le champ de vision ne sort pas de la map"""
            if gardien.positionY+gardien.view>p-1:
                ChampTemporaire-=gardien.positionY+gardien.view-(p-1)
                """on verifie si on a pas un mur dans le champ de vision pour eviter les "fausses" comparaisons"""
                while gardien.positionY+curseur<p & curseur<=ChampTemporaire:
                    if map[gardien.positionX][gardien.positionY+curseur]==1:
                        ChampTemporaire=gardien.view-curseur
                    else:
                        curseur+=1
                        if personnage.positionY<=gardien.positionY+ChampTemporaire:
                            if personnage.positionY>=gardien.positionY+1:
                                if personnage.positionX==gardien.positionX:
                                    EstDansLeChamp=1
        else:
            if gardien.orientation==2:
                """on verifie que le champ de vision ne sort pas de la map"""
                if gardien.positionX-gardien.view<0:
                    ChampTemporaire+=gardien.positionX-gardien.view
                    """on verifie si on a pas un mur dans le champ de vision pour eviter les "fausses" comparaisons"""
                    while gardien.positionX-curseur>-1 & curseur<=ChampTemporaire:
                        if map[gardien.positionX-curseur][gardien.positionY]==1:
                            ChampTemporaire=gardien.view-curseur
                        else:
                            curseur+=1
                            if personnage.positionX<=gardien.positionX-1:
                                if personnage.positionX>=gardien.positionX-ChampTemporaire:
                                    if personnage.positionY==gardien.positionY:
                                        EstDansLeChamp=1
            else:
                if gardien.orientation==3:
                    """on verifie que le champ de vision ne sort pas de la map"""
                    if gardien.positionX+gardien.view>n-1:
                        ChampTemporaire-=gardien.positionX+gardien.view-(n-1)
                        """on verifie si on a pas un mur dans le champ de vision pour eviter les "fausses" comparaisons"""
                        while gardien.positionX+curseur<n & curseur<=ChampTemporaire:
                            if map[gardien.positionX+curseur][gardien.positionY]==1:
                                ChampTemporaire=gardien.view-curseur
                            else:
                                curseur+=1
                                if personnage.positionX<=gardien.positionX+ChampTemporaire:
                                    if personnage.positionX>=gardien.positionX+1:
                                        if personnage.positionY==gardien.positionY:
                                            EstDansLeChamp=1
    return(EstDansLeChamp)




def afficher_matrice(m):
    for i in range(len(m)):
        print(m[i])
        print("\n")

def essaie():
    reperer=0
    fin=False
    gardien=Gardien(1,1,[2,1,1,1,3,3,0,0,0,2],2,10)
    personnage=Personnage(0,0)
    map=[[4,0,0,0,0],[0,3,0,0,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    afficher_matrice(map)
    while reperer==0 and not(fin):
        print(fin,reperer)
        x=input()
        personnage.DeplacerPersonnage(map,x)
        reperer=InChamp(personnage,gardien,map)
        reperer+=gardien.cramer
        gardien.DeplacerGardien(map)
        reperer=InChamp(personnage,gardien,map)
        reperer+=gardien.cramer
        fin=arrivee(personnage.positionX,personnage.positionY)
        afficher_matrice(map)
    if not(fin):
        print("Perdu !")
    else:
        print("Bravo !")



essaie()
