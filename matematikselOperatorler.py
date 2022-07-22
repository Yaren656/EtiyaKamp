print("Operatorler")
sayi = 15
print(sayi + 10)
print(sayi - 10)
print(sayi * 10)
print(sayi / 10) #sayi değişmez işlemi yapıp print eder sadece

print("********")

sayi = sayi + 10 #sayinin değerini değiştirir
print(sayi)
print(sayi + 10)
print(sayi - 10)
print(sayi * 10)
print(sayi / 10)

print(sayi % 5) #bölümünden kaç kalır, mod operatörü

print("********")

ondalikSayi = 10.5
print(ondalikSayi + 10)
print(ondalikSayi - 10)
print(ondalikSayi * 10)
print(ondalikSayi / 10)

sayi = 100
print(sayi ** 2) #sayinin üçüncü üssü, üs alma işlemi
print(sayi // 15) #tam bölme işlemi, int olarak getirir

baslik = "Merhaba"
isim = "Engin Demiroğ"
print(baslik + " Etiya")
print(baslik + " Kodlamaio" + " Engin Demiroğ")

#string format
print("{title} Sayın {name}".format(title=baslik, name=isim))
print(f"{baslik} Sayın {isim}") 




#print(baslik*10) #bunu çalıştırır
#print(baslik/10) fakat bunu çalıştırmaz

#print(baslik.lower())
#print(baslik.upper())
#print(len(baslik)) #lenght

#tip değiştirme
# input => kullanıcıdan veri alma
#vade = input("Vade tutarı giriniz : ")
#print(f"Vadenin tipi ilk başta : {type(vade)}")
#vade = int(vade)
#vade = vade + 10
#print(f"Vadenin tipi dönüşümden sonra : {type(vade)}")
#print(f"Girdiğiniz vade: {vade}")

#pair.py dosya oluştur, kullanıcıdan 2 input al
#1. input vize notu 0.40 %40
#2. input final notu 0.60 %60
#geçme notu 50'den büyül olma durumunu yazdır

vizeNotu = input("Lütfen Vize Notu Giriniz : ")
(f"Vize Notu Tipi {type(vizeNotu)}")
vizeNotu = int(vizeNotu)
finalNotu = input("Lütfen Final Notu Giriniz : ")
(f"Final Notu Tipi {type(finalNotu)}")
finalNotu = int(finalNotu)

ortalama = vizeNotu*0.4 + finalNotu*0.6
print(f"Geçme durumunuz : {ortalama > 50}, Ortalamanız : {ortalama}")






