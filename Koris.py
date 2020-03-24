# Ohjelmassa heitetään korista.
# Samalla harjoitellaan jäsen muuttujien ja funktioiden käyttämstä sekä demotaan ja huomataan private muuttujan hyödyt sekä luokan selitetekstin antaminen.
# -*- coding: UTF-8 -*-
import random

class Kilpailija():
    """Kilpailija: sisältää korit ja nimen"""
    __nimi = ""
    korit = 0
    def __init__(self):
        self.__nimi = input("Anna minulle nimi: ")
        
    def tilanne(self):
        print("Olen",self.__nimi,"ja minulla on",self.korit,"koria!")
        
    def heitto(self):
        self.korit = self.korit + random.randint(0,1)

    def tulos(self):
        print("Tulos:", self.__nimi, ":", self.korit, end = " ")

    def voitto(self):
        print(self.__nimi, "voitti. Hurraa, hurraa ja hurraa voittajalle!")

    def havio(self):
        print(self.__nimi, "hävisit tänään. Aina ei voi voittaa, ei edes joka kerta. Sorry.")
        
def main():
    eka = Kilpailija()
    toka = Kilpailija()
    eka.tilanne()
    toka.tilanne()
    kierrokset = int(input("Anna kierrosten lukumäärä:"))
    while True:
        for i in range(kierrokset-1):
            eka.heitto()
            toka.heitto()
        eka.tulos()
        print(" <==> ", end = "")
        toka.tulos()
        print("\n")
        lopetus = input("Jatketanko heittelyä? (K/E)")
        if lopetus.lower().startswith("k"):
            pass
        else:
            try:
                print("Pelasitte", eka.korit+toka.korit,"heittoa", (eka.korit+toka.korit)/kierrokset,"ja kierrosta")
                if eka.korit > toka.korit:
                    eka. voitto()
                    toka.havio()
                else:
                    eka.havio()
                    toka.voitto()
                break
            except ZeroDivisionError as (e):
                print(e)
                kierrokset = int(input("Anna nollasta poikkeava kierrosten määrä"))
            
if __name__ == "__main__":
    main()