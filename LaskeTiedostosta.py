# Ohjelma avaa käyttäjän antaman tiedoston ja laskee sen sisältöä. 
# Ohjelmalla on virheenkorjaukset mukana käyttäjän antamien tietojen ja lukuvirheiden varalta.

def syote():
		try:
			tiedosto = input("Anna tiedoston nimi:")
			kahva = open(tiedosto,"r")
			sisalto = kahva.read()
			kahva.close()
			summa = int(sisalto)+313
		except IOError:
			print("Virheellinen tiedostonnimi")
		except ValueError:
			print("Tiedoston sisältö virheellinen!")
		else:
			print("Saatiin tulos",summa)
			
def main():
	syote()
	
if __name__ == "__main__":
	main()