

bil = input("batas maksimum: ")
bil = int(bil) 
b = [1,2]
for a in range(0,bil):
    if a+2 <= bil:
        b[a+2] = b[a] + b[a+1] 
        if b[a+2] % 2 == 0:
            genap = b[a+2]
        elif b[a+2] % 2 == 1:
            ganjil = b[a+2]
            
for x in range(0,bil):
    genap = genap[x] + genap[x+1]
    ganjil = ganjil[x] + ganjil[x+1]

for y in range(0,bil):
    print(genap[y])

for z in range(0,bil):
    print(ganjil[z])

#b.append('tambah')

