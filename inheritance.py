class mhs:

    def __init__ (self, nama, kampus):
        self.nama = nama
        self.kampus = kampus

    def perkenalan (self):
        print(f'Perkenalkan nama saya {self.nama} dari kampus {self.kampus}')

iwan = mhs('Ridwan','Nanyang Technological University')
iwan.perkenalan()

# membuat objek turunannya

class mhsjurusan(mhs):
    pass

class mhsorganisasi(mhs):
    pass

andi = mhsjurusan('andi','UI')
somad = mhsorganisasi('somade','UGM')

andi.perkenalan()
somad.perkenalan()

print('==='*30)

# Membuat konstruktor pada kelas turunan
'''
Apa yang terjadi ketika kelas turunan memiliki konstruktor sendiri?
Ia akan menimpa konstruktor dari kelas induk sehingga konstruktor 
kelas induk tidak akan pernah dieksekusi.

konstruktor kelas parent tidak lagi dieksekusi ketika kita membuat instance dari kelas child. 
Hal itu terjadi karena sekarang kedua kelas tersebut telah memiliki konstruktor sendiri

'''

# jelasnya kita tidak ingin menimpa konstruk pada kelas parent, maka solusi yang dapat dilakukan adalah:
'''
yang pertama menggunakan fungsi super().__init__()
dan yang kedua menggunakan classparent.__init__()
'''

class mhsjurusan(mhs):
    def __init__(self, nama, kampus):
        super().__init__(nama, kampus)


andi = mhsjurusan('andi','UI')
andi.perkenalan()

# untuk nambah properti/item baru yg ndada di class parent ya tinggal tambah pake self aja di childnya.
