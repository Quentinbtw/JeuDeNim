from tkinter import *

class Moteur :
    
    def __init__ (self, nom1, nom2, nbBatons, nbBatonsSupp):
        """
        Initialise le nombres de batons et le joueur qui joue.
        """
        
        self.nbBatons = nbBatons
        self.joueur = 1
        self.nom1 = nom1
        self.nom2 = nom2
        self.nbBatonsSupp = nbBatonsSupp
        
        
    def enlever (self, moinsBatons):
        """
        Soustrait le nombre de batons aux batons en jeu
        """
        
        self.nbBatons = self.nbBatons - moinsBatons
        
    def limitation (self, moinsBatons):
        """
        Limite le nombre de batons soustrait entre 1 et 3.
        """
        
        if moinsBatons > self.nbBatonsSupp or moinsBatons < 1 :
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
        nbBatons = input("Avec combien de batons voulez-vous jouer ? ")
        
        while nbBatons.isdigit() is False:
            nbBatons = input("Avec combien de batons voulez-vous jouer ? ")
            
        nbBatonsSupp = input("Combien de batons maximum voulez-vous enlever chaque tour ? ")
        while nbBatonsSupp.isdigit() is False:
            nbBatonsSupp = input("Combien de batons maximum voulez-vous enlever chaque tour ?")
        
        
        self.jeu = Moteur(nom1, nom2, int(nbBatons), int(nbBatonsSupp))
        self.jouer()
        
        
    def jouer (self):
        """
        Gère la partie.
        """
        print("Tour du joueur " + str(self.jeu.joueur))
        
        print("| " * self.jeu.nbBatons)
        
        if self.jeu.joueur == 1:
            moinsBatons = input("Combien de batons voulez vous retirer ? (Tour de " + self.jeu.nom1 + ") ")
            
        else:
            moinsBatons = input("Combien de batons voulez vous retirer ? (Tour de " + self.jeu.nom2 + ") ")
        
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
    

class InterfaceUtilisateur:
    
    def __init__(self, fenetre):
        """
       Initialise ma fenêtre pour le jeu de nim
        """
        
        self.fenetre = fenetre
        self.fenetre.title("Jeu De Nim by... " )
        self.fenetre.attributes("-fullscreen", True)
        self.grandEcran = True
        self.fenetre.bind("<F11>", self.changerFullScreen)
        self.fenetre.geometry("1000x600+200+200")
        self.fenetre.configure(bg='black')
        self.largeur = self.fenetre.winfo_screenwidth()
        self.hauteur = self.fenetre.winfo_screenheight()
        self.nom1 = None
        self.nom2 = None
        self.labelNom = Label(self.fenetre, text="Entrer le nom du joueur 1", bg='black', fg='white')
        self.labelNom.pack()
        self.entreeNom = Entry(self.fenetre)
        self.entreeNom.pack()
        self.fenetre.bind("<Return>", self.enregistrerNom)
        
        
    def changerFullScreen(self, event=None):
        """
        Alterne entre fenêtré et grand écran.
		"""
        
        if self.grandEcran :
            self.fenetre.attributes("-fullscreen", False)
            self.grandEcran = False 
            paddingGauche = int((self.largeur - 1000) / 2)
            paddingHaut = int((self.hauteur - 600) / 2)
            self.fenetre.geometry("1000x600+"+str(paddingGauche)+"+"+str(paddingHaut))
        
        else:
            self.fenetre.attributes("-fullscreen", True)
            self.grandEcran = True
            
    def enregistrerNom(self, event=None):
        """
		Enregistre les noms des participants 
		"""
        
        if self.nom1 is None :
            self.nom1 = self.entreeNom.get()
            self.labelNom.config(text="Entrer le nom du joueur 2")
            self.entreeNom.delete(0,"end")
        else :
            self.nom2 = self.entreeNom.get()
            self.jeu = Moteur(self.nom1, self.nom2, 21, 3)
            self.toutEffacer()
            
    def toutEffacer(self):
        """
		Efface tous les widgets.
		"""
        
        for widget in self.fenetre.winfo_children():
            widget.destroy()
        
            
    

        
fenetre = Tk()
InterfaceUtilisateur(fenetre)
fenetre.mainloop()

        

        
        
        
        