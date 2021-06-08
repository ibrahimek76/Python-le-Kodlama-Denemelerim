


urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price

    })
    i += 1