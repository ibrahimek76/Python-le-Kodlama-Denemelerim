#   sayıların değerlerini, değiştiren program

a=(input("a :"))
b=(input("b :"))
print("Değiştirilmeden Önce Değerler :\na:{}   b: {}\n".format (a,b))
a,b=b,a
print("Değiştirildikten Sonra Değerler : \na:{}  b: {}\n".format(a,b))