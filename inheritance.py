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

