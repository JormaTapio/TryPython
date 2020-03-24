# Graffisen ikkunan esimerkki
from tkinter import *
import sys

def lopeta():
    ikkuna.destroy()
    sys.exit(0)

ikkuna = Tk()

teksti_ikkuna = Label(ikkuna, text = "Pythonin Tkinter toiminnassa")
teksti_ikkuna.pack()

lopeta_nappi = Button(ikkuna, text = "Lopeta", command = lopeta)
lopeta_nappi.pack(side = BOTTOM)

ikkuna.mainloop()