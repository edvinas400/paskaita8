class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(metai, modelis, kuro_tipas)

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai ipilti")


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("Vaziuoja autonomiskai")


a = Automobilis(2014, "Nisan Cube", "Benzinas")
b = Elektromobilis(2020, "Volkswagen ID.3", "Elektra")
a.vaziuoti()
a.stoveti()
a.pildyti_degalu()
b.vaziuoti()
b.stoveti()
b.pildyti_degalu()
b.vaziuoti_autonomiskai()
