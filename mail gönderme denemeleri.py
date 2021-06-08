import smtplib
gmail ="kendi mailiniz"
password= "kendi şifreniz"
karşıtaraf="karsı tarafa gidicek mail"
server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(gmail,password)

msg="Saldırı Altındasınız"
receiver = karşıtaraf
server.sendmail(gmail, receiver , msg.encode("utf-8"))
print("E Posta Gönderildi")
