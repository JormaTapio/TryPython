# -*- coding: cp1252 -*-

from random import randint
import sys

def lukupeli():
    arvaus = 0
    luku = randint(0,100)
    while True:
        syote = int(input("Anna luku 0-100 väliltä: "))
        arvaus = arvaus + 1
        if syote < 0:
              print("Virheellinen syöte!")
              print("Lopetetaan.")
              sys.exit(0)
        if syote == luku:
              print("Arvasit oikein!")
              print("Arvauksia oli",arvaus,"kertaa.")
              break
        elif syote < luku:
              print("Luku on suurempi.")
        else:
              print("Luku on pienempi.")

if __name__ == "__main__":
       lukupeli()
