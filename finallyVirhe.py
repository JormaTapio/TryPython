# -*- coding: cp1252 -*-
while True:
    #Pyydetään käyttäjältä luku syötteenä
    luku = input("Anna lukuarvo: ")
    #koitetaan muuttaa syöte lukuarvoksi
    try:
        luku1 = int(luku)
        print("Annoit luvun",luku1)
    #Jos tapahtuu mikä tahansa virhe,
    #lopetetaan hallitusti
    finally:
        print("Ohjelmassa oli virhe, lopetetaan.")
    