baslik = "Merhaba Etiya" #metinsel veri türü : string, str
print(baslik)
baslik = "Hoş geldiniz"
print(baslik) #değerini değştik ve tekrar yazdırdık

vade = 16 #tam sayı veri türü : int, integer
print(vade)
print(type(vade)) #type'ını verir
print(type(baslik))

kur = 17.5 #ondalıklı sayılarda Python'da nokta(.) kullan : float, decimal, double, currency
print(kur)
print(type(kur))

kurlar = ["EURO","DOLAR","TL"] #array, list
print(kurlar)

tupleOrnek = ("EURO",5,"TL") #tuple, değiştirilemez, listeye çevirip tekrar tuple'a geri çevirmek gerekir
print(tupleOrnek)

girisYapti = True #boolean, bool false ya da true. Karar yapılarında kullanırız giriş ya olur ya olmaz gibi
print(girisYapti)

araba ={
"Marka" : "BMW",
"Model" : "3.20",
"Year" : 2012,
"Attachment" : ["Xenon Far", "Hayalet Ekran"]
} #dict, dictionary, bir değere karşılık gelen bir değer, aradığınız kelime ve anlamı
#attachment : ek özellikler
print(araba)
