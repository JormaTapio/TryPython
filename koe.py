# satunnaisluvun  generointi syöttäjän antamalta väliltä
import random

def lukuFunktio(alaraja,ylaraja):
    
    luku = random.randint(alaraja,ylaraja)
    print("Generoin sinulle luvun ",luku)

def main():
    while True:
        ylaraja = int(input("Anna random-lukujen yläraja: "))
        alaraja =  int(input("Anna random-luklujen alaraja: "))
        lukuFunktio(alaraja,ylaraja)
        jatko = input("Lopeta lopettaa ")
        if jatko == "Lopeta":
            break

if __name__=="__main__":
    main()  # -*- coding: cp1252 -*-

  from random import randint
  import sys

  def lukupeli():
      luku = randint(0,100)
      while True:
          
          syote = int(input("Anna luku 0-100 väliltä: "))
          if syote < 0:
              print("Virheellinen syöte!")
              print("Lopetetaan.")
              sys.exit(0)
          if syote == luku:
              print("Arvasit oikein!")
              break
          elif syote < luku:
              print("Luku on suurempi.")
          else:
              print("Luku on pienempi.")

  if __name__ == "__main__":
  # -*- coding: cp1252 -*-

  from random import randint
  import sys

  def lukupeli():
      luku = randint(0,100)
      while True:
          
          syote = int(input("Anna luku 0-100 väliltä: "))
          if syote < 0:
              print("Virheellinen syöte!")
              print("Lopetetaan.")
              sys.exit(0)
          if syote == luku:
              print("Arvasit oikein!")
              break
          elif syote < luku:
              print("Luku on suurempi.")
          else:
              print("Luku on pienempi.")

  if __name__ == "__main__":
       lukupeli()  # -*- coding: cp1252 -*-

  from random import randint
  import sys

  def lukupeli():
      luku = randint(0,100)
      while True:
          
          syote = int(input("Anna luku 0-100 väliltä: "))
          if syote < 0:
              print("Virheellinen syöte!")
              print("Lopetetaan.")
              sys.exit(0)
          if syote == luku:
              print("Arvasit oikein!")
              break
          elif syote < luku:
              print("Luku on suurempi.")
          else:
              print("Luku on pienempi.")

  if __name__ == "__main__":
       lukupeli()  # -*- coding: cp1252 -*-

  from random import randint
  import sys

  def lukupeli():
      luku = randint(0,100)
      while True:
          
          syote = int(input("Anna luku 0-100 väliltä: "))
          if syote < 0:
              print("Virheellinen syöte!")
              print("Lopetetaan.")
              sys.exit(0)
          if syote == luku:
              print("Arvasit oikein!")
              break
          elif syote < luku:
              print("Luku on suurempi.")
          else:
              print("Luku on pienempi.")

  if __name__ == "__main__":
       lukupeli()  def verolaskuri(palkka,prosentti):
      """Vastaanottaa palkan (int) ja veroprosentin (0-100)
      palauttaa paluuarvona loppusumman kokonaislukuna """
  
      loppusumma = (palkka * ((100 - prosentti) / 100)) 
      return loppusumma  def verolaskuri(palkka,prosentti):
      palauttaa paluuarvona loppusumman kokonaislukuna """
  
      loppusumma = (palkka * ((100 - prosentti) / 100)) 
      """Vastaanottaa palkan (int) ja veroprosentin (0-100)
      return loppusumma
Uusi tiedostonluku:
  def verolaskuri(palkka,prosentti):
      """Vastaanottaa palkan (int) ja veroprosentin (0-100)
      palauttaa paluuarvona loppusumman kokonaislukuna """
  
      loppusumma = (palkka * ((100 - prosentti) / 100)) 
      return loppusumma
Uusi tiedostonluku:
  def verolaskuri(palkka,prosentti):
      """Vastaanottaa palkan (int) ja veroprosentin (0-100)
      palauttaa paluuarvona loppusumman kokonaislukuna """
  
      loppusumma = (palkka * ((100 - prosentti) / 100)) 
      return loppusumma

Uusi tiedostonluku:
  def verolaskuri(palkka,prosentti):
      """Vastaanottaa palkan (int) ja veroprosentin (0-100)
      palauttaa paluuarvona loppusumman kokonaislukuna """
  
      loppusumma = (palkka * ((100 - prosentti) / 100)) 
      return loppusumma

