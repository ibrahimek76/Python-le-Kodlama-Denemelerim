#Kullanıcı Yetkisi İsteyen Program
#Üzerine E posta Ekle E maille Kontrol Edilsin
#Yetki Deneme Hakkı Ver
#ehliyet almak için yaş eğitim kontrolu olan programdaki gibi if elif elseyi kullan eksik var



ad=input("Lütfen İsminizi Giriniz:")
yas= input("Lütfen Yaşınızı Giriniz")
email=(input("Lütfen Mailinizi Giriniz:"))
parola=(input("Lütfen Parolanızı Giriniz:"))
sys_email="elektronikci_edr@hotmail.com"
sys_parola="edirneli"

if (yas  >= 18):
    print("Sisteme Giriş  Yetkiniz Bulunmamaktadır.... ")
else:
    print("Sisteme Hoşgeldin DR.Cable....")