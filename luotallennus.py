# Tämä ohjelma luo käyttäjän nimeämän tiedoston tallennusta varten kysymällä erikseen tiedoston nimen ja tallenusmuodon.

# -*- coding: UTF-8 -*-

def luoTiedosto():
    while True:
        try:
            nimi = input("Anna haluamasi niminen tallennustiedosto ilman päätettä:")
            paate = input("Anna tiedoston tallennus muoto ilman pistettä:")
            tiedosto = nimi+"."+paate
            kahva = open(tiedosto,"w")
            kahva.close()
            return tiedosto
        except Exception as e:
            print(e)
            print("Jotakin meni mönkään yritä uudelleen.")
            print("Ehkä yritit antaa kiellettyjä merkkejä tiedoston nimessä.")


def main():
    tiedosto = luoTiedosto()
    kahva = open(tiedosto,"r")
    print(kahva)
    kahva.close()

main()
