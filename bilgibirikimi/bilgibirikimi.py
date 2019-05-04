import os 
import webbrowser


chrome_yoluWin = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#sadece Windows'da çalışır!
chrome_yoluMac = 'open -a /Applications/Google\ Chrome.app %s'
chrome_yoluLin = '/usr/bin/google-chrome %s'

def iletisim(cevap):
    if cevap == 'Ne Yapıyorsun ?':
        print('Hiiç...Öyle size yardım ediyorum.')
        cevap=input('>>>')
    if cevap == 'Bana bir şeyler öner':
        print('Bilemedim ki şimdi')
        cevap=input('>>>')
    if cevap == 'Naber':
        print('İyiyim')
        cevap=input('>>>')
    if cevap == 'ping':
        print('pong')
        cevap=input('>>>')
    if cevap == 'Müzik aleti çalabiliyor musun ?':
        print('Sence çalabiliyor muyum ?\a\a\a')
        cevap=input('>>>')
    if cevap == 'Sen ne işe yararsın ?':
        print('Çok şey yaparım: sana yardım ederim,istediğini internette ararım,seninle sohbet ederim...')
        cevap=input('>>>')
    if cevap == 'Ne Güzel':
        print('Ney mi güzel ?')
        cevap=input('>>>')
    if cevap == 'Webde ara':
        print('Neyi webde arayayım belirtirsen sevinirim')
        webdeara=input('Webde aranmak üzere >>>')
        if os.name=='nt':
            webbrowser.get(chrome_yoluWin).open('''https://www.google.com.tr/search?q='''+webdeara+'''&oq='''+webdeara+'''&aqs''')
        if os.name=='posix':
            webbrowser.get(chrome_yoluLin).open('''https://www.google.com.tr/search?q='''+webdeara+'''&oq='''+webdeara+'''&aqs''')
        cevap=input('>>>')
    else:
        print('Ne dediğinizi anlamadım ancak isterseniz Webde arayabilirim(1 yazın) veya bana bir şey söylersiniz bir dahaki sefere bunu hatırlarım(2 yazın),hiçbir şey yapmak istemiyosanız(3 yazın).')
        elsecevap = input('>>>')
        if elsecevap== '1':
            webbrowser.get(chrome_yolu).open('''https://www.google.com.tr/search?q='''+cevap+'''&oq='''+cevap+'''&aqs''')
            cevap=input('>>>')
        if elsecevap=='2':
            bilgibirikimi = open('bilgibirikimi/bellek.py','w', encoding="utf-8")
            bilgi=input('>>>')       
            cevapi= "'"+cevap+"'"
            bilgii="'"+bilgi+"'"
            bilgibirikimi.write('''
    if cevap == '''+cevapi+''':
        print('''+bilgii+''')
        cevap=input('>>>')''')
            print('İşlem başarı ile tamamlandı, bir dahaki sefere hazırlıklı olacağım.')
            bilgibirikimi.close()
        if elsecevap == '3':
            cevap = input('>>>')