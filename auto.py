# Ohjelmassa käsitellään jäsenmuuttujien ja jäsenfunktioiden kautta taloudessa olevia henkilöautoja.
# -*- coding: UTF-8 -*-

#perus Auto-luokka
class Auto:
    merkki = "Porche"
    ajokilometri = 10000
    kori = "Coupe"
    vari = "Musta"
    malli = "911 Turbo"
    runkonumero = "1234-5678-9012"
    def tiedot(self):
        print("Merkki:",self.merkki)
        print("Ajokilometrit:",self.ajokilometri)
        print("Korimalli:",self.kori, end =" ")
        print("Väri:",self.vari)
        print("Minulla on ",self.malli,"-mallinen auto, jonka runkonumero on ",self.runkonumero,".", sep="")

#hieman keinotekoinen Henkiloauto-luokka vakuutustietojen antamiseksi
class Henkiloauto(Auto):
    vakuutus = "Seisontavakuutus"
    def lisatiedot(self):
       print("Autolla on",self.vakuutus,end=".\n")

#perheen lapsen Leluauto-luokka, jossa määritellään aikaisempien tietojen lisäksi materiaali leluautolle.
class Leluauto(Auto):
    materiaali = "maalattu pelti ja muovi"
    def lisatiedot(self):
        print("Leikkiauton materiaali on",self.materiaali,end=".")

#pääohjelmassa luodaan olemassa olevista autoista listat kaikkien tietojen syöttämiseksi ja hallitsemiseksi
def main():
    #talouden autokohtaiset tiedot
    print("\nTaloudessa olevien autojen tiedot:")
    merkit = ["Porche","Ford", "Peogeot", "Mazda"]
    ajokilometrit = [230000, 145000, 164000, 142000]
    korit = ["Coupe", "Farmari", "Porrasperä", "Coupe"]
    varit = ["Valkoinen", "Vihreä", "Punainen", "Sininen"]
    mallit = ["924S", "Focus", "463", "M3"]
    runkonumerot = ["1234-5678-9876","4334-1278-3034","1894-3477-6056","5334-5678-5078"]
    vakuutukset = ["seisontavakuutus", "seisontavakuutus", "seisontavakuutus","liikennevakuutus"]

    #perheessä autoja kertoo kaikkien autojen kokonaismäärän
    autoja = len(merkit)
    Autot = []
    for kierros in range(0,autoja):
        Auto = "Auto"+str(kierros)
        Autot.append(Auto)
        Autot[kierros] = Henkiloauto()

    for kierros in range(0,autoja):
        Auto = Autot[kierros]
        Auto.merkki = merkit[kierros]
        Auto.ajokilometri = ajokilometrit[kierros]
        Auto.kori = korit[kierros]
        Auto.vari = varit[kierros]
        Auto.malli = mallit[kierros]
        Auto.runkonumero = runkonumerot[kierros]
        Auto.vakuutus = vakuutukset[kierros]
        Autot[kierros] = Auto
        print(kierros+1, end=". ")
        Autot[kierros].tiedot()
        Autot[kierros].lisatiedot()

    #lopuksi käsitellään perheen lapsten rakaimpia leikkiautoja käyttämällä Auto() -luokan perusarvoja päivitettynä Leluauto()-luokan lisätiedoilla
    Villenauto = Leluauto()
    Veetinauto = Leluauto()
    Veetinauto.materiaali = "Dublo-lego ja muovi"
    Veetinauto.merkki = "avoauto"
    Veetinauto.vari = "keltainen"
    print("\nPerheen lapset:")
    print("Villen rakas leluauto oli", end= " ")
    print(Villenauto.vari.lower(),Villenauto.merkki,end=". ")
    Villenauto.lisatiedot()
    print("\nVeetin rakas leluauto oli", end= " ")
    print(Veetinauto.vari.lower(),Veetinauto.merkki,end=". ")
    Veetinauto.lisatiedot()

if __name__ == "__main__":
    main()
