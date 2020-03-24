# -*- coding: UTF-8 -*-

def morsseMerkit():
    #Määritellään Morse-koodin aakkoset, numerot ja erikoismerkit.
    aakkoset = {    'a' : '.-',     'p' : '.--.',    'b' : '-...',   'q' : '--.-',
                    'c' : '-.-.',   'r' : '.-.',     'd' : '-..',    's' : '...',   
                    'e' : '.',      't' : '-',       'f' : '..-.',   'u' : '..-',
                    'g' : '--.',    'v' : '...-',    'h' : '....',   'w' : '.--',
                    'i' : '..',     'x' : '-..-',    'j' : '.---',   'y' : '-.--',
                    'k' : '-.-',    'z' : '--..',    'l' : '.-..',   'å' : '.--.-',
                    'm' : '--',     'ä' : '.-.-',    'n' : '-.',     'ö' : '---.',
                    'o' : '---',    'ü' : '..--',    ' ' : ' '  }

    numerot  = {    "0" : " _ _ _ _ _", "1" : ". _ _ _ _",  "2" : "· · _ _ _",
                    "3" : "· · · _ _",  "4" : "· · · · _",  "5" : "· · · · ·",
                    "6" : "_ · · · ·",  "7" : "_ _ · · ·",  "8" : "_ _ _ · ·",
                    "9" : "_ _ _ _ ."   }

    erikoismerkit = {   "?" : " . . _ _ . .",	"/" : " _ . . _ .",
                        "=" : " _ . . . _", 	":" : " _ _ _ . . .",
                        "," : " _ _ . . _ _",	"-" : " _ . . . . _",
                        "(" : " _ . _ _ .",	    ")" : " _ . _ _ . _" ,
                        "." : "._._._"   }

    morssemerkit = aakkoset 
    morssemerkit.update(numerot)
    morssemerkit.update(erikoismerkit)
    return morssemerkit

def morsetus(sana):
    #Määritellään Morse-koodin aakkoset, numerot ja erikoismerkit.
    morssemerkit = morsseMerkit()
    kaannos = ""
    print("Teksti: '",sana,"' on morsekoodina")
    sana = sana.lower()
    for i in range(0,len(sana)):
        kaannos = kaannos + morssemerkit[sana[i]]+"/"
    print(kaannos)

def main():
    laskuri = 0
    sana1 = 'TAPIO MYLLÄRINEN'
    sana2 = "Rakas vaimoni Lea Myllärinen"
    sana3 = "Life is life."
    tupleSanat = sana1,sana2,sana3
    pituus = len(tupleSanat)
    try:
        while (laskuri<pituus):
            teksti = tupleSanat[laskuri]
            morsetus(teksti)
            laskuri = laskuri+1
    except KeyError as e:
        print("Tekstissä:'", teksti, "' merkki",e," puuttuu annetusta morse-koodista.")
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()