print("*****************\nKullanıcı Girişi\n******************\n")

sys_kullanıcı_adı= "iibrahim" #sistemde varsayılan kullanıcı adı
sys_parola = "12345" #sistemde varsayılan parola
kullanıcı_adı= input("Kullanıcı Adını Giriniz:")
parola =input("Parolanızı Giriniz:")

if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı Adı Hatalı . . . ")
elif (kullanıcı_adı==sys_kullanıcı_adı and parola != sys_parola):
    print("Parola Hatalı . . . .")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı Ve Parola Hatalı . . . ")
else:
    print("Tebrikler Başarıyla Giriş Yaptınız . . . .")