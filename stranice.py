from tkinter import *
from klase import *

class PocetnaStranica(Frame):
    def __init__(self, parent, controller): #Ovo su uobicajeni identifikatori(parent, controller)
        Frame.__init__(self, parent)
        self.configure(bg="lightblue") #Celoj stranici stavim bg
        l = Label(self, text="Dobro dosli u prodavnicu Sunce", font=("Times", 40, "bold"), bg="lightblue", fg="red")
        l.pack(pady=250, padx=50)

class Registracija(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Registracija", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        #Stavljam frame da odvojim naslov
        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, text="Ime i prezime", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)
        e1 = Entry(self)
        e1.pack()

        l2 = Label(self, text="Username", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l2.pack(pady=10)
        e2 = Entry(self)
        e2.pack()

        l3 = Label(self, text="Password", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l3.pack(pady=10)
        e3 = Entry(self)
        e3.pack()

        #Stavim command: lambda: ime instance u klase.py i pozovem metodu za registraciju i prosledim kao argument Zaposleni(to je lista nasih zaposlenih) i njemu kao argumente stavim e1.get(), jer uzimam podatke koji su uneti u input polje
        b = Button(self, text="Registruj se", command=lambda: prodavnica.register_employee(Zaposleni=Zaposleni(e1.get(), e2.get(), e3.get())))
        b.pack(pady=30)

class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Login", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, text="Username", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)
        e1 = Entry(self)
        e1.pack()

        l2 = Label(self, text="Password", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l2.pack(pady=10)
        e2 = Entry(self)
        e2.pack()

        #Isto sto sam uradio za klasu Registracija, radim i ovde. Pozovem instancu objekta iz klase.py, prosledim metodu prijava i dodam joj argumente koje ima ta metoda. Stavio sam e1.get(), jer opet, uzimam podatke unete u input polje
        b = Button(self, text="Prijavi se", command=lambda: prodavnica.prijava(username=e1.get(), password=e2.get()))
        b.pack(pady=30)
    
class Cena(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Cena", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, text="Naziv proizvoda", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)
        e1 = Entry(self)
        e1.pack()

        l2 = Label(self, font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l2.pack(pady=10)

        #Ovde sam stavio l2.configure(), jer ta labela nema text i hocu da se u toj labeli(inace, ta labela je ispod prve, samo se ne vidi, nema text) pokaze da li imamo ili nemamo taj proizvod
        b = Button(self, text="Proveri", command=lambda: l2.configure(text=f"{prodavnica.upit_cena(name=e1.get())} dinara"))
        b.pack(pady=30)

class Uplata(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Uplata", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, text="Naziv proizvoda", font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)
        e1 = Entry(self)
        e1.pack()

        l2 = Label(self, font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l2.pack(pady=10)

        #Prazna lista proizvoda(pr) gde cu da dodajem moje podatke
        pr = []

        #Stavio sam kao command da dodajem sve unete podatke(unete u input polje) u tu listu. Tome sluzi ova komanda pr.append(e1.get())
        b = Button(self, text="Dodaj", command=lambda: pr.append(e1.get()))
        b.pack(pady=20)

        #Pravim f-ju koja ce da prihvata neodredjen broj args i kwargs(kljucne reci)
        def funkcije(*funcs): #Ovo *funcs je isto kao i *args i **kwargs
            def func(*args, **kwargs):
                #Za svaku f-ju iz nepoznatog broja f-ja(misli se za svako f u funcs)
                for f in funcs:
                    f(*args, **kwargs)
            return func
        
        def prazni_listu(l):
            del l[:]

        b1 = Button(self, text="Suma", command=lambda: funkcije(l2.configure(text=f"Za uplatu {prodavnica.upit_uplata(pr=pr)} dinara"), prodavnica.upit_uplata(pr=pr), prazni_listu(l=pr)))
        b1.pack()

class Prodaja(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Prodaja", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)

        b = Button(self, text="Racun?", command=lambda: l1.configure(text=f"Racun: {prodavnica.uplata} dinara"))
        b.pack(pady=20)

        b1 = Button(self, text="Potvrdi", command=lambda: prodavnica.prodaja())
        b1.pack()

class Reset(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        l = Label(self, text="Reset", font=("Times", 20, "bold"), bg="lightblue", fg="red")
        l.pack(pady=10, padx=50)

        f = Frame(self, width=1200, height=2, relief=SUNKEN) #SUNKEN, da imamo udubljenje
        f.pack(pady=10)
        l = Label(self, bg="lightblue")
        l.pack(pady=50)

        l1 = Label(self, font=("Times", 16, "bold"), bg="lightblue", fg="red")
        l1.pack(pady=10)

        b = Button(self, text="Potvrdi", command=lambda: prodavnica.reset())
        b.pack(pady=10)
