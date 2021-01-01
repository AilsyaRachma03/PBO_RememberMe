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
class Semester:
    def __init__(self):
        pass

class MenuSemester():
    @staticmethod
    def menuSemester():
        print("="*50)
        print("             === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Tampilkan data Semester")
        print("2. Cari Semester")
        print("3. Membuat data Semester")
        print("4. Update data Semester")
        print("5. Hapus data Semester")
        print("0. Kembali")
        print("*" * 50)
        menu = input("Pilih Menu Ke-: ")

        if menu == "1":
            print("*"*50)
            print("MENU MENAMPILKAN DATA SEMESTER")
            MenuSemester.lihat(db)
        elif menu == "2":
            print("*"*50)
            print("MENU MENCARI DATA SEMESTER")
            MenuSemester.cari(db)
        elif menu == "3":
            print("*"*50)
            print("MENU INSERT DATA SEMESTER BARU")
            MenuSemester.masukan(db)
        elif menu == "4":
            print("*"*50)
            print("MENU UPDATE DATA SEMESTER")
            MenuSemester.update(db)
        elif menu == "5":
            print("*"*50)
            print("MENU MENGHAPUS DATA SEMESTER")
            MenuSemester.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
            # from ClassMahasiswa import programBerjalan
            # programBerjalan()
            # exit()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM semester"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Semester     : ',x[0])
                print('IP           : ',x[1])
                print('IPK          : ',x[2])
                print('Catatan      : ',x[3])
                print('-'* 50)

    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Semester atau IPK yang dicari: ")
        sql = "SELECT * FROM semester WHERE semester LIKE %s OR IPK LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Semester     : ',x[0])
                print('IP           : ',x[1])
                print('IPK          : ',x[2])
                print('Catatan      : ',x[3])
                print('-'* 50)

    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah data Semester Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                semester = input("Masukan Semester : ")
                IP =float(input("Masukan IP : "))
                IPK= float(input("Masukan IPK : "))
                Catatan = input("Masukan Catatan : ")
                val = (semester, IP, IPK, Catatan)
                cursor = db.cursor()
                sql = "INSERT INTO semester (semester, IP, IPK, Catatan) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            MenuSemester.menuSemester()
    
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Semester ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                semester = input("Masukan Id Data yang akan Diubah: ")
                IP = input("Masukan IP baru: ")
                IPK = input("Masukan IPK baru: ")
                Catatan = input("Masukan Catatan baru: ")
                sql = "UPDATE semester SET IP=%s, IPK=%s, Catatan=%s WHERE semester=%s"
                val = (IP, IPK, Catatan ,semester)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            MenuSemester.menuSemester()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                semester = input("pilih Semester : ")
                sql = "DELETE FROM semester WHERE semester=%s"
                val = (semester,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data Semester : {}".format(e))
        else:
            MenuSemester.menuSemester()

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
class Semester:
    def __init__(self):
        pass

class MenuSemester():
    @staticmethod
    def menuSemester():
        print("="*50)
        print("             === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Tampilkan data Semester")
        print("2. Cari Semester")
        print("3. Membuat data Semester")
        print("4. Update data Semester")
        print("5. Hapus data Semester")
        print("0. Kembali")
        print("*" * 50)
        menu = input("Pilih Menu Ke-: ")

        if menu == "1":
            print("*"*50)
            print("MENU MENAMPILKAN DATA SEMESTER")
            MenuSemester.lihat(db)
        elif menu == "2":
            print("*"*50)
            print("MENU MENCARI DATA SEMESTER")
            MenuSemester.cari(db)
        elif menu == "3":
            print("*"*50)
            print("MENU INSERT DATA SEMESTER BARU")
            MenuSemester.masukan(db)
        elif menu == "4":
            print("*"*50)
            print("MENU UPDATE DATA SEMESTER")
            MenuSemester.update(db)
        elif menu == "5":
            print("*"*50)
            print("MENU MENGHAPUS DATA SEMESTER")
            MenuSemester.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
            # from ClassMahasiswa import programBerjalan
            # programBerjalan()
            # exit()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM semester"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Semester     : ',x[0])
                print('IP           : ',x[1])
                print('IPK          : ',x[2])
                print('Catatan      : ',x[3])
                print('-'* 50)

    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Semester atau IPK yang dicari: ")
        sql = "SELECT * FROM semester WHERE semester LIKE %s OR IPK LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Semester     : ',x[0])
                print('IP           : ',x[1])
                print('IPK          : ',x[2])
                print('Catatan      : ',x[3])
                print('-'* 50)

    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah data Semester Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                semester = input("Masukan Semester : ")
                IP =float(input("Masukan IP : "))
                IPK= float(input("Masukan IPK : "))
                Catatan = input("Masukan Catatan : ")
                val = (semester, IP, IPK, Catatan)
                cursor = db.cursor()
                sql = "INSERT INTO semester (semester, IP, IPK, Catatan) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            MenuSemester.menuSemester()
    
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Semester ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                semester = input("Masukan Id Data yang akan Diubah: ")
                IP = input("Masukan IP baru: ")
                IPK = input("Masukan IPK baru: ")
                Catatan = input("Masukan Catatan baru: ")
                sql = "UPDATE semester SET IP=%s, IPK=%s, Catatan=%s WHERE semester=%s"
                val = (IP, IPK, Catatan ,semester)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            MenuSemester.menuSemester()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                semester = input("pilih Semester : ")
                sql = "DELETE FROM semester WHERE semester=%s"
                val = (semester,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data Semester : {}".format(e))
        else:
            MenuSemester.menuSemester()

while True:
>>>>>>> df21c25ee1da9876e743cee97a333bfaf17958e6
    MenuSemester.menuSemester()