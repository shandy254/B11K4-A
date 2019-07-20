kata = input("masukan kata ")

panjang=len(kata)

satu = round(1/3 * panjang)
dua = round(2/3 * panjang)

print("panjang : ",panjang)

for k in range(0,satu):
    print(kata[k],end='')
print(",",end='')
for k in range(satu,dua):
    print(kata[k],end='')
print(",",end='')
for k in range(dua,panjang):
    print(kata[k],end='')

print("")

for k in range(0,satu):
    print(kata[k],end='')

for k in range(satu,dua):
    print(kata[k],end='')
print(",",end='')
for k in range(dua,panjang):
    print(kata[k],end='')
