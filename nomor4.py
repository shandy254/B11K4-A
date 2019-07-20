"""
‘ARKAFOOD5’ dan ‘DITRAKTIRDEMY’. 
Ketentuan menggunakan kode promo ARKAFOOD5 adalah pemesanan minimal 50rb, 
diskon 50% dengan maksimal potongan sebesar 50rb. 

Untuk ketentuan kode promo DITRAKTIRDEMY, 
pemesanan minimal sebesar 25rb, 
diskon 60% dengan maksimal potongan sebesar 30rb. 

Untuk pengiriman, 1,5 kilometer pertama dikenakan tarif 5 rb, 
dan setiap satu kilometer selanjutnya dikenakan penambahan 3 rb. 
Untuk beberapa restoran dikenakan pajak yakni tarif 5% dari harga makanan.


Buatlah fungsi/method untuk menghitung berapa total harga yang harus dibayar Rara 
dengan parameter harga makanan, 
kode voucher (“False” jika tidak menggunakan), 
jarak, dan pajak (“False” jika tidak ada).

Contoh Input: arkaFood(75000,“ARKAFOOD5”,5,“False”)
Contoh Output: Rp. 54.500 
"""

def arkaFood(harga,kode,jarak,pajak):
    if kode == "ARKAFOOD5":    
        if harga >= 50000:
            diskon = 50/100 * harga
            if diskon > 50000:
                hrg_now=harga-50000
            else:
                hrg_now=harga-diskon
    elif kode == "DITRAKTIRDEMY":
        if harga >= 25000:
            diskon = 60/100 * harga
            if diskon > 30000:
                hrg_now=harga-30000
            else:
                hrg_now=harga-diskon
    else:
        hrg_now=harga

    if jarak <= 1.5:
        ongkir = ongkir + 5000
    elif jarak > 1.5:
        pengali=round((jarak-1.5)/1)
        ongkir = pengali * 3000

    if pajak == '5%':
        pjk = 5/100 * harga
    else:
        pjk = pajak

    
    hartot = hrg_now + ongkir + pjk
    print("harga total: ",hartot)


#Contoh Input: 
arkaFood(75000,"ARKAFOOD5",5,'5%')