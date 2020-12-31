class MenuUtama:
    def __init__(self):
        pass
        
    @staticmethod
    def menuUtama():
        print("*"*50)
        print("="*50)
        print("            === Remember Me ===")
        print("="*50,"\n","Pilihan Menu")
        print("1. Menu Jadwal")
        print("2. Menu Tugas")
        print("0. Kembali")
        print("*"*50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            from ClassJadwal import MenuJadwal
            print("*" * 50,"\n")
            print("MENU JADWAL")
            jadwal=MenuJadwal()
            jadwal.menu()
        elif menu == "2":
            print("*" * 50,"\n")
            from ClassTugas import MenuTugas
            print("MENU TUGAS")
            tugas=MenuTugas()
            tugas.menu()
        elif menu == "0":
            print("*" * 50,"\n")
            from ClassMahasiswa import programBerjalan
            programBerjalan()
        else:
            print("Menu salah!, Masukan Ulang!")
            MenuUtama.menuUtama()

#Overiding 
#Encapsulation
#

