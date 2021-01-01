<<<<<<< HEAD
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
        print("3. Menu Semester")
        print("4. Menu Planning")
        print("0. Kembali")
        print("*"*50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            from ClassJadwal import MenuJadwal
            print("*" * 50,"\n")
            print("MENU JADWAL")
            jadwal=MenuJadwal()#class child
            jadwal.menu()
        elif menu == "2":
            print("*" * 50,"\n")
            from ClassTugas import MenuTugas
            print("MENU TUGAS")
            tugas=MenuTugas()#class child
            tugas.menuTugas()
        elif menu == "3":
            print("*" * 50,"\n")
            from ClassSemester import MenuSemester
            print("MENU SEMESTER")
            tugas=MenuSemester()#class child 
            tugas.menuSemester()
        elif menu == "4":
            print("*" * 50,"\n")
            from ClassPlanning import Planning
            print("MENU PLANNING")
            plan=Planning()#class child 
            plan.menuPlanning()
        elif menu == "0":
            from ClassMahasiswa import programBerjalan
            programBerjalan()
        else:
            print("Menu salah!, Masukan Ulang!")
            MenuUtama.menuUtama()


=======
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
        print("3. Menu Semester")
        print("4. Menu Planning")
        print("0. Kembali")
        print("*"*50)
        menu = input("Pilih Menu Ke-: ")
            
        if menu == "1":
            from ClassJadwal import MenuJadwal
            print("*" * 50,"\n")
            print("MENU JADWAL")
            jadwal=MenuJadwal()#class child
            jadwal.menu()
        elif menu == "2":
            print("*" * 50,"\n")
            from ClassTugas import MenuTugas
            print("MENU TUGAS")
            tugas=MenuTugas()#class child
            tugas.menuTugas()
        elif menu == "3":
            print("*" * 50,"\n")
            from ClassSemester import MenuSemester
            print("MENU SEMESTER")
            tugas=MenuSemester()#class child 
            tugas.menuSemester()
        elif menu == "4":
            print("*" * 50,"\n")
            from ClassPlanning import Planning
            print("MENU PLANNING")
            plan=Planning()#class child 
            plan.menuPlanning()
        elif menu == "0":
            from ClassMahasiswa import programBerjalan
            programBerjalan()
        else:
            print("Menu salah!, Masukan Ulang!")
            MenuUtama.menuUtama()


>>>>>>> df21c25ee1da9876e743cee97a333bfaf17958e6
