from Menu import MenuUtama

import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="rememberme")
cursor=conn.cursor()

class Mahasiswa:
    def __init__(self, Nim, NamaMahasiswa):
        self.Nim=Nim
        self.NamaMahasiswa=NamaMahasiswa

    def showInfo(self):
        print("NIM= {}\nNama Mahasiswa = {}".format(self.Nim,self.NamaMahasiswa))

def Registrasi():
    Nim=str(input("Masukkan NIM: "))
    NamaMahasiswa=str(input("Masukkan Nama        : "))
    query="Insert into mahasiswa values('{}','{}')".format(Nim,NamaMahasiswa)
    cursor.execute(query)
    conn.commit()
    print("Registrasi Berhasil,Silahkan Login")

def Login():
    for i in range(3):
        Nim = str(input("Masukkan NIM\t\t: "))
        NamaMahasiswa = str(input("Masukkan Nama\t: "))
        query= "select Nim from mahasiswa where Nim='{}' and NamaMahasiswa='{}'".format(Nim,NamaMahasiswa) 
        try: 
            cursor.execute(query)
            nim=cursor.fetchall()[0][0]
            print("         Nim dan Nama Benar !")
            print("*" * 50)
            print("Selamat Datang !")
            return nim
        except:
            print("*"* 50, "\nData Anda Masukkan Salah!\nCoba Lagi!\n","*"* 50)
    print("Anda telah gagal Login Sebanyak 3 Kali")
    return False
# Cobak line 28 kamu ubah jadi nim=cursor.fetchall()[0][0],
# terus itu dicut ke isinya
# try yang paling atas sendiri, abis itu return nim nya dak usah dikasih [0][0]
def programBerjalan():
    while True:
        print("                    SELAMAT DATANG\n                      REMEMBER ME \n" ,50*"*") 
        main = int(input("1. Login \n2. Registrasi \n3. Logout \nPilih menu di atas : "))
        print("*"* 50)
        if main == 1:
            print("LOGIN REMEMBER ME")
            print("*"* 50)
            Nim=Login()
            if Nim != False:
                query="select * from mahasiswa where Nim='"+str(Nim)+"'"
                cursor.execute(query)
                dataAkun=cursor.fetchall()[0]
                user=Mahasiswa(dataAkun[0], dataAkun[1])
                user.showInfo()
                menu=MenuUtama()
                menu.menuUtama()
        elif main==2:
            print("REGISTRASI REMEMBER ME")
            print("*" * 50)
            Registrasi()
        elif main==3:
            print("LOG OUT")
            print("*" * 50)
            exit()
        else:
            print("Menu yang anda pilih tidak tersedia")
programBerjalan()



        # elif main==4:
        #     from ClassSemester import MenuSemester
        #     MenuSemester.menuSemester()