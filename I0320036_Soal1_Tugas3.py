#nama teman
list_nama = ['Dhea', 'Cita', 'Fadhila', 'Alif', 'Rengga', 'Sekar', 'Tsania', 'Efa', 'Hafizh', 'Desy']

#menampilkan nama indeks 4, 6, dan 7
print(list_nama[4])
print(list_nama[6])
print(list_nama[7], '\n')

#mengganti nama indeks 3, 5, dan 9
list_nama[3] = 'Vizal'
list_nama[5] = 'Uddin'
list_nama[9] = 'Erika'

#menambahkan 2 nama
list_nama.extend(['Bonang','Putri'])

#menampilkan perulangan nama
x = 0
for iterasi in list_nama :
    print(iterasi)

#menampilkan panjang list
print(len(list_nama))