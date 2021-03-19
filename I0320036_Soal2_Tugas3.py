print ('Biodata Erysa')

#membuat dictionary
dict = {'Nama'           : 'Erysa Putri Vara Afifa',
        'Hobi'           : ['Menonton film', 'Mendengarkan musik', 'Bersepeda'],
        'Sosial Media'   : ['Instagram : erysaptr', 'Line : erysaputri_', 'WhatsApp : 082136015244'],
        'Lagu Kesukaan'  : ['Everything i wanted', 'Through the night', 'Mendarah'],
        'Makanan Favorit': ['Sate ayam', 'Pempek', 'Nugget']}

#mengubah salah satu hobi
dict['Hobi'][2] = 'Membaca'

#mengubah salah satu sosial media
dict['Sosial Media'][2] = 'Telegram : erysaputri'

#menghapus 2 makanan favorit
del dict['Makanan Favorit'][0:2]

#menambahkan hobi
dict['Hobi'].append('Jalan-jalan')

print(dict)