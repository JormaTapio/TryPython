# Lista muutetaan yhdeksi teksiobjektiksi, jossa listan jäsenten välissä on tyhjämerkki.
""" Lista tekstiriviksi ["koi", "poika","tyttö"] ==> "koi poika tyttö" """

def muuta(lista):         
    # tekstin alustaminen "" 
    teksti = "" 
    # muutetaan lista tekstiksi
    for x in range(len(lista)):
        teksti += lista[x] + " "
    return teksti 

def main():
    print(__doc__)
    lista = ["koi", "poika","tyttö"]
    print(muuta(lista))   

main()