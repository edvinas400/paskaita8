import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def _paskaiciuoti(self):
        x = (datetime.datetime.now() - self.dirba_nuo)
        dienos = x.days
        return dienos

    def paskaiciuoti_atlyginima(self):
        atlyginimas = int(self.ikainis) * 8 * self._paskaiciuoti()
        return atlyginimas


class NormalusDarbuotojas(Darbuotojas):
    def paskaiciuoti_atlyginima(self):
        atlyginimas = super().paskaiciuoti_atlyginima() / 7 * 5
        return atlyginimas


a = Darbuotojas("Stasas", 7, "2021-12-14")
print(a.paskaiciuoti_atlyginima())
b = NormalusDarbuotojas("Sausainis", 8, "2021-12-15")
print(b.paskaiciuoti_atlyginima())
