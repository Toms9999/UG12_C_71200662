a = input("Masukkan angka : ")
b = input("Masukkan angka yang di hitung : ")

count = 0

for i in a :
    if i == b :
        count += 1
print('angka {b} muncul {count} kali')