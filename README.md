# PythonIfChatBot
If ve Else kod bloklarından oluşan,öğrenebilen,web araması yapabilen,karşılıklı konuşma yapılabilen bir chatbot. 


## Nasıl Kullanılır ?
* **asist.py** dosyası açılır
* Karşılıklı sohbet chat botu hazır!
* Programı bitirmek için **"Görüşürüz"** yazmanız gereklidir yoksa öğrenilen bilgiler **kaydedilmez** ve bir sonraki kullanımda bellekle beraber **silinir**.


## Nasıl **"Öğreniyor"** ?
Bilinmeyen bir cümle veya kelimeyle karşılaşınca 1,2 ve 3 olmak üzere 3 seçenek var, bu 3 seçenek;
* Bilinmeyen veri İnternette aranır.
* Bilinmeyen veri bir dahaki kullanımda hatırlanması için kullanıcın verdiği cevapla kaydedilir.
* Hiçbir şey yapılmaz.

### 2. Seçenek Nasıl Çalışıyor ?
* Bilinmeyen veri **bellek.py** dosyasına kaydedilir(dosya w kipinde açılır bu sayede önceki veriler silinir ve eski veriler tekrar tekrar kaydedilmez)
* Programı kapatırken **"Görüşürüz"** yazılır ve **belek.py** dosyasındaki veriler **bilgibirikimi.py** dosyasının sonuna eklenir.

## Bilinen Problemler
* Aynı anda 2 veri **bellek.py** dosyasına kaydedilemiyor(diğer dosya açma kipleri **eski** verilerin **sürekli** kaydedilmesine neden oluyor.)
* Program **büyük/küçük harf** ayırt ediyor.
* Programın sürekli çalışmasını sağlayan döngü problemlere neden oluyor.

### Problemlere Çözümler
* --
* Cevaplar **küçük harfe** çevirilir bu sayede **büyük küçük harf ayrımı** yok edilir
* --
