bulan_pembelian = ('januari','februari','maret','april','mei',
'juni','juli','agustus','september','oktober','november','desember')

# mengakses dengan indexing slicing
print('kuarter pertama:')
print(bulan_pembelian[0:4])

list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']


# MASUK KE LIST MANIPULATION
# Fitur .append()
print("\n>>> Fitur .append()")
list_makanan.append('Ketoprak')
print(list_makanan)

# Fitur .clear()
print("\n>>> Fitur .clear()")
list_makanan.clear()
print(list_makanan)

# Fitur .count()
print("\n>>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('sudirman')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3

# Fitur .extend(), menggabungkan kedua list spt halnya operator +, kalo diset analog kek update()
print("\n>>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Sate']
list_minuman = ['Es Teh', 'Es Kopi', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)

# Fitur .index()
print("\n>>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 4
print(score_pertama_sud) # akan menampilkan output 5

# Fitur .insert()
print("\n>>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3,'Budi')
print(list_score)

# Fitur .pop(), ngapus dg index kalo mau pake str ya pake aja remove, oiya kalo di set ini ngapusnya acak aja ga index2an
print("\n>>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)

# Fitur .reverse()
print("\n>>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)

# Fitur .sort()
print("\n>>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse=True)# Descending
print(list_menu) 


# MASUK KE SET MANIPULATION


# Fitur .union()
print("\n>>> Fitur .union()") # ini mirip banget sama update
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel1)
print(parcel3)

# Fitur .isdisjoint() 
print("\n>>> Fitur .isdisjoint()") # apakah suatu set disjoint (saling lepas/tidak mengandung elemen yang sama)??
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Kiwi','Melon','Pisang'}
parcel3 = {'Apel','Srikaya','Semangka'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)

# Fitur .issubset()
print("\n>>> Fitur .issubset()") # nilai kebenaran apakah sebuah set merupakan subset dari set lainnya. 
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian','Semangka','Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_A_dalam_C = parcel_A.issubset(parcel_C)
parcel_B_dalam_C = parcel_B.issubset(parcel_C)
print(parcel_A_dalam_C)
print(parcel_B_dalam_C)

# Fitur .intersection()
print("\n>>> Fitur .intersection()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C)

# Fitur .difference()
print("\n>>> Fitur .difference()")
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C)

# Fitur .symmetric_difference()
print("\n>>> Fitur .symmetric_difference()")
parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel','Jeruk','Semangka','Leci'}
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)