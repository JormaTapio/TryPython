# Ohjelmalla tulostetaan eri asiakkaiden maksutietoja antamalla kullekin asiakkaalle omiatietoja täydentämään oletusarvoja.
# laskutus() -ohjelma toimii main() -ohjelmana.

# -*- coding: UTF-8 -*-

class Asiakas():
    nimi = "Matti Meikäläinen"
    loppusumma = 0
    maksutapa = "Luottokortti"                              # Luottokortti tai Käteinen
    viitenumero = "1234-5678-9012345"
    def tiedot(self):
         print("Nimi: ",self.nimi)
         print("Loppusumma: ",self.loppusumma)
         print("Maksutapa: ",self.maksutapa, end =" ")
         if self.maksutapa == "Käteinen":
            return "Great job!\n"
         else:
            print("Viitenumero: ",self.viitenumero)
            return ""

def laskutus():                                            # laskutus() = main()
    matti = Asiakas()
    print(matti.tiedot())

    tapsa = Asiakas()
    tapsa.nimi = "Tapio Meikäläinen"
    tapsa.loppusumma = 1000
    tapsa.maksutapa = "Käteinen"
    print(tapsa.tiedot())

    lissu = Asiakas()
    lissu.nimi = "Liisa Lappalainen"
    lissu.viitenumero = "4321-5678-9012345"
    print(lissu.tiedot())

laskutus()