# -*- coding: utf-8 -*-

import random
import time
import sys
import webbrowser

sys.path.append(r'bilgibirikimi')

import bilgibirikimi
    
selamlama = ['Merhaba','Selamlar','Merhabalar Efenim','Selamlar Efenim','Nabersiniz','Ooo Hoşgelmişsiniz','Selam','Merhabalar']
halhatir = ['Nabersiniz','Nasılsınız','İyisiniz Umarım']
iyiyim = ['Ne güzel, esenlikler dilerim','Ne güzel','Esenlikler dilerim','Daha da iyi olmanızı temenni ederim',]

print('-'*15,'Python Koşullu Asistan','-'*15)

print(random.choice(selamlama))
print('Hal Hatır Sormak Lazım,',random.choice(halhatir))


while True:
    cevap = input('>>>')

    if cevap == 'Görüşürüz':
        print('Görüşürüz')
        blk = open("bilgibirikimi/bellek.py", "r")
        veri = blk.read()
        modul = open("bilgibirikimi/bilgibirikimi.py", "a+")
        modul.write("\n"+veri)
        time.sleep(2)
        break
    if cevap == 'İyiyim' or 'iyiyim':
        print(random.choice(iyiyim))
        cevap=input('>>>')

    bilgibirikimi.iletisim(cevap)