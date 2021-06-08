#While Komutu ile alt alta girilen ismi sıralama

isim=input("Lütfen İsminizi Giriniz:")
sayac = 0
while sayac <len(isim):
    print(isim[sayac])
    sayac +=1
else:
    print("Adının Harflerini Sıraladım...")