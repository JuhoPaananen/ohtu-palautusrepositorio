from enum import Enum
from tkinter import ttk, constants, StringVar

class Summa:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus._edelliset_arvot.append(self.sovellus.arvo())
        arvo = self.lue_syote()
        self.sovellus.plus(arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.sovellus._edelliset_arvot.pop())

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus._edelliset_arvot.append(self.sovellus.arvo())
        arvo = self.lue_syote()
        self.sovellus.miinus(arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.sovellus._edelliset_arvot.pop())

class Nollaus:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus._edelliset_arvot.append(self.sovellus.arvo())
        self.sovellus.nollaa()

    def kumoa(self):
        self.sovellus.aseta_arvo(self.sovellus._edelliset_arvot.pop())


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._edelliset_komennot = []

        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(self._sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(self._sovellus, self._lue_syote)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovellus.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return int(self._syote_kentta.get())

    def _suorita_komento(self, komento):
        if komento != Komento.KUMOA:
            komento_olio = self._komennot[komento]
            komento_olio.suorita()
            print(self._sovellus.arvo())
            self._edelliset_komennot.append(komento_olio)
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            if self._edelliset_komennot:
                viimeisin_komento = self._edelliset_komennot.pop()
                viimeisin_komento.kumoa()
                print(self._sovellus.arvo())
                if not self._edelliset_komennot:
                    self._kumoa_painike["state"] = constants.DISABLED

        if self._sovellus.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._arvo_var.set(self._sovellus.arvo())
        self._syote_kentta.delete(0, constants.END)
        
