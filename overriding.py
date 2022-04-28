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
