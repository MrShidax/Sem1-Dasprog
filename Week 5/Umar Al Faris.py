#Tugas 3 Soal di bawah code contoh



# #Create String
string0 = "Umar Al Faris"
string1 = "5054241015"
string2 = "Bogor"

#Print String
print("Nama saya adalah : " + string0)
print("NRP : " + string1)
print("Asal Daerah : " + string2)

#Access character in string
print("Inisial Saya : " + string0[0] + string0[5] + string0[8])

#String Slicing
print("Nama belakang saya : " + string0[8:])
print("Nama panggilan saya : " + string0[0:4])

#Reverse String
print("Reverse dari NRP saya adalah : " + string1[::-1])

#Update String
string3 = "Saya Mahasiswa RKA"

#Ubah menjadi "Saya Bukan Mahasiswa RPL"
#Menggunakan convert list lalu join
list3 = list(string3)
list3[4] = " bukan "
string4 = "".join(list3)
string5 = string4[0:21] + "RPL"
print(string5)

#menggunakan method
string6 = string3.replace("Mahasiswa RKA", "bukan mahasiswa RPL")
print(string6)
print("")
print("----------- PEMBATAS -----------")
print("")
#----------------------------------------
#Tugas Implementasi
#1 Deleting a character dari kota asal
#2 Escape Sequencing in Python + Example
#3 Python String Formating (Example 1, 2, 3, 4)

#1 Deleting a character dari kota asal
# Menghapus huruf G (Index ke 2)
print("Nomor 1")
list4 = list(string2)
list4[2] = ""
string7 = "".join(list4)
print("Menghapus huruf g (Index ke 2)")
print(string7)
print("")

print("Nomor 2")
#2 Escape Sequencing in Python + Example
# Contoh String Octal
string8 = "Nama Saya : \125\155\141\162\040\101\154\040\106\141\162\151\163"
print(f"Contoh String Octal => {string8}")

# Contoh String HEX
string9 = "Nama Saya : \x55\x6d\x61\x72\x20\x41\x6c\x20\x46\x61\x72\x69\x73"
print(f"Contoh String HEX => {string9}")

# Contoh Raw String Octal dan HEX
string10 = r"Raw Octal : \125\155\141\162\040\101\154\040\106\141\162\151\163"
print(string10)
string11 = r"Raw HEX : \x55\x6d\x61\x72\x20\x41\x6c\x20\x46\x61\x72\x69\x73"
print(string11)
print("")

print("Nomor 3")
print("")

print("Example 1")
string12 = "{} {} {}".format("Umar", "Al", "Faris")
print(string12)
string12 = "{2} {0} {1}".format("Umar", "Al", "Faris")
print(string12)
string12 = "{U} {F} {A}".format(U="Umar", A="Al", F="Faris")
print(string12)
print("")

print("Example 2")
string13 = "{0:b}".format(135)
print(string13)
string14 = "{0:e}".format(123.456789)
print(string14)
string15 = "{0:.2f}".format(1/3)
print(string15)
print("")

print("Example 3")
string16 = "|{:<10}|{:^10}|{:>10}|".format("Umar", "Al", "Faris")
print(string16)
string17 = "\n{0:^20} Lahir Pada Tahun {1:>10}".format("Umar Al Faris", 2006)
print(string17)
print("")

print("Example 4")
INT1 = 12.3456789
print("Formatting minimal panjang 3 dan minimal 2 angka desimal")
print("%3.2f" % INT1)
print("Formatting minimal panjang 3 dan minimal 4 angka desimal")
print("%3.4f" % INT1)