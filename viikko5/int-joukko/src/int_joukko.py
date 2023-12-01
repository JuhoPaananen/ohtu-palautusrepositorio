KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not self.positiivinen_kokonaisluku(kapasiteetti):
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        self.kapasiteetti = kapasiteetti

        if not self.positiivinen_kokonaisluku(kasvatuskoko):
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def positiivinen_kokonaisluku(self, n):
            return isinstance(n, int) and n > 0
    
    def lista_taynna(self):
        return self.alkioiden_lkm == len(self.ljono)
    
    def numero_listassa(self, n):
        return n in self.ljono
    
    def kasvata_listaa(self):
        taulukko_old = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)

    def kasvata_alkioiden_lkm(self):
        self.alkioiden_lkm = self.alkioiden_lkm + 1

    def vahenna_alkioiden_lkm(self):
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.kasvata_alkioiden_lkm()
            return True
        else:
            pass

        if not self.numero_listassa(n):
            self.ljono[self.alkioiden_lkm] = n
            self.kasvata_alkioiden_lkm()

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.lista_taynna():
                self.kasvata_listaa()
            return True

        return False

    def poista(self, n):
        if self.numero_listassa(n):
            self.ljono.remove(n)
            self.vahenna_alkioiden_lkm()
            self.ljono.append(0)

            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
