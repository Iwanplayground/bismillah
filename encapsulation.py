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

    