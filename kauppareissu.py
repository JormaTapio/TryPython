# Ohjelma kauppakierroksen tekemiseen ja ostoskorin täyttämiseen eri asiakkailla. Kaikki tiliasiakkaat kuuluvat saman perheeseen.
# Perheen äiti ja isä kuittaavat tilimaksut pois palkkapäiviensä yhteydessä, kun käyvät kaupassa, johon perheenostostili on avattu.
# Asiakasvaihtoehdoluokat ovat tavallinen perittävä emoluokka Asiakas() sekä TiliAsiakas()-, VIPAsiakas()- ja heti MaksavaAsiakas() 
# -luokat.

# -*- coding: UTF-8 -*-

import time
import pickle

#funktio luo tiedoston, jos sitä ei ole olemassa. Tiedosto on tyyppiä nimi ja sen lyhenne.
def valitseMuistio(tiedosto):
    try:
        tiedosto = open(tiedosto,"r")
        tiedosto.close()
    except IOError:
        print("Tiedostoa ei löydy, luodaan tiedosto.")
        tiedosto = open(tiedosto,"w")
        tiedosto.close()

#perus Asiakas()-luokka
class Asiakas:
    """Asiakas -luokka määrittelee koriin kerättävät kauppatavarat"""
    kori = []
    tiedosto = ""
    rahaa = 0
    #lisää ostoskoriin tuotteita
    def lisaa(self):
        esine = input("Mitä laitetaan koriin?: ")
        self.kori.append(esine)

    #kassalle mintäessä tulostetaan korin sisältö
    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,self.kori):
            print(self.kori[i], end = " ")
        print()

    #asiakas lopettaa ostokset valitsemalla kassalle menon (eri tyylisesti kirjoitettujen sanojen "kassa" ja kirjaimen "k" -valinnalla)
    def ostokierros(self):
        while True:
            valinta = input("Lisätäänkö tuote vai mennäänkö kassalle? (Kassa): ")
            if valinta[0:5].lower() == "kassa" or valinta.lower() == "k":
                self.kassalle()
                break
            else:
                self.lisaa()

#TiliAsiakas()-luokka perii Asiakas()-luokan jäsenmuutujat ja -funktiot
class TiliAsiakas(Asiakas):
    """TiliAsiakas -luokka määrittelee koriin ja yhteiselle tilille kerättävät kauppatavarat"""
    #kassa tutkii korin sisällön
    def kassalle(self):
        if self.kori == 0:
            print("Kori on tyhjä.")
        else:
            print("Tilille ostettu seuraavat tuotteet:")
            for i in range(0,len(self.kori)):
                print(self.kori[i], end = " ")
            print()
    
    #tallennetaan tiliostokset tilikohtaiseen tiedostoon
    def tallennus(self,tiedosto):
        kahva = open(tiedosto,"a")
        kori = listaTekstiksi(self.kori)
        if len(kori) == 1:
            kahva.write(kori)
        else:
            kahva.write(", "+kori)     #pilkku lisätään, että tilin velanlaksu helpottuu, kun kaikki tuotteet maksava t yhden rahan
        kahva.close()
    
    #maksaa tilimaksut kuun lopussa palkanmaksun yhteydessä
    def maksaVelka(self,tiedosto):
        kahva = open(tiedosto,"r")
        sisus = kahva.read()
        kahva.close()
        pilkkuja = 0
        for i in range(len(sisus)):
            if sisus[i] == ",":
                pilkkuja += 1
        velat = pilkkuja + 1
        if velat <= self.rahaa:
            print("Tilillä on maksamatta seuraavat kauppatavarat:", sisus)
            print("Rahaa kauppatilillä on velkojen maksun jälkeen", self.rahaa-velat,"rahaa")
            self.kahva = open(tiedosto,"w")
            kahva.close()
        else:
            print("Pankkitilillä ei ole tarpeeksi rahaa tilinvelkojen maksamiseen.")

#MaksavaAsiakas()-luokka perii Asiakas()-luokan jäsenmuutujat ja -funktiot
class MaksavaAsiakas(Asiakas):
    """MaksavaAsiakas -luokka määrittelee koriin kerättävät kauppatavarat, jotka maksetaan heti omista varoista"""
    kori = []
    rahaa = 3
    #MaksavanAsiakas -luokan ostoskierroksen logiikka ei suvaitse desimaalirahoja. 
    #MaksavaAsiakas maksaa aina laskunsa käteisellä tai tilisiirtona ostostapahtuman yhteydessä.
    def kassalle(self):
        ostoksia = len(self.kori) 
        if ostoksia == 0:
            print("Kori on tyhjä.")
        else:
            print("Korissa oli seuraavat tuotteet:")
            for i in range(0,ostoksia):
                print(self.kori[i], end = " ")
            print()
            try:
                if self.rahaa < ostoksia:
                    if self.rahaa < ostoksia:
                        print("\nRahasi riittivät",self.rahaa,"tuotteeseen:")
                        for i in range(0,self.rahaa-1):
                            print(self.kori[i], end = " ")
                        print("ja", self.kori[self.rahaa])
            except TypeError as e:
                print(e)
                print("Taisit unohtaa, että meille käy vain kokonaiset rahat.")
                print("Kauppatavaroiden kokonaishinta on",ostoksia)
                rahaa = int(input("Annatko kokonaisluvun maksaaksensi laskun käyttörahoistasi:"))
                if rahaa >= ostoksia:
                    print("Kiitos maksusta. Palautusta tulee",rahaa-ostoksia,"rahaa.")
            print("Tervetuloa uudelleen.")

