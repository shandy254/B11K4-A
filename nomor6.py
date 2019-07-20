"""
Format Input: namaFungsi(‘jenis operasi matematika’,N,array digit)
Jenis Operasi: 
A.	SUM = penjumlahan
B.	MUL = perkalian
C.	SUB = pengurangan
D.	DIV = pembagian
 
Contoh Input:
mrBrulee(‘SUM’,20,[11,13,15])
//SUM = penjumlahan, N = 20 => D11 + D13 + D15  = 0 + 1 + 2
mrBrulee(‘MUL’,20,[12,15,17])
// D12 * D15 * D17 = 1 * 2 * 3
 
Contoh Output:
3
6
"""


def mrbag(operasi,max,dig):
    for a in range(1,max):
        if operasi == 'SUM':
            hsl=hsl + dig[a]
        elif operasi == 'MUL':
            hsl=hsl * dig[a]
        elif operasi == 'SUB':
            hsl=hsl - dig[a]
        elif operasi == 'DIV':
            hsl=hsl / dig[a]

    print("hasil : ",hsl)

mrbag('SUM',20,[11,13,15])