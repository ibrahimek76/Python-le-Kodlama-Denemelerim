#Kullanıcı adı ve parolanın uzunluğunu veren program

kullanıcı_adı =input("Kullanıcı Adınız:")   #Değer
parola= input("Parolanız\t\t\t\t:")              #Değer
toplam_uzunluk =len(kullanıcı_adı)+len(parola) #Değer
mesaj= "Kullanıcı Adı Ve Parolanız Toplam {} Karakterden Oluşuyor" #Değer
#Değerler Yazılır daha sonra if else kullanılır yada kullanılması gereken fonksıyonlar
print(mesaj.format(toplam_uzunluk))
if toplam_uzunluk>40:
    print("Kullanıcı Adınız İle Parolanızın","Toplam Uzunluğu 40 Karakteri Geçmemeli)")
else:
    print("Sisteme Hosgeldiniz....")