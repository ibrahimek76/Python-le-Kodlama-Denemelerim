#soru cevap if elif else
sayac = 0
soru=input("Bir Meyve Adı Söleyin  Bana:")

cevap2 =("Tebrikler Hadi Devam Edelim....")

meyve=("gerçekten meyvemidir?")

if soru=="Elma" or soru=="elma":
    print("Evet Elma Bir Meyvedir")
elif soru =="Karpuz" or soru =="karpuz":
        print("Evet Karpuz Bir Meyvedir")
elif soru=="Armut" or soru =="armut":
    print("Evet Armut Bir Meyvedir")
else:
    print("Gerçekten meyvemidir")

soru2=input("eminsen 'e' harfine bas:")#üzerinde çalış

while (sayac<1):
    print(cevap2)
    sayac +=1
#gerçekten meyvemidir sorusuna evetse "e" hayırsa "h" yazdır
#cevap "e" ise devam edelim "h" ise başka soru sor diye yazdır