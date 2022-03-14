# BP - EX: 13.2

class Maillon :
    '''
        self.valeur : la valeur du Maillon
        self.suivant : La prochain dans la liste 'File'
    '''
    def __init__(self,v) :
        '''
            ...__init__
            v [any]: Valeur du Maillon

            Renvoie rien
        '''
        self.valeur = v
        self.suivant = None

class File : 
    '''
        self.dernier_file : dernier element de la File
    '''
    def __init__(self) :
        '''
            ...__init__

            Renvoie rien
        '''
        self.dernier_file = None 

    def enfile(self,element) : 
        '''
            # self [class]: self
            element [class]: 

            Renvoie rien
        '''
        nouveau_maillon = Maillon(element) 
        nouveau_maillon.suivant = self.dernier_file 
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        '''
            Renvoie vrai si la File est vide et faux si non
        '''
        return self.dernier_file == None 

    def affiche(self) : 
        '''
            affiche les valeurs de la File

            Renvoie rien
        '''
        maillon = self.dernier_file 
        while maillon != None :
            if maillon.suivant != None:
                print(maillon.valeur, end = ' ; ')
            else:
                print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        '''
            defile les valeurs de la File

            Renvoie la dernier element de la File
        '''
        if not self.est_vide() : 
            if self.dernier_file.suivant == None : 
                resultat = self.dernier_file.valeur 
                self.dernier_file = None 
                return resultat 
            maillon = self.dernier_file
            while maillon.suivant.suivant != None : 
                maillon = maillon.suivant 
            resultat = maillon.suivant.valeur
            maillon.suivant = None 
            return resultat 
        return None

# ----------------------------------------------------------------
F = File()

print(F.est_vide()) # ! Returns True

F.enfile(2)
F.affiche() # ! Returns 2

print(F.est_vide()) # ! Returns False

F.enfile(5)
F.enfile(7)
F.affiche() # ! Returns 7 ; 5 ; 2

print(F.defile()) # ! Returns 2

print(F.defile()) # ! Returns 5

F.affiche()
# ! Returns 7

# * Finished! 🎉