Uusi tiedostonluku:
  # -*- coding: cp1252 -*-

  import omamoduuli
  
  def main():
      palkka = int(input("Anna kuukausipalkka: "))
      vero = int(input("Anna veroprosentti (0-100): "))

      loppusumma = omamoduuli.verolaskuri(palkka,vero)

      print("Sinulle jää käteen", loppusumma,"euroa.")

  if __name__ == "__main__":
      main()

Uusi tiedostonluku:
  # -*- coding: cp1252 -*-

  import omamoduuli
  
  def main():
      palkka = int(input("Anna kuukausipalkka: "))
      vero = int(input("Anna veroprosentti (0-100): "))

      loppusumma = omamoduuli.verolaskuri(palkka,vero)

      print("Sinulle jää käteen", loppusumma,"euroa.")

  if __name__ == "__main__":
      main()

Uusi tiedostonluku1:
  # -*- coding: cp1252 -*-

  import omamoduuli
  
  def main():
      palkka = int(input("Anna kuukausipalkka: "))
      vero = int(input("Anna veroprosentti (0-100): "))

      loppusumma = omamoduuli.verolaskuri(palkka,vero)

      print("Sinulle jää käteen", loppusumma,"euroa.")

  if __name__ == "__main__":
      main()

Uusi tiedostonluku1:
  # -*- coding: cp1252 -*-

  def otaluku():
      luku = input("Anna lukuarvo: ")
      return luku

  def main():
      luku1 = otaluku()
      luku2 = otaluku()
      try:
          tulos = int(luku1) / int(luku2)

      except ZeroDivisionError:
          print("Nollalla ei voi jakaa.")
  
      except (TypeError, ValueError):
          print("Kirjaimilla ei voi laskea.")

      else:
          print("Tulos on",tulos)

  if __name__ == "__main__":
      main()

Uusi tiedostonluku1:
  # -*- coding: cp1252 -*-

  #Pyydetään käyttäjältä luku syötteenä
  luku = input("Anna lukuarvo: ")

  #koitetaan muuttaa syöte lukuarvoksi
  try:
      luku = int(luku)
      print("Annoit luvun",luku)
  #Jos tapahtuu mikä tahansa virhe,
  #lopetetaan hallitusti
  finally:
      print("Ohjelmassa oli virhe, lopetetaan.")

Uusi tiedostonluku1:
 # -*- coding: cp1252 -*-
 #Pyydetään käyttäjältä luku syötteenä
 luku = input("Anna lukuarvo: ")
 #koitetaan muuttaa syöte lukuarvoksi
 try:
     luku = int(luku)
     print("Annoit luvun",luku)
 #Jos tapahtuu mikä tahansa virhe,
 #lopetetaan hallitusti
 finally:
     print("Ohjelmassa oli virhe, lopetetaan.")

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
#Pyydetään käyttäjältä luku syötteenä
luku = input("Anna lukuarvo: ")
#koitetaan muuttaa syöte lukuarvoksi
try:
    luku = int(luku)
    print("Annoit luvun",luku)
#Jos tapahtuu mikä tahansa virhe,
#lopetetaan hallitusti
finally:
    print("Ohjelmassa oli virhe, lopetetaan.")

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
def luvunpyytaja():
    while True:
        try:
            lukuarvo = input("Anna lukuarvo: ")
            lukuarvo = float(lukuarvo)
            return lukuarvo
        except Exception:
            print("Virheellinen arvo, yritä uudestaan.")
def main():
    print("Anna kokonaispalkka euroina")
    palkka = luvunpyytaja()
    print("Anna veroprosentti (0-100)")
    veroprosentti = luvunpyytaja()
    kateen = palkka * ((100 - veroprosentti) / 100)
    print("Sinulle jää",kateen,"euroa.")
if __name__ == "__main__":
    main()

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
def morsetus(sana):
    #Määritellään joitain Morse-koodin aakkosia
    aakkoset = { 'a' : '.-', 'b' : '-...',
                 'c' : '-.-.', 'd' : '-..',
                 'e' : '.', 'f' : '..-.',
                 'g' : '--.', 'h' : '....',
                 'i' : '..', 'j' : '.---',
                 'k' : '-.-', 'l' : '.-..'}
    kaannos = ""
    for i in range(0,len(sana)):
        kaannos = kaannos + aakkoset[sana[i]]+"/"
    print("Sana",sana,"on morsekoodina")
    print(kaannos)
