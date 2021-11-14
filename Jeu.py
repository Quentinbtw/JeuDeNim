class Moteur :
    
    def __init__ (self, nom1, nom2):
        """
        Initialise le nombres de batons et le joueur qui joue.
        """
        
        self.nbBatons = 21
        self.joueur = 1
        self.nom1 = nom1
        self.nom2 = nom2
        
    def enlever (self, moinsBatons):
        """
        Soustrait le nombre de batons aux batons en jeu
        """
        
        self.nbBatons = self.nbBatons - moinsBatons
        
    def limitation (self, moinsBatons):
        """
        Limite le nombre de batons soustrait entre 1 et 3.
        """
        
        if moinsBatons > 3 or moinsBatons < 1 :
            return False
        
        return True 
    
    def finDeTour (self):
        """
        Vérifie si la partie est terminée et change de joueur.
        """
        if self.nbBatons <= 0:
            return True 
        
        if self.joueur == 2:
            self.joueur = 1
            
        else:
            self.joueur = 2
        
        return False
            

class Console:
    
    def __init__ (self):
        """
        Initialise l'interface utilisateur.
        """
        nom1 = input("Quel est le prénom du joueur 1 ? ")
        nom2 = input("Quel est le prénom du joueur 2 ? ")
        self.jeu = Moteur(nom1, nom2)
        
    def jouer (self):
        """
        Gère la partie.
        """
        print("Tour du joueur " + str(self.jeu.joueur))
        
        print("| " * self.jeu.nbBatons)
        
        moinsBatons = input("Combien de batons voulez vous retirer ? ")
        
        while moinsBatons.isdigit() is False or self.jeu.limitation(int(moinsBatons)) is False :
            
            print("Nombre de batons incorrect")
            moinsBatons = input("Combien de batons voulez vous retirer ? ")
            
        self.jeu.enlever(int(moinsBatons)) 
        
        if self.jeu.finDeTour() :
            
            if self.jeu.joueur == 1 :
                print("LE GRAND GAGNANT EST : " + self.jeu.nom2)
            else:
                print("LE GRAND GAGNANT EST : " + self.jeu.nom1)
            
            return
                
        return self.jouer()
        
        
        
        
        