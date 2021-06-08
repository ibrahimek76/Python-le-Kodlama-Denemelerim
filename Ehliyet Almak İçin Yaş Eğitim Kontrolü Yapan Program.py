#Ehliyet alma koşulu 18 yaş ve eğitim durumu lise yada üniversite olmalıdır


isim=input("Lütfen İsminizi Giriniz:")
yaş=int(input("Lütfen Yaşınızı Giriniz:"))
eğitim=input("Eğitim Durumunuzu Giriniz:")
if yaş>=18:
    if (eğitim == "lise"  or   eğitim == "üniversite"or eğitim != "ilkokul"):
        print(f"{isim}\tEhliyet Alabilirsiniz")
    else:
        print(f"{isim}\t Ehliyet Alamazsın Eğitim Durumun Yetersiz")
else:
       print(f"{isim}\tEhliyet Alamazsın Yaşın Tutmuyor")