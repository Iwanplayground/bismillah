class orang:

    def __init__ (self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan (self):
        print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')

iwan = orang('Ridwan','JOGJA')
iwan.perkenalan()

# membuat objek turunannya

class mhs(orang):
    pass

class karyawan(orang):
    pass

andi = mhs('andi','jakarta')
somad = karyawan('somade','NTT')

andi.perkenalan()
somad.perkenalan()

