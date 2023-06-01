class Mahasiswa:
#Deklarasi kelas Mahasiswa
    def __init__(self, nama, nim, jurusan):
    #Konstruktor dari kelas
    #Untuk Self merupakan parameter pertama yang digunakan untuk merujuk pada objek yang sedang dibuat
    #Selain itu merupakan parameter yang akan menerima nilai
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        #inisialisasi atribut Nama, NIM, dan Jurusan ketiganya memakai tipe data String 

    def tampilkan_info(self):
    #Deklarasi method untuk menampilkan informasi mahasiswa
        print("Nama Mahasiswa:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan Mahasiswa:", self.jurusan.NamaJurusan)
        #Mencetak data dari objek mahasiswa yaitu nama, NIM, dan jurusan mahasiswa
        #NamaJurusan merupakan atribut dari objek Jurusan


class Jurusan:
#Deklarasi kelas Jurusan
    def __init__(self, nama_jurusan):
    #Konstruktor dari kelas
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
        #inisialisasi atribut NamaJurusan dan DaftarMahasiswa
        #DaftarMahasiswa diinisialisasi sebagai list 

    def tambah_mahasiswa(self, mahasiswa):
    #Deklarasi Method untuk menambahkan mahasiswa ke dalam DaftarMahasiswa
        self.DaftarMahasiswa.append(mahasiswa)
        #Menggunakan method append() untuk menambahkan mahasiswa ke dalam list DaftarMahasiswa

    def tampilkan_daftar_mahasiswa(self):
    #Deklarasi Method untuk menampilkan daftar mahasiswa
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        #Mencetak daftar Mahasiswa yang terdaftar di jurusan
        for mahasiswa in self.DaftarMahasiswa:
        #Perulangan for untuk mengiterasi setiap elemen dalam list DaftarMahasiswa
            print("- Nama:", mahasiswa.nama)
            print("  NIM:", mahasiswa.nim)
            #Mencetak nama dan nim setiap objek mahasiswa dalam list DaftarMahasiswa


class Universitas:
#Deklarasi kelas Universitas
    def __init__(self, nama_universitas):
    #Konstruktor dari kelas
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
        #inisialisasi atribut NamaUniversitas dan DaftarJurusan
        #DaftarJurusan diinisialisasi sebagai list 

    def tambah_jurusan(self, jurusan):
    #Deklarasi method untuk menambahkan jurusan ke dalam list DaftarJurusan
        self.DaftarJurusan.append(jurusan)
        #Juga menggunakan method append() untuk menambahkan jurusan ke dalam list DaftarJurusan

    def tampilkan_daftar_jurusan(self):
    #Deklarasi method untuk menampilkan daftar jurusan
        print("\nDaftar Jurusan di Universitas", self.NamaUniversitas)
        #Mencetak judul sesuai dengan nama universitas
        for jurusan in self.DaftarJurusan:
            #Perulangan for untuk mengiterasi setiap elemen dalam list DaftarJurusan
            print("- Jurusan:", jurusan.NamaJurusan)
            #Mencetak nama dan nim setiap objek mahasiswa dalam list DaftarMahasiswa


universitas1 = Universitas("XYZ University")
#Membuat objek universitas1
jurusan1 = Jurusan("Teknik Informatika")
#Membuat objek jurusan1
universitas1.tambah_jurusan(jurusan1)
#Menambahkan objek jurusan1 ke dalam universitas1
mahasiswa1 = Mahasiswa("Ahmad Zul Zhafran", "G1A022088", jurusan1)
#Membuat objek mahasiswa1 dengan data asli saya sendiri: nama "Ahmad Zul Zhafran", NIM "G1A022088", dan jurusan objek Jurusan Informatika
jurusan1.tambah_mahasiswa(mahasiswa1)
#Menambahkan objek mahasiswa1 ke dalam jurusan1
mahasiswa1.tampilkan_info()
#Menampilkan informasi mahasiswa1

universitas1.tampilkan_daftar_jurusan()
#Menampilkan daftar jurusan di Universitas XYZ
jurusan1.tampilkan_daftar_mahasiswa()
# Menampilkan daftar mahasiswa di Jurusan Informatika

print("\n===============PBO Kelas B===============")
print("\n============Ahmad Zul Zhafran============")
print("\n================G1A022088================")