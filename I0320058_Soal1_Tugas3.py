#Isi list sebanyak 10
list = ['ojat', 'nurki', 'afnan', 'jefri', 
        'aji', 'ilham', 'ivan', 'rafli', 'ahnaf', 'fagih']

#Tampilkanlah isi list indeks nomor 4,6,7
print("nilai pada index 4 : ", list[4])
print("nilai pada index 6 : ", list[6])
print("nilai pada index 7 : ", list[7])
print("nilai pada index 4,6,7 : ", list[4], list[6], list[7])

#Gantilah nama teman mu yang berada di list 3,5,9
print("Sebelum mengganti index 3, 5, 9 : ", list[3], list[5], list[9])
list[3] = 'hafid'
list[5] = 'hafiz'
list[9] = 'hafizh'
print("Setelah mengganti index 3, 5, 9 : ", list[3], list[5], list[9])

#Tambahkanlah 2 nama teman mu
list.append('rara')
list.append('talitha')
print(list)

#Tampilkan semua teman kamu dengan perulangan
for nama in list:
    print(nama) 

#Tampilkan panjang list
print(len(list))
