# Kolay Beden Kitle İndeksi Hesapma
#İf else Blokları sonradan dahil edilmiştir
#Aşağıda Verilen Değerler ile programı yazın
# BKİ 18.5'un altındaysa -------> Zayıf < küçüktür olucak
 #BKİ 18.5 ile 25 arasındaysa ------> Normal >=  18.5 için büyük eşittir olucak < büyüktür 25 için
 #BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu >= 25 için büyük eşittir < küçüktür 30 için
 #BKİ 30'un üstündeyse -------------> Obez else ile yazdır

boy=int and float(input("Boyunuzu (cm Cinsinden)Giriniz: "))
kilo=int and float(input("Kilonuzu Giriniz:"))

print("Beden Kitle İndeksiniz:",kilo / (boy ** 2))

if(kilo< 18.5):
    print("Zayıf ")
elif (kilo >=18.5 and kilo < 25):
    print("Normal")
elif (kilo>=25 and kilo<30):
    print("Fazla Kilolu")
else:
    print("Obez")
