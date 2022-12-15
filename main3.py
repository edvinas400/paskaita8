class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return (f"{self.suma}")

    def __repr__(self):
        return self.suma


class PajamuIrasas(Irasas):
    def __init__(self, suma):
        super().__init__(suma)
        self.siuntejas = input("Iveskite siunteja: ")
        self.papildoma_informacija = input("Iveskite papildoma informacija: ")

    def __str__(self):
        return (f"{self.suma} {self.siuntejas} {self.papildoma_informacija}")


class IslaiduIrasas(Irasas):
    def __init__(self, suma):
        super().__init__(suma)
        self.atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        self.isigyta_preke_paslauga = input("Iveskite isigyta preke/paslauga: ")

    def __str__(self):
        return (f"{self.suma} {self.atsiskaitymo_budas} {self.isigyta_preke_paslauga}")


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        irasas = PajamuIrasas(suma)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, suma):
        irasas = IslaiduIrasas(suma)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        balansas = 0
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                balansas += x.suma
            elif isinstance(x, IslaiduIrasas):
                balansas -= x.suma
        print(balansas)

    def parodyti_ataskaita(self):
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                print("Pajamos", x)
            elif isinstance(x, IslaiduIrasas):
                print("Islaidos", x)


mano = Biudzetas()
while True:
    veiksmas = int(input("""1 - Ivesti pajamas
2 - Ivesti islaidas
3 - Rodyti balansa
4 - Rodyti ataskaita
0 - Iseiti \n"""))
    match veiksmas:
        case 1:
            mano.prideti_pajamu_irasa(int(input("Iveskite suma:")))
        case 2:
            mano.prideti_islaidu_irasa(int(input("Iveskite suma:")))
        case 3:
            mano.gauti_balansa()
        case 4:
            mano.parodyti_ataskaita()
        case 0:
            print("Ate")
            break
        case _:
            print("Neteisingai pasirinktas veiksmas")
