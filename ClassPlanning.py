import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "rememberme"
)#con itu untuk koneksi ke database kalau cursor buat eksekusi kode
class Planning:
    def __init__(self):
        pass
    
    @staticmethod
    def menuPlanning():
        print("="*50)
        print("             === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Tampilkan Planning")
        print("2. Cari data Planning")
        print("3. Membuat data Planning")
        print("4. Update data Planning")
        print("5. Hapus data Planning")
        print("0. Kembali")
        print("*" * 50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            print("*"*50)
            print("MENU MENAMPILKAN JADWAL")
            Planning.lihat(db)
        elif menu == "2":
            print("*"*50)
            print("MENU MENCARI DATA")
            Planning.cari(db)
        elif menu == "3":
            print("*"*50)
            print("MENU INSERT DATA BARU PLANNING")
            Planning.masukan(db)
        elif menu == "4":
            print("*"*50)
            print("MENU UPDATE DATA PLANNING")
            Planning.update(db)
        elif menu == "5":
            print("*"*50)
            print("MENU MENGHAPUS DATA")
            Planning.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM planning JOIN semester on planning.semester = semester.semester"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Id           : ',x[0])
                print('semester     : ',x[1])
                print('Planning     : ',x[2])
                print('Harapan      : ',x[3])
                print('-'* 50)
    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Semester atau Id yang dicari: ")
        sql = "SELECT * FROM planning WHERE Id LIKE %s Or semester LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            print("Data telah ditemukan : ")
            for x in results:
                print('Id           : ',x[0])
                print('semester     : ',x[1])
                print('Planning     : ',x[2])
                print('Harapan      : ',x[3])
                print('-'* 50)

    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah Planning Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                semester = input("Masukan Semester: ")
                Planning = input("Masukan Planning: ")
                Harapan = input("Masukan Harapan: ")
                val = (semester, Planning, Harapan)
                cursor = db.cursor()
                sql = "INSERT INTO planning(semester, Planning, Harapan ) VALUES (%s, %s, %s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            Planning.menuPlanning()
    
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Planning?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                Id = input("Masukan Id Data yang akan Diubah: ")
                semester = input("Masukan Semester: ")
                Planning = input("Masukan Planning: ")
                Harapan = input("Masukan Harapan: ")
                val = (semester, Planning, Harapan)

                sql = "UPDATE planning SET semester=%s, Planning=%s, Harapan=%s WHERE Id=%s"
                val =(semester, Planning, Harapan, Id)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            Planning.menuPlanning()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data Planning ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                Id = input("pilih Id : ")
                sql = "DELETE FROM planning WHERE Id=%s"
                val = (Id,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data : {}".format(e))
        else:
            Planning.menuPlanning()

while True:
    Planning.menuPlanning()