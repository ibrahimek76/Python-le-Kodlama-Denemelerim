import smtplib
gmail ="drkablosuz@gmail.com"
password= "5530035101ek"
karşıtaraf="ibrahimek76@gmail.com"
server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(gmail,password)

msg="Saldırı Altındasınız"
receiver = karşıtaraf
server.sendmail(gmail, receiver , msg.encode("utf-8"))
print("E Posta Gönderildi")