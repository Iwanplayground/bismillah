'''
overriding adalah fitur yang memungkinkan kita untuk mengimplementasikan “ulang” 
method pada sebuah child class atau kelas turunan yang sebenarnya 
fungsi tersebut telah didefinisikan di dalam parent class 

Overriding sendiri memberikan keuntungan kepada kita karena kita bisa 
menduplikat kelas lain sehingga kode program lebih singkat
'''

class kendaraan:
    def berjalan(self):
        print('berjalan...')

class motor(kendaraan):
    def berjalan(self):
        print('berjalan dengan cepat..')

sepeda = kendaraan()
vario = motor()

sepeda.berjalan()
print('==='*30)
# kita dapaat menambahkan paramater pd fungsi yg diminta, contoh:
class kendaraan:
    def berjalan(self):
        print('berjalan...')

class motor(kendaraan):
    def berjalan(self,kecepatan,satuan='km/jam'):
        print(f'berjalan dengan kecepatan {kecepatan}{satuan}')

sepeda = kendaraan()
cbr = motor()

sepeda.berjalan()
cbr.berjalan(180)

print('==='*30)
# bisa juga kita panggil fungsi pada kelas induk, spt pada pewarisan sblmnya

class makhlukhidup:
    def bicara(self):
        print('ngomong...')

class kucing(makhlukhidup):
    def bicara(self,bunyi):
        super().bicara()
        print(f'----> dengan suara {bunyi}')

manusia = makhlukhidup()
milli = kucing()

manusia.bicara()
milli.bicara('meonggg')

'''
SIMPULAN
1. Teknik overriding membuat kita bisa memodifikasi fungsi yang sudah didefinisikan pada kelas Induk
2. Kita juga bisa mempertahankan fungsi asli yang terdapat pada kelas induk dengan memanggil fungsi super()
'''