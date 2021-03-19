#Nama, hobi (harus lebih dari 2), sosial media (harus lebih dari 2), 
#lagu kesukaan (harus lebih dari 2), makanan favorit (harus lebih dari 2),

def print_datadiri(data):
  for label, isi in data.items():
      if type(isi) == list: 
          for i in range(len(isi)):
              print("{} {} : {}".format(label, i+1, isi[i]))
      else:
          print("{} : {}".format(label, isi))

datadiri ={'Nama':'Alam',
            'Hobi':['Travelling', 'Main game', 'Mukbang'],
            'Sosmed':['Ig : @alam_syach10', 'Line : alambana123', 'Fb : alam syach'],
            'Lagu':['To the bone', 'Aku ikhlas', 'Lingsir wengi'],
            'Makanan':['Nasgor', 'Bakso', 'Ayam goreng']}

print_datadiri(datadiri) 
print(" ")
#Ubah salah satu dari hobi dan sosial media kalian, 
#hapuslah 2 makanan favorit kalian, dan tambahkan lah 1 hoby kalian
datadiri['Hobi'][2]='Menyelam'
datadiri['Sosmed'][0]='Wa : 085887678966'
del datadiri['Makanan'][:2]
datadiri['Hobi'].append('Membaca')

print("Setelah data diubah : ")
print_datadiri(datadiri)