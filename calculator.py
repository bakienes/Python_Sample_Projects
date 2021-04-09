#Calculator

secenek= """

		[1] Addition  [2] subtraction  [3] multiplication  [4] division  [5] exponentiation


"""
print(secenek)

secenek= int(input("Make your choice: "))
sayılar= input("Enter the numbers to be processed with a space between them.: ")
sayılar_bölünmüş= sayılar.split(" ")

if secenek == 1:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} + {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı + ikinci_sayı))

elif secenek == 2:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} - {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı - ikinci_sayı))

elif secenek == 3:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} * {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı * ikinci_sayı))

elif secenek == 4:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} / {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı / ikinci_sayı))

elif secenek == 5:
	ilk_sayı= float(sayılar_bölünmüş[0]) #Base
	ikinci_sayı= int(sayılar_bölünmüş[1]) #Force

	print("{} ** {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı ** ikinci_sayı))
else:
	print("You made a wrong choice")
