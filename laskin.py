# Laskin kahdeksalla vaihtoedon toteuttavalla asialla. 6 eri laskennalla, joista kaksi käyttää math-kirjastoa, 
# yhdellä lähtösyöteiden vaihtamisella ja yhdellä ohjelman lopetamisvalinnalla
# Laskin 8 portaisella valikolla ja käyttäjän antaman syötteen tarkistuksella.
from math import sin, cos

# Funktio, joka tarkistaa käyttäjän syötteen oikeellisuuden
def luvunLukija():
	while True:
		try:
			luku = input("Anna luku:")
			luku = int(luku)
		except ValueError:
			print("Virheellinen syöte!")
		else:
			return luku

# 8-valinnan laskin			
def main():
	luku1 = luvunLukija()
	luku2 = luvunLukija()
	while True:
		print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7) Vaihda luvut\n(8) Lopeta")
		print("Valitut luvut:", str(luku1), str(luku2)) 
		valinta = int(input("Tee valinta (1-8): "))
		if valinta == 1:
			tulos = luku1 + luku2
		elif valinta == 2:
			tulos = luku1 - luku2
		elif valinta == 3:
			tulos = luku1 * luku2
		elif valinta == 4:
			tulos = luku1 / luku2
		elif valinta == 5:
			tulos = sin(luku1/luku2)
		elif valinta == 6:
			tulos = cos(luku1/luku2)
		elif valinta == 7:
			luku1 = luvunLukija()
			luku2 = luvunLukija()
		elif valinta == 8:
			break
		if valinta == 7:
			pass
		else:
			print("Tulos on: ", str(tulos))
			
if __name__ == "__main__":
	main()