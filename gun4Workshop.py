# print ("******---******")

# salary = int(input("Lütfen güncel maaşınızı giriniz : "))
# hike = int(input("Lütfen maaşınıza uygulanacak zammı yüzdelik bazında giriniz : "))

# newSalary = salary + (salary * (hike/100))

# print(f"Maaşınızın zamlı hali : {newSalary}")


# print ("******---******")


num = int(input("Lütfen 1'den büyük bir sayı giriniz : "))
x = False
for i in range(2, num):
    #print(f"Num değeri : {num}")
    if num % i == 0: #örn: 10 % 2 = 0, if devam eder, x = 1 oldu, diğer if'e geldi else çalıştı.
        i += 1       #örn: 7 % 2 =! 0 if break oldu, diğer if'e geldi, x == 0 kaldı ilk koşul çalıştı.
        x = 1
        break

if x == False:
    print("Girilen sayı asal sayıdır.")
else:
    print("Girilen sayı asal değildir.")