#VIPAsiakas() -luokka saa ilmaisen kierroksen Asiakas() -luokan toiminnoilla 
class VIPAsiakas(Asiakas):
    """VIPAsiakas -luokka määrittelee koriin kerättävät ilmaiset kauppatavarat"""
    #VIPAsiakas ei maksa mitään ottamistan tuotteista
    def kassalle(self):
        if len(self.kori) == 0:
            print("Kori on tyhjä.")
        else:
            print("Korissasi ovat seuraavat kauppatavarat:")
            pituus = len(self.kori)
            for i in range(pituus):
                print(self.kori[i], end = " ")
        print("\nVIP-asiakkaat ovat aina tervetulleita. Toivottavasti pidät tuotteistamme!")
        print("Tervetuloa uudelleen.")

#apufunktio listan muuttamiseksi tekstiksi
def listaTekstiksi(list):  
    #alusta teksti ja liitä kaikki listan alkiot vuorollaan teksin jatkoksi 
    teksti = ""  
    for ele in list:  
        teksti += ele + ", "      
    return teksti[0:-2]

#eri asiakasryhmiä kokeillaan ja katsotaan kuinka tiliasiakas ryhmä toimii perheen sisällä
def eriAsiakkaat():
    print("\n*** TiliAsiakas *** ")
    tapsa = TiliAsiakas()
    tapsa.ostokierros()

    print("\n*** TiliAsiakas *** ")
    risto = TiliAsiakas()
    risto.ostokierros()

    print("\n*** MaksavaAsiakas *** ")
    teemu = MaksavaAsiakas()
    teemu.kori = []
    teemu.ostokierros()

    #halutaan osoittaa, ettei desimaaliraha toimi
    print("\n*** MaksavaAsiakas *** ")
    nikolai = MaksavaAsiakas()
    nikolai.rahaa = 1.2
    nikolai.kori = []
    nikolai.ostokierros()

    print("\n*** VIP-asiakas *** ")
    lea = VIPAsiakas()
    lea.kori = []
    lea.ostokierros()

    print("\n*** TiliAsiakas *** ")
    liisa = TiliAsiakas()
    liisa.rahaa = 3
    liisa.ostokierros()

#ohjelmassa luodaan perhekohtainen tiedosto kaupantiliveloille tuotteista
def Kauppareissu():
    """ Ohjelma kysyy asiakkaalta kauppatavarat ja tulostaa ne kassalla. """
    #tiedosto = "myllis.txt"
    #tiedosto = "lyra.txt"
    tiedosto = "lappalainen.txt"
    valitseMuistio(tiedosto)        #varsianinen tilitiedosto luodaan tässä
    asiakasTili = TiliAsiakas()
    eriAsiakkaat()
    
    #tärkein tarkotus vanhemmilla on maksaa jälkeläistensä kaupantilitapahtumat 
    isa = TiliAsiakas()
    isa.rahaa = 3200
    aiti = TiliAsiakas()
    aiti.rahaa = 3100
    aiti.kori = []
    asiakasTili.tallennus(tiedosto)

    #tutkitaan onko tänään vanhempien tilimaksupäivä
    #isä maksaa tilivelat pois jokaisen kuun 1.-5. päivä
    #äiti maksaa tilivelat pois jokaisen kuun 7.-10. päivä
    day = int(time.strftime("%d"))
    if day >= 1 and day <= 5:
        print("\nIsän palkkapäivä on kuun 1. päivä, joten isä maksaa perheen tilivelat pois 1.-5. päivän aikana, jos käy kaupassa.")
        isa.maksaVelka(tiedosto)
    elif day >= 7 and day <= 10:
        print("\nÄitin palkkapäivä on kuun 7. päivä, joten äiti maksaa perheen tilivelat pois 6.-10. päivän aikana, jos käy kaupassa.")
        aiti.maksaVelka(tiedosto)
    else:
        print("Tilimaksut siirtyvät seuraavaan kuun alkuun maksettavaksi.")


Kauppareissu() 

