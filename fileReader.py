# Ohjelmalla voi lukea "Koe.txt" -tiedoston kaikki rivit alkaen alku-parametrin määrittämästä kohdasta
# -*- coding: cp1252 -*-

import os,sys

with open(os.path.join(sys.path[0], "koe.txt"), "r") as tiedosto:
    alku = 4
    while True:
        riveja = list(tiedosto.readlines())
        tiedosto.close
        uusitiedosto = open("koe.py","a")
        uusitiedosto.write("\n\nUusi tiedostonluku1:\n")
        for rivi in riveja:
            sisus = rivi[alku:]
            uusitiedosto.write(sisus)
        uusitiedosto.close
        break