sana_1 = "lakki"
sana_2 = "elegia"
morsetus(sana_1)
morsetus(sana_2)

Uusi tiedostonluku1:
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

Uusi tiedostonluku1:
-*- coding: cp1252 -*-
class toimitus:
    """Luokka määrittelee toimitettavat esineet"""
  
    nimi = ""
    osoite = ""
def lisaa():
    asiakas = input("Asiakkaan nimi:")
    paikka = input("Anna toimitusosoite:")
    paketti = toimitus()
    paketti.nimi = asiakas
    paketti.osoite = paikka
    return paketti

def main():

    kierros = []
    maara = int(input("Kuinka monta toimitusta?:"))
    for i in range(0,maara):
        toimitus = lisaa()
        kierros.append(toimitus)
    print("Vierailtavat paikat:")
    
    for i in range(0,maara):
        print(kierros[i].nimi+":"+kierros[i].osoite)
if __name__ == "__main__":
    main()

Uusi tiedostonluku1:
class Asiakas:
    nimi = "Matti Meikäläinen"
    loppusumma = 0
    maksutapa = "Luottokortti"
    viitenumero = "1234-5678-9012345"
    def tiedot(self):
         print("Nimi: ",self.nimi)
         print("Loppusumma: ",self.loppusumma)
         print("Maksutapa: "self.maksutapa", end =" ")
         print("Viitenumero: ",self.viitenumero)

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
class asiakas:
    """Luokka määrittelee toimitettavat esineet"""
    
    kori = []
    def lisaa(self):
        esine = input("Mitä laitetaan koriin?: ")
        self.kori.append(esine)

    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end = " ")
def main():
    henkilo = asiakas()
    while True:
        valinta = input("Lisätäänkö tuote vai mennäänkö\
kassalle?: ")
        if valinta == "kassalle":
            henkilo.kassalle()
            break
        else:
            henkilo.lisaa()
if __name__ == "__main__":
    main()

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
class asiakas:
    """Luokka määrittelee toimitettavat esineet"""
    
    kori = []
    def lisaa(self):
        esine = input("Mitä laitetaan koriin?: ")
        self.kori.append(esine)

    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end = " ")
def main():
    henkilo = asiakas()
    while True:
        valinta = input("Lisätäänkö tuote vai mennäänkö\
kassalle?: ")
        if valinta == "kassalle":
            henkilo.kassalle()
            break
        else:
            henkilo.lisaa()
if __name__ == "__main__":
    main()

Uusi tiedostonluku1:
class Asiakas:
    nimi = "Matti Meikäläinen"
    loppusumma = 0
    maksutapa = "Luottokortti"
    viitenumero = "1234-5678-9012345"
    def tiedot(self):
        print("Nimi: ",self.nimi)
        print("Loppusumma: ",self.loppusumma)
        print("Maksutapa: "self.maksutapa", end =" ")
        print("Viitenumero: ",self.viitenumero)

Uusi tiedostonluku1:
class KantaAsiakas(Asiakas):
    bonuskortti = "ABCD-1234"
    bonustili = 0
    def kantatiedot(self):
         print("Asiakkaalla on",self.bonustili,"bonuseuroa.")

Uusi tiedostonluku1:
# -*- coding: cp1252 -*-
class asiakas:
    """Luokka määrittelee toimitettavat esineet"""
       kori = []
    def lisaa(self):
        esine = input("Mitä laitetaan koriin?: ")
        self.kori.append(esine)
    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end = " ")

class maksava_asiakas(asiakas):
    rahaa = 2
    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end = " ")
        if self.rahaa < len(self.kori):
            print("\nRahasi eivät kuitenkaan riittäneet \
kuin näihin:")
            print(self.kori[0],self.kori[1])
def main():
    henkilo = maksava_asiakas()
    while True:
        valinta = input("Lisätäänkö tuote vai \
mennäänkö kassalle?: ")
        if valinta == "kassalle":
            henkilo.kassalle()
            break
        else:
            henkilo.lisaa()
if __name__ == "__main__":
    main()