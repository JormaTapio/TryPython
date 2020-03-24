# Oman kastelujärjestelmän simulointiohjelma
import sys

class Kytkin:
    """Kytkinluokka, joka sisältää Boolean-arvon."""
    __asento = False
    def palauta(self):
        return self.__asento
    def muuta(self):
        if self.__asento == False:
            self.__asento = True
        else:
            self.__asento = False

def paistaako(paiste=True):
    if paiste == "None":
        paistaa = input("Paistaako aurinko Kyllä (K/k)?")
        if paistaa.lower().startswith("k"):
            paistaa = True
        else:
            paistaa = False
    else:
        paistaa = paiste
    return paistaa

def main():
    while True:
        laskuri = 0
        kastelujarjestelma = Kytkin()
        print()
        paistaa = paistaako("None")
        print("Kastelujarjestelmän tila (päällä/ei päällä).")
        kastelujarjestelma.muuta()
        print("Paistaako aurinko?",paistaa)
        print("Onko kastelu päällä?", kastelujarjestelma.palauta())
        
        while True and laskuri != 1:
            ensiviikonsää = {"maanantai" : "k" , "tiistai" : "k" , "keskiviikko" : "k" , "torstai" : "e" , "perjantai" : "e" , "lauantai" : "k" , "sunnuntai" : "k"}
            #päivä,paistaa= ensiviikonsää
            viikonpäivät = ["maanantai", "tiistai", "keskiviikko" , "torstai", "perjantai", "lauantai", "sunnuntai"]
            print("\nEnsiviikon sääennuste:")
            for viikonpaiva in range(7):
                print(viikonpäivät[viikonpaiva],"paistaa",ensiviikonsää[viikonpäivät[viikonpaiva]]=="k")
            print("\nKysy onko kastelujärjestelmä päällä tiettynä viikonpäivänä? \
(maanantai=m , tiistai=ti , keskiviikko=k , torstai=to , perjantai=p , lauantai=l , sunnuntai=s).")
            while True:
                paiva = input("Kysy viikonpäivä?: ")
                paiva = paiva.lower()
                if paiva[0] == "t":
                    paiva = paiva[0:1]
                else:
                    paiva = paiva[0] 
                for viikonpaiva in range(len(viikonpäivät)):
                    if viikonpäivät[viikonpaiva].startswith(paiva):
                        paiva = viikonpäivät[viikonpaiva]
                        break
                laskuri = laskuri + 1    
                print(paiva, "ja aurinko paistaa,vai?", ensiviikonsää[paiva]=="k")
                if laskuri == 3:
                    lopetus = input("Lopetetaanko? L tai l lopettaa: ")
                    if lopetus.lower().startswith("l"):
                        loppu = input("Haluatko lopettaa koko ohjelman? Lopeta L tai l: ")
                        if loppu.lower().startswith("l"):
                            sys.exit()
                        else:
                            laskuri = 1
                            break
                    else:
                        laskuri = 0

        
main()