<<<<<<< HEAD
# from ClassMahasiswa import Mahasiswa

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "rememberme"
)
#con itu untuk koneksi ke database kalau cursor buat eksekusi kode

class Jadwal:
    def __init__(self, IdJadwal, Hari, Jam, MataKuliah, Keterangan):
        self.IdJadwal= IdJadwal
        self.Hari= Hari
        self.Jam = Jam
        self.MataKuliah = MataKuliah
        self.Keterangan = Keterangan

class MenuJadwal():
    @staticmethod
    def menu():
        print("="*50)
        print("             === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Tampilkan Jadwal")
        print("2. Cari Jadwal")
        print("3. Membuat Jadwal")
        print("4. Update Jadwal")
        print("5. Hapus Jadwal")
        print("0. Kembali")
        print("*" * 50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            print("*"*50)
            print("MENU MENAMPILKAN JADWAL")
            MenuJadwal.lihat(db)
        elif menu == "2":
            print("*"*50)
            print("MENU MENCARI DATA")
            MenuJadwal.cari(db)
        elif menu == "3":
            print("*"*50)
            print("MENU INSERT DATA BARU")
            MenuJadwal.masukan(db)
        elif menu == "4":
            print("*"*50)
            print("MENU UPDATE DATA")
            MenuJadwal.update(db)
        elif menu == "5":
            print("*"*50)
            print("MENU MENGHAPUS DATA")
            MenuJadwal.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM jadwalkuliah"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Id           : ',x[0])
                print('Hari         : ',x[1])
                print('Mata Kuliah  : ',x[2])
                print('Jam          : ',x[3])
                print('Keterangan   : ',x[4])
                print('-'* 50)
    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Hari atau Mata Kuliah yang dicari: ")
        sql = "SELECT * FROM jadwalkuliah WHERE Hari LIKE %s OR MataKuliah LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            print("Data telah ditemukan : ")
            for x in results:
                print('Id           : ',x[0])
                print('Hari         : ',x[1])
                print('Mata Kuliah  : ',x[2])
                print('Jam          : ',x[3])
                print('Keterangan   : ',x[4])
                print('-'* 50)

    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah Jadwal Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                hari = input("Masukan Hari: ")
                matkul = input("Masukan Nama Mata Kuliah: ")
                jam = input("Masukan Jam Format [jam:menit:detik] : ")
                ket = input("Masukan Keterangan : ")
                val = (hari, matkul, jam, ket)
                cursor = db.cursor()
                sql = "INSERT INTO jadwalkuliah (Hari, MataKuliah, Jam, Keterangan) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            MenuJadwal.menu()
    
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Jadwal ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                Id = input("Masukan Id Data yang akan Diubah: ")
                hari = input("Masukan Hari: ")
                matkul = input("Masukan Nama Mata Kuliah: ")
                jam = input("Masukan Jam Format [jam:menit:detik] : ")
                ket = input("Masukan Keterangan : ")

                sql = "UPDATE jadwalkuliah SET Hari=%s, MataKuliah=%s, Jam=%s, Keterangan=%s WHERE IdJadwal=%s"
                val = (hari, matkul, jam, ket, Id)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            MenuJadwal.menu()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data Jadwal ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                Id = input("pilih Id : ")
                sql = "DELETE FROM jadwalkuliah WHERE IdJadwal=%s"
                val = (Id,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data : {}".format(e))
        else:
            MenuJadwal.menu()

while True:
=======
# from ClassMahasiswa import Mahasiswa

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "rememberme"
)
#con itu untuk koneksi ke database kalau cursor buat eksekusi kode

class Jadwal:
    def __init__(self, IdJadwal, Hari, Jam, MataKuliah, Keterangan):
        self.IdJadwal= IdJadwal
        self.Hari= Hari
        self.Jam = Jam
        self.MataKuliah = MataKuliah
        self.Keterangan = Keterangan

class MenuJadwal():
    @staticmethod
    def menu():
        print("="*50)
        print("             === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Tampilkan Jadwal")
        print("2. Cari Jadwal")
        print("3. Membuat Jadwal")
        print("4. Update Jadwal")
        print("5. Hapus Jadwal")
        print("0. Kembali")
        print("*" * 50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            print("*"*50)
            print("MENU MENAMPILKAN JADWAL")
            MenuJadwal.lihat(db)
        elif menu == "2":
            print("*"*50)
            print("MENU MENCARI DATA")
            MenuJadwal.cari(db)
        elif menu == "3":
            print("*"*50)
            print("MENU INSERT DATA BARU")
            MenuJadwal.masukan(db)
        elif menu == "4":
            print("*"*50)
            print("MENU UPDATE DATA")
            MenuJadwal.update(db)
        elif menu == "5":
            print("*"*50)
            print("MENU MENGHAPUS DATA")
            MenuJadwal.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM jadwalkuliah"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Id           : ',x[0])
                print('Hari         : ',x[1])
                print('Mata Kuliah  : ',x[2])
                print('Jam          : ',x[3])
                print('Keterangan   : ',x[4])
                print('-'* 50)
    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Hari atau Mata Kuliah yang dicari: ")
        sql = "SELECT * FROM jadwalkuliah WHERE Hari LIKE %s OR MataKuliah LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            print("Data telah ditemukan : ")
            for x in results:
                print('Id           : ',x[0])
                print('Hari         : ',x[1])
                print('Mata Kuliah  : ',x[2])
                print('Jam          : ',x[3])
                print('Keterangan   : ',x[4])
                print('-'* 50)

    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah Jadwal Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                hari = input("Masukan Hari: ")
                matkul = input("Masukan Nama Mata Kuliah: ")
                jam = input("Masukan Jam Format [jam:menit:detik] : ")
                ket = input("Masukan Keterangan : ")
                val = (hari, matkul, jam, ket)
                cursor = db.cursor()
                sql = "INSERT INTO jadwalkuliah (Hari, MataKuliah, Jam, Keterangan) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            MenuJadwal.menu()
    
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Jadwal ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                Id = input("Masukan Id Data yang akan Diubah: ")
                hari = input("Masukan Hari: ")
                matkul = input("Masukan Nama Mata Kuliah: ")
                jam = input("Masukan Jam Format [jam:menit:detik] : ")
                ket = input("Masukan Keterangan : ")

                sql = "UPDATE jadwalkuliah SET Hari=%s, MataKuliah=%s, Jam=%s, Keterangan=%s WHERE IdJadwal=%s"
                val = (hari, matkul, jam, ket, Id)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            MenuJadwal.menu()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data Jadwal ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                Id = input("pilih Id : ")
                sql = "DELETE FROM jadwalkuliah WHERE IdJadwal=%s"
                val = (Id,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data : {}".format(e))
        else:
            MenuJadwal.menu()

while True:
>>>>>>> df21c25ee1da9876e743cee97a333bfaf17958e6
    MenuJadwal.menu()