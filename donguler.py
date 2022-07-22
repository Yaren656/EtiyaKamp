# for -- iteration
ogrenciler = ["Fatih", "Aykut", "Eyyub", "Deniz"] #index sıfırdan başlar.

for ogrenci in ogrenciler:
    #print(f"Öğrenci Adı : {ogrenci}")
    if ogrenci.lower()=="fatih".lower():
        print(f"Adı: {ogrenci}" + " = " "OKEY")

# öğrenci ismi Fatih ise ekrana "OKEY" yazsın

for sayi in range(50, 100): #ilk değerden >= ikinci değerden <'leri yazar. 3. parametre arttırma.
    if sayi % 2 == 0:
        print(sayi)


for sayi in range(50, 100,3):
    print(sayi)


print("******----******")

#while -- olduğu sürece
sayac = 0
while sayac < 50:
    print(sayac)
    sayac += 1    #sayac = sayac + 1

# kullanıcı x kadar not ortalaması girmek istiyor
# girdiği not 50'den büyük ve eşitse geçti
# console'da : 50 dersten 25 ini geçtiniz gibi yazacak
# girdiği tüm notlar görmek istiyor


girilecekNotSayisi = int(input("Kaç adet not gireceksiniz? "))
gecilenDersSayisi = 0
girilenNotlar = []
for note in range(girilecekNotSayisi):
    girilenNot = float(input(f"{note+1}. notu giriniz: "))
    girilenNotlar.append(girilenNot) #listeye ekledim
    if girilenNot >= 50:
        gecilenDersSayisi += 1
print(f"{girilecekNotSayisi} dersten {gecilenDersSayisi} dersi geçtiniz.")
#print(f"Girdiğiniz notlar :  {girilenNotlar}")

i = 0
for girilenNot in girilenNotlar:
     print(f"{i+1}. girdiğiniz not : {girilenNot} ")
     i+=1


print("*****-------*****")


# ÖDEV program sonunda girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır.
# kişi direkt ortalama not girmek yerine vize ve final girecek siz oradan o dersin ortalamasını
# hesaplayıp geçip kalma durumuna göre işlem yapacaksınız vize %40, %60
# dictionary dene. Önce kodlama.io'dan kursu bitir sonra bunu yap

vize = int(input("Vize Notunuz : "))
final = int(input("Final Notunuz : "))
ortalama = vize * 0.4 + final * 0.6
if ortalama > 50:
    print(f"Ortalamanız : {ortalama} -- Geçtiniz")
else:
    print(f"Ortalamanız :{ortalama} -- Kaldınız")

print(f"Girdiğiniz Vize Notunuz : {vize} ")
print(f"Girdiğiniz Final Notunuz : {final}")
