girdi = input("Girdi ->>>")
cikti = input("Çıktı ->>>")

karar = input("KAYDETMEK İÇİN 1;SİLMEK İÇİN 2 ->>>")

while True:
	if karar == "2":
		girdi = input("Girdi ->>>")
		cikti = input("Çıktı ->>>")

		karar = input("KAYDETMEK İÇİN 1;SİLMEK İÇİN 2 ->>>")
	if karar == "1":
		blg = open("bilgibirikimi/bilgibirikimi.py", "a+", encoding="utf-8")
		girdii= "'"+girdi+"'"
		ciktii="'"+cikti+"'"
		blg.write('''
    	if cevap == '''+girdii+''':
        print('''+ciktii+''')
        cevap=input('>>>')''')
		blg.close()
		girdi = input("Girdi ->>>")
		cikti = input("Çıktı ->>>")

		karar = int(input("KAYDETMEK İÇİN 1;SİLMEK İÇİN 2 ->>>"))