# Ohjelma pitusmitan antamiseksi

def pituusmitta(mitta):
	if (mitta != 0):
		print("Antamasi syöte oli",mitta,"merkkiä pitkä.")
	else:
		print("Et antanut syötettä")
		
def main():
	while True:
		syote = input("Anna syöte (Lopeta lopettaa): ")
		if (syote == "Lopeta"):
			break
		pituus = len(syote)
		pituusmitta(pituus)
	
if __name__=="__main__":
	main()