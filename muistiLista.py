# Muistikirja, joka käyttää hyväksi Pythonin listaa ja tallentaa sen ohjelman lopuksi tiedostoon "muistio.dat". 
# Kyseinen muistio ladataan ohjelman alussa tai luodaan, jos sitä ei ole tai tapahtuu virhe tiedoston lukemisessa.
# 1) Ohjelmaan voidaan lisätä merkintöjä, joissa on aikaleima.
# 2) Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
# 3) Ohjelmalla voi poistaa yksittäisen merkinnän listalta.
# 4) Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa valitussa tiedostossa.

from time import strftime
import pickle

#ohjaa käyttäjää antamaan luvun
def LuvunTarkistaja(luku=0):
    while True:
        try:
            if (luku.isdigit() == True):
                lukuarvo = int(luku)
            else:
                lukuarvo = int(input("Anna lukuarvo: "))
            return lukuarvo
        except Exception as e:
            print(e)
            print("Virheellinen arvo, yritä uudestaan.")

#muistion runko eri vaihtoehtoineen
def Valinta(lista,file):
    try:
        while True:
            try:
                print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta\n")
                valinta = input("Mitä haluat tehdä?:")
                valinta = LuvunTarkistaja(valinta)
                #(1) Lue muistikirjaa
                if valinta == 1:                                
                    for merkinta in range(len(lista)):
                        print(lista[merkinta])
                #(2) Lisää merkintä
                elif valinta == 2:
                    tieto = input("Kirjoita uusi merkintä: ")
                    lisays = tieto+":::"+strftime("%X %x")         #tulostus formaatti: 00:58:25 03/10/20
                    lista.append(lisays)
                #(3) Muokkaa merkintää
                elif valinta == 3:
                    print("Listalla on",len(lista),"merkintää.")
                    #Listan ensimmäinen numero on 0. 
                    monesko = int(input("Mitä niistä muutetaan?:"))-1
                    print(lista[monesko])
                    lista.pop(monesko)
                    muutos = input("Anna uusi teksti: ")
                    muutos = muutos+":::"+strftime("%X %x")
                    lista.insert(monesko,muutos)
                #(4) Poista merkintä    
                elif valinta == 4:
                    print("Listalla on", len(lista),"merkintää.")
                    poisto = int(input("Mitä niistä poistetaan?:"))-1
                    print("Poistettiin merkintä",lista.pop(poisto))
                #(5) Tallenna ja lopeta
                elif valinta == 5:
                    try:
                        print("Lopetetaan.")
                        kahva = open(file,"wb")              #kirjoitustila,mikäli tiedostoa ei löydy sellainen luodaan 
                        kahva.close()                        #tai kirjoitetaan sen perään (tietoa bittiarvoina)
                        pickle.dump(lista, kahva) 
                        break
                    except IOError as e:
                        print(e)
                else:
                    print("Väärä valinta")
            except TypeError as e:
                print(e)
    except Exception as e:
        print(e)    
        
def Muistiinpanoja():
    try:
        file = "muistio.dat"
        kahva = open(file,"rb")
        tiedosto = pickle.load(kahva)                        #ladataan muistio.dat (datatiedosto)       
        kahva.close()
        lista = tiedosto
        Valinta(lista,file)
    except FileNotFoundError:
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
        kahva = open(file,"wb")
        kahva.close()
        lista = []
        Valinta(lista,file)
   # except EOFError as e:
    #    print(e)
     #   print("Vanha tiedosto on korruptpoitunut. Poista se käsin.")
      #  print("Mahdollisesti et sulkenut Muistiinpajoja -ohjelmaa viimeksi 5. valinnan kautta.")
    else:
        Valinta(lista,file)
        
if __name__=="__main__":
    Muistiinpanoja()
        