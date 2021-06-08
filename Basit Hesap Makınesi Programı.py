print("""
**************************
Hesap Makinesi   Programına Hoşgeldiniz
işlemler:
1.Toplama 
2.çıkarma
3.carpma
4 bölme
*****************************
""")
a = int(input("Birinci Sayıyı Giriniz :"))
b = int(input("İkinci Sayıyı Giriniz :"))

işlem =  input("İşlem Numarasını Giriniz:")    #Koşullar Buna Göre Yazıldı

if (işlem == "1"):
    print("{} İle {}' nin Toplamı {} dır".format(a,b, a + b))
elif (işlem =="2"):
    print("{} İle {} 'nin Farkı {} dır".format(a,b, a - b))
elif (işlem =="3") :
    print("{} İle {}'nin Çarpımı {} dir".format(a,b, a * b))
elif (işlem =="4"):
    print("{} İle {} 'e Bölümü {} dir".format(a,b, a / b))
else:
    print("Lütfen Geçerli Bir İşlem Seçiniz....")