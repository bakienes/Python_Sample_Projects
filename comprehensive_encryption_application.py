#Comprehensive Encryption Application

import string
import os

alfabe= string.ascii_lowercase
max_karakter= len(alfabe)

temizle= ("cls" if os.name == "nt" else "clear")


def seçenekler():
	while True:
		os.system(temizle)
		seçenek= input("What do you want to do: ").lower()
		if seçenek in ("encrypt","encryption","make encryption","do encryption","I would like to do encryption"):
			şifreleme()
		elif seçenek in ("decoding,decrypt"):
			şifre_çöz()
		else:
			print("To do encryption (%s) write, to decrypt (%s) write." % ("encrypt","decoding"))


def şifreleme():
	metin= input("Enter the text to be encrypted: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	şifrelenmiş_metin= ""
	for karakter in metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no += şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			şifreli_karakter= chr(karakter_sıra_no)
			şifrelenmiş_metin += şifreli_karakter

		else:
			şifrelenmiş_metin += karakter
	os.system(temizle)
	print("%s of the word %d encrypted with key %s" % (metin,şifreleme_anahtarı,şifrelenmiş_metin))
	input("Press any key to continue")



def şifre_çöz():
	şifreli_metin= input("Enter the encrypted text to be decrypted: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	çözülmüş_metin= ""
	for karakter in şifreli_metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no -= şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			çözülmüş_karakter= chr(karakter_sıra_no)
			çözülmüş_metin += çözülmüş_karakter
			
		else:
			çözülmüş_metin += karakter
	os.system(temizle)
	print("%s your encrypted text %d unraveled with the key %s" % (şifreli_metin,şifreleme_anahtarı,çözülmüş_metin))
	input("Press any key to continue")



def şifrelemeAnahtarı():
	anahtar= int(input("Enter encryption key (1-%s):" % max_karakter))
	if anahtar >=1 and anahtar <= max_karakter:
		return anahtar
	else:
		return 1



if __name__ == "__main__":
	seçenekler()
