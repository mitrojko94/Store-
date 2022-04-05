class Proizvod:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} cost {self.price}"

class Zaposleni:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def __str__(self):
        return f"Employee {self.name}\nusername: {self.username}\npassword: {self.password}"

class Prodavnica(Proizvod, Zaposleni):
    def __init__(self, proizvodi, zaposleni):
        self.proizvodi = proizvodi
        self.zaposleni = zaposleni
        self.kasa = 10000 #Suma novca u kasi
        self.uplata = 0 #Trenutna uplata

        #Kreiram jos jedno polje, da bi samo oni koji hoce da se registruju i koju mogu da se uloguju, da pristupe ostalim podacima aplikacije
        self.jePrijavljen = False #Kad se kreira klase nije prijavljen, zato je False
    
    def register_employee(self, Zaposleni):
        self.zaposleni.append(Zaposleni)
    
    def prijava(self, username, password):
        for z in self.zaposleni:
            if z.username == username and z.password == password:
                self.jePrijavljen = True
                print(f"Welcome in system market, {z.name}")
                break
            else:
                print(f"Wrong! Try Again!")
                
    #Provera cena proizvoda
    def upit_cena(self, name):
        for p in self.proizvodi:
            if p.name == name:
                return p
                
        else:
            print("Try Again! We don't have that proisvod!")
    
    def upit_uplata(self, pr):
        novac = 0
        for p in self.proizvodi:
            for pp in pr:
                if pp == p.name:
                    novac += int(p.price) #Stavio sam int, jer je u txt. fajlu kao string, pa da bih pretvorio u int
        
        #print(f"Za uplatu {novac}")
        self.uplata = novac
        return self.uplata
    
    #Pravim ovu metodu da ponistim uplatu, ako korisnik nesto nece da kupi
    def reset(self):
        self.uplata = 0
        print(self.kasa)
    
    def prodaja(self):
        self.kasa += self.uplata
        self.uplata = 0
        print(self.kasa)

proizvodi = [l.strip() for l in open("C:/Users/Darko/Desktop/ITOiP Python/Informacioni sistem prodavnice/Moj rad/proizvodi.txt")]
lista_proizvoda = []

for i in range(len(proizvodi)):
    proizvodi[i] = proizvodi[i].split()
    p = Proizvod(name=proizvodi[i][0], price=proizvodi[i][1])
    lista_proizvoda.append(p)

#Provera da li sam lepo ubacio podatke u listu
# for l in lista_proizvoda:
#     print(l)

zaposleni = []

z1 = Zaposleni(name="Darko", username="mitrojko94", password="firmasi021")
z2 = Zaposleni(name="Zoran", username="kizafirmas", password="mutljavina")

zaposleni.append(z1)
zaposleni.append(z1)

#Provera da li sam lepo ubacio zaposlene u listu
# for l in zaposleni:
#     print(l)

prodavnica = Prodavnica(proizvodi=lista_proizvoda, zaposleni=zaposleni)

# for p in prodavnica.proizvodi:
#     print(p)

# for z in prodavnica.zaposleni:
#     print(z)

#Registrovanje novog zaposlenog
z3 = Zaposleni(name="Nemanja", username="sojka", password="utoka")

prodavnica.register_employee(Zaposleni=z3)

# for z in prodavnica.zaposleni:
#     print(z)

#Da li korisnik postoji
prodavnica.prijava(username="sojka", password="utokaa")

#Provera upita cena
prodavnica.upit_cena(name="jaja")

#Provera uplate
l = ["jaja", "mleko", "sok"]
prodavnica.upit_uplata(pr=l)
#print(prodavnica.kasa)

#Provera reset-a
prodavnica.reset()

#Provera prodaje
prodavnica.prodaja()
#print(prodavnica.kasa)
