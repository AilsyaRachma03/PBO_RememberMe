import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "rememberme"
)
#con itu untuk koneksi ke database kalau cursor buat eksekusi kode
class Tugas:
    def __init__(self, IdTugas, NamaTugas, MataKuliah, TglPemberian, TglPengumpulan, DeadlineJam, KeteranganTugas ):
        self.IdTugas= IdTugas
        self.NamaTugas= NamaTugas
        self.MataKuliah= MataKuliah
        self.TglPemberian= TglPemberian
        self.TglPengumpulan= TglPengumpulan
        self.DeadlineJam= DeadlineJam
        self.KeteranganTugas= KeteranganTugas
        
class MenuTugas():
    @staticmethod
    def menuTugas():
        print("=== Remember Me ===","\n", "Pilihan Menu")
        print("1. Tampilkan Daftar Tugas")
        print("2. Cari Tugas")
        print("3. Membuat Tugas")
        print("4. Update Tugas")
        print("5. Hapus Tugas")
        print("0. Kembali")
        print("*" * 50,"\n")
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            print("MENU MENAMPILKAN DAFTAR TUGAS")
            MenuTugas.lihat(db)
        elif menu == "2":
            print("MENU MENCARI DAFTAR TUGAS")
            MenuTugas.cari(db)
        elif menu == "3":
            print("MENU INSERT DATA TUGAS BARU")
            MenuTugas.masukan(db)
        elif menu == "4":
            print("MENU UPDATE DATA TUGAS")
            MenuTugas.update(db)
        elif menu == "5":
            print("MENU MENGHAPUS DATA TUGAS")
            MenuTugas.hapus(db)
        elif menu == "0":
            from Menu import MenuUtama
            MenuUtama.menuUtama()
        else:
            print("Menu salah!, Masukan Ulang!") 

    @staticmethod 
    def lihat(db):
        cursor = db.cursor()
        sql = "SELECT * FROM tugaskuliah"
        cursor.execute(sql)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            for x in results:
                print('Id Tugas         : ',x[0])
                print('Nama Tugas       : ',x[1])
                print('Mata Kuliah      : ',x[2])
                print('TglPemberian     : ',x[3])
                print('TglPengumpulan   : ',x[4])
                print('Deadline Jam     : ',x[5])
                print('Keterangan Tugas : ',x[6])
                print('-'* 30)

    @staticmethod
    def cari(db):
        cursor = db.cursor()
        keyword = input("Masukan Nama Tugas atau Mata Kuliah yang dicari: ")
        sql = "SELECT * FROM tugaskuliah WHERE NamaTugas LIKE %s OR MataKuliah LIKE %s"
        val = ("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada data")
        else:
            print("Data telah ditemukan : ")
            for x in results:
                print('Nama Tugas       : ',x[1])
                print('Mata Kuliah      : ',x[2])
                print('TglPemberian     : ',x[3])
                print('TglPengumpulan   : ',x[4])
                print('Deadline Jam     : ',x[5])
                print('Keterangan Tugas : ',x[6])
                print('-'* 30)


                print('-'* 30)
    @staticmethod
    def masukan(db):
        print("Apakah Anda Ingin Menambah Tugas Baru?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                NmTugas = input("Masukan Nama Tugas: ")
                MtKuliah = input("Masukkan Mata Kuliah: ")
                TglPem = input("Masukan Tanggal Pemberian tugas [0000-00-00]: ")
                TglPeng = input("Masukan Tanggal Pengumpulan Tugas [0000-00-00]: ")
                DlJam = input("Masukkan Deadline Jam Pengumpulan Tugas [jam:menit:detik]: ")
                KetTugas = input("Masukan Keterangan : ")
                val = (NmTugas, MtKuliah, TglPem, TglPeng, DlJam, KetTugas)
                cursor = db.cursor()
                sql = "INSERT INTO tugaskuliah (NamaTugas, MataKuliah, TglPemberian, TglPengumpulan, DeadlineJam, KeteranganTugas) VALUES (%s, %s, %s, %s, %s,%s)"
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Disimpan".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Input : {}".format(e))
        else:
            MenuTugas.menuTugas()()
        
    @staticmethod
    def update(db):
        print("Apakah Anda Ingin Melakukan Perubahan terhadap Data Tugas ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        print("Sebelumnya lihat data di menu Menampilkan Data (1), untuk mengetahui Identitas lengkap data yang akan diubah")
        if pilih == "Iya":
            try:
                cursor = db.cursor()
                Id = input("Masukan Id Data yang akan Diubah: ")
                NamaTugas = input("Masukan Nama Tugas: ")
                MataKuliah = input("Masukkan Mata Kuliah: ")
                TglPemberian = input("Masukan Tanggal Pemberian tugas [0000-00-00]: ")
                TglPengumpulan = input("Masukan Tanggal Pengumpulan Tugas [0000-00-00]: ")
                DeadlineJam = input("Masukkan Deadline Jam Pengumpulan Tugas [00:00:00]: ")
                KeteranganTugas = input("Masukan Keterangan : ")

                sql = "UPDATE tugaskuliah SET NamaTugas=%s, MataKuliah=%s, TglPemberian=%s, TglPengumpulan=%s, DeadlineJam =%s,KeteranganTugas=%s WHERE IdTugas=%s"
                val = (NamaTugas, MataKuliah, TglPemberian, TglPengumpulan, DeadlineJam, KeteranganTugas, Id)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Diubah".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Update Data : {}".format(e))
        else:
            MenuTugas.menuTugas()

    @staticmethod
    def hapus(db):
        print("Apakah Anda Ingin Menghapus Data Tugas ?")
        pilih=input("Masukan jawaban Iya/ Tidak : ")
        if pilih == "Iya":
            try :
                cursor = db.cursor()
                Id = input("pilih Id : ")
                sql = "DELETE FROM tugaskuliah WHERE IdTugas=%s"
                val = (Id,)
                cursor.execute(sql, val)
                db.commit()
                print("{} Data Berhasil Dihapus".format(cursor.rowcount))
            except mysql.connector.Error as e:
                print("Gagal Hapus Data : {}".format(e))
        else:
            MenuTugas.menuTugas()

while True:
    MenuTugas.menuTugas()

