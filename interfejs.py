from stranice import *
from klase import *

#Kreiram klasu, koja je glavna za nas interfejs
class GUI(Tk):
    def __init__(self, *args, **kwargs): #args se odnosi na neogranicen broj parametara koji se prosledjuju, a nisu neke kljucne reci, a kwargs se odnosi na neogranicen broj parametara koji se mogu proslediti, ali su kljucne reci(keywords)
        Tk.__init__(self, *args, **kwargs)
        self.title("Prodavnica Sunce")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.stranice = {}

        meni = Menu(container)

        #zm - zaposleni meni
        zm = Menu(meni, tearoff=0)
        meni.add_cascade(menu=zm, label="Zaposleni")
        zm.add_command(label="Registracija", command=lambda: self.prikazi_stranicu(Registracija))
        zm.add_command(label="Login", command=lambda: self.prikazi_stranicu(Login))
        zm.add_separator()
        zm.add_command(label="Izlaz", command=self.destroy)

        #prm - proizvod meni
        prm = Menu(meni, tearoff=0)
        meni.add_cascade(menu=prm, label="Proizvodi")
        # prm.add_command(label="Dodaj")
        # prm.add_command(label="Izbaci")
        # prm.add_separator()
        prm.add_command(label="Cena", command=lambda: self.provera(Cena))
        prm.add_command(label="Uplata", command=lambda: self.provera(Uplata))
        prm.add_command(label="Prodaja", command=lambda: self.provera(Prodaja))
        prm.add_separator()
        prm.add_command(label="Reset", command=lambda: self.provera(Reset)) #Ovo prodavnica je uvezeno iz klase.py, a ona ima metodu reset() koju mogu da pozovem

        Tk.config(self, menu=meni)

        for s in (PocetnaStranica, Registracija, Login, Cena, Uplata, Prodaja, Reset):
            stranica = s(container, self)
            self.stranice[s] = stranica
            stranica.grid(row=0, column=0, sticky="nsew")
        
        self.prikazi_stranicu(PocetnaStranica)

    def prikazi_stranicu(self, cont):
        stranica = self.stranice[cont]
        stranica.tkraise() #Izvlaci konkretnu stranicu u prozor
    
    #Metoda koja proverava da li je neki korisnik prijavljen ili ne
    def provera(self, cont):
        if prodavnica.jePrijavljen == True:
            self.prikazi_stranicu(cont=cont)
        else:
            print("Pristup zabranjen!")

#Kreiram objekat klase GUI
IS = GUI()
IS.geometry("1200x600") #Navode se dimenzije pod stringom
IS.mainloop()