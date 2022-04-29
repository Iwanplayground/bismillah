'''
Access Modifiers adalah sebuah konsep di dalam pemrograman berorientasi objek 
di mana kita bisa mengatur hak akses suatu atribut dan fungsi pada sebuah class.

access modifier di py itu ada 3: public,protect,Private
'''

# public

class belahketupat:

    def __init__(self,diagonal1,diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.luas = (diagonal1*diagonal2)*0.5

ketupatlebaran = belahketupat(50,60)
print(f'diagonal satu : {ketupatlebaran.diagonal1}')
print(f'diagonal dua : {ketupatlebaran.diagonal2}')
print(f'dengan kedua diagonal seperti itu didapatkan luasnya adalah : {ketupatlebaran.luas}')

'''Kemudian ia juga memiliki 
3 buah atribut (diagonal 1 dan 2 dan  luas) yang mana semuanya memiliki 
hak akses publik. Soalnya kita bisa liat itu kan diaksesnya diluar class '''


print('==='*30)
# protect
# Untuk mendefinisikan atribut dengan hak akses protected, 
# kita harus menggunakan prefix underscore _ sebelum nama variabel.

class pesawat:
    def __init__(self,merk):
        self._merk = merk

        # kita coba akses diluar bisa atau ga?

cesnna = pesawat('cesnna F089')
print(f'merk : {cesnna._merk}') 

'''
Kita masih bisa mengakses atribut _merk dari luar kelas, 
karena hal ini hanya bersifat convention alias adat atau kebiasaan saja 
yang harus disepakati oleh programmer. Di mana jika suatu 
atribut diawali oleh _, maka ia harusnya tidak boleh diakses 
kecuali dari internal kelas tersebut atau dari kelas yang mewarisinya.
'''

# seperti ini contohnya

class Mobil:
  def __init__(self, merk):
    self._merk = merk

class Mobillistrik(Mobil):
  def __init__(self, merk, total_voltase):
    super().__init__(merk)
    self._total_voltase = total_voltase

  def pamer(self):
    # akses _merk dari subclass
    print(
      f'Ini mobil {self._merk} dengan total gear {self._total_voltase}'
    )

tesla = Mobillistrik('TESLA',220)
tesla.pamer()

print('==='*30)
# private
class motor:
  def __init__(self, merk):
    self.__merk = merk

# kita akses dari luar gmn ntar?
'''mio = motor('mio')
print(f'Merk: {mio.__merk}')

 nah udah kita lihat darisitu dia error-->motor object has no attribute __merk '''

# kalo mau akses trs gimana dah?
class motor:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkanmerk(self):
        print(f'tampilkan merknya: {self.__merk}')

vario = motor('vario')
vario.tampilkanmerk()
