



import re

# U S E R N A M E

username_dicari = re.compile(r'[a-zA-Z][a-zA-Z0-9._%+-]{5,9}')
username = '5agusT99'
mo1 = username_dicari.search(username)
#mo1.group()

username_dicari = re.compile(r'[a-zA-Z][a-zA-Z0-9._%+-]{5,9}')
username2 = 'basha'
mo2 = username_dicari.match(username)


# P A S S W O R D

password_dicari = re.compile(r'[a-zA-Z][a-zA-Z0-9._%+-]{5,9}')
password = '5agusT99'
mo3 = password_dicari.search(password)
#mo1.group()

password_dicari = re.compile(r'([a-zA-Z][a-z][A-Z][0-9][._%+-]){8,}')
password = 'basha'
mo4 = password_dicari.match(password)

"""
if username == mo1:
    print(mo1)
else:
    print("false")

if username2 == mo2:
    print(mo2)
else:
    print("false")
"""

print(mo1)
print(mo2)
print(mo3)
print(mo4)

"""
tambah=0
salah=0
text = 'konsonan'
for huruf in text:
   #print('cetak huruf',huruf,end='') 
   #print()
   batas = tambah + 1
   if huruf[0] != [a-zA-Z]:
       salah + 1
    elif huruf != [a-zA-Z0-9._%+-]:
        salah + 1

if salah >= 1 | batas <= 5 | batas >= 9:
    print("false")
else:
    print("true")
"""




