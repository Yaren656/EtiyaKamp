# kosul yapıları if, elif(else if), else
#indent - o kodun içinde olmak

# ortalamaNotu = 90

# if ortalamaNotu < 50:
#     print("Kaldınız")
# elif ortalamaNotu >= 50 and ortalamaNotu <=40:
#     print("Normal geçtiniz")
# else:
#     print("Başarıyla geçtiniz")

# print("Her halükarda çalıştırmak istediğim kod")

sayi = input("Sayıyı giriniz : ")
sayi = int(sayi)
if sayi % 2 == 0:
    print("Sayı çifttir.")
elif sayi % 2 == 1:
    print("Sayı tektir.")
else:
    print("Sayı hesaplanamadı.")
