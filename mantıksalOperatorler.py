print(1==2) #sağına ve soluna yazılan değerin eşitliğini kontrol eder, mantıksak operatör olduğundan true ya da false döndürür
#print("1"==1) #aynı veri tipinde olmalılar, false döner

print(1 != 1) #sağına ve soluna yazılan değerlerib eşit olmama durumunu ister
#print("1" != "1")

print(1 > 1) #sola yazılan değerin sağa büyük olmasını ister
print(1 >= 1) 

print( 1 < 1)
print(1 <= 1)

print("12" > "1") #metin karakter uzunluğu ölçer

vade = 24
maxVade = 36
kredi = 1000
      #true     #and      #true
print(vade > 12 and kredi < 10000) #and - iki koşulunda sağlanması, istediğin kadar and yazabilirsin
print(vade < 12 and kredi < 1000)
       #false          #true

print() #or - iki veya daha fazla koşuldan tek birinin doğru olmasını ister 
print(vade < 12 or kredi < 10000)
       #false   #or   #true  => true

print(vade > 30 and maxVade == 36 or kredi < 1000)

print((vade > 30 or maxVade == 36) and kredi > 1000)

