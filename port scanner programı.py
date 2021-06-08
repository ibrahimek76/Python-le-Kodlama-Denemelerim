import os
#sudo apt-get install nmap yüklü olmadığı için hata sebebi kali sürümü için geçerli
#nmap import edilmesi lazım 

print("""
port tarayıcı uygulamasına hoşgelniz
işlem seçin
1) hızlı tarama
2)servis ve versiyon hakkında bilgi edinme
3)işletim sistemi hakkında bilgi edinme
4)detaylı arama(proxy gerektitir
""")
işlemno= input("işlem no giriniz:")
if (işlemno == "1"):
    hedefip = input("hedef ip giriniz:")
    os.system("nmap   " + hedefip)
elif (işlemno == "2"):
    hedefip = input("hedef ip giriniz:")
    os.system("nmap  -Ss  -sV  " + hedefip)
elif (işlemno == "3"):
    hedefip = input("hedef ip giriniz:")
    os.system("nmap  -O " + hedefip)
elif (işlemno == "4"):
    hedefip = input("hedef ip giriniz:")
    proxy1= input("proxy adreslerinizi giriniz(örnek: socks://127.0.1.0):")
    os.system("nmap   -Pn    "    +    hedefip   +   "  -sV   - sS    -V   -T4  -0    -- proxy  " +  proxy1)
