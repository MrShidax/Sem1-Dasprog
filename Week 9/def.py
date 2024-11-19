def my_name(nama_saya, umur_saya):
    print(f'Hello my name is {nama_saya}, umur saya saat ini {umur_saya} tahun')
my_name('Umar Al Faris', 18)

def penjumlahan_aneh(a, b):
    hasil_aneh = (a+b)*(a-b)
    return hasil_aneh
print(penjumlahan_aneh(3, 2))
print(f'Hasilnya adalah {penjumlahan_aneh(4,2)}')

def nama_hari(*harinya):
    print(f'Hari ketiga adalah {harinya[2]}')
nama_hari('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')

my_name(umur_saya=18, nama_saya='Umar')

def hari_bulan(**tanggalnya):
    print(f'Hari ini adalah hari {tanggalnya['hari']} dan bulan adalah bulan {tanggalnya['bulan']}')
hari_bulan(hari='Rabu', bulan='Oktober')

def negaraku(country='Indonesia', continent='Asia'):
    print(f'I am from {country}. Its is a part of {continent}')
negaraku('Sweden')
negaraku(continent='Asia Tenggara')
negaraku()

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x,y):
   print('x is '+str(x)+' and y is '+str(y))

my_function(3,4)
my_function(4,5)

#[ERROR tidak boleh key-argument] my_function(x = 3, y = 4)

def my_function(*, x):
    print(x)
    
my_function(x = 5)
#[ERROR hanya bisa key-argument] my_function(5)

def my_function(a,b, /, *, c, d):
    print(a + b + c + d)
    
my_function(5, 6, c = 7, d = 8)