print ("******---******")

salary = int(input("Lütfen güncel maaşınızı giriniz : "))
hike = int(input("Lütfen maaşınıza uygulanacak zammı yüzdelik bazında giriniz : "))

newSalary = salary + (salary * (hike/100))

print(f"Maaşınızın zamlı hali : {newSalary}")


print ("******---******")


num = int(input("Lütfen 1'den büyük bir sayı giriniz : "))
x = 0
for i in range(2, num):
    #print(f"Num değeri : {num}")
    if num % i == 0:
        i += 1
        x = 1
        break

if x == 0:
    print("Girilen sayı asal sayıdır.")
else:
    print("Girilen sayı asal değildir.")

