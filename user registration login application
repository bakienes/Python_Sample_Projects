#User Registration / Login Application

import os,time

çevrimiçi_kullanıcı = False

def giriş_yap():
	global çevrimiçi_kullanıcı
	kullanıcı_adı= input("Enter your username: ")
	şifre= input("Enter your password: ")

	dosya= open("users.txt","r")
	satırlar = dosya.readlines()
	çevrimiçi_kullanıcı = False
	for kullanıcı in satırlar:
		bölünmüş = kullanıcı.split()
		bölünmüş_k_adı= bölünmüş[0]
		bölünmüş_şifre= bölünmüş[1]
		if kullanıcı_adı == bölünmüş_k_adı and şifre == bölünmüş_şifre:
			çevrimiçi_kullanıcı= kullanıcı_adı
	if çevrimiçi_kullanıcı:
		print("Welcome: ",kullanıcı_adı)
	else:
		print("Username or password is wrong!")
	input("Press any key to continue")


def kayıt_ol():
	kullanıcı_adı= input("Enter username: ")
	mail= input("Enter your e-mail address: ")
	if not kontrol(kullanıcı_adı):
		
		#Username is not available

		print("=========Username Already Exists===========")
		time.sleep(1)
		os.system(temizle)
		return kayıt_ol()
	şifre= input("Enter your password: ")
	şifre_o= input("Reenter password: ")

	if şifre != şifre_o:
		print("======Passwords Did Not Match=====")
		time.sleep(1)
		os.system(temizle)
		return kayıt_ol()

	dosya = open("users.txt","a")
	dosya.write(kullanıcı_adı)
	dosya.write(" ")
	dosya.write(şifre)
	dosya.write(" ")
	dosya.write(mail)
	dosya.write("\n")
	dosya.close()
	print("The user is registered.")
	input("Press any key to continue")


def kontrol(kullanıcı_adı):
	try:
		if kullanıcı_adı not in open("users.txt","r").read():
			return True
		else:
			return False
	except FileNotFoundError:
		return True


temizle = ("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
	while True:
		os.system(temizle)
		print("""

					[1] Register
					[2] Login

			""")

		seçim= int(input("Make your choice: "))
		if seçim == 1:
			os.system(temizle)
			kayıt_ol()
		elif seçim == 2:
			os.system(temizle)
			giriş_yap()

