# list data buku
buku = [[1,"Pemrograman Python", "Teknologi", 20],
        [2,"Ensiklopedia", "Umum", 50],
        [3,"Filosofi Jawa", "Filosofi dan Psikologi", 10],
        [4,"Kajian Islam", "Agama", 30],
        [5,"Asal Usul Indonesia", "Sejarah", 45],
        [6,"Membangun Bisnis Yang Baik", "Sosial dan Ekonomi", 55],
        [7,"Belajar Desain Grafis", "Seni dan Rekreasi", 25]]

# fungsi read
def lihat():
    print("_"*85)
    print("|Nomor|Judul Buku\t\t\t  |Kategori\t\t\t      |Jumlah|")
    print("‾"*85)
    for row in buku :
        print("|{: <5}|{: <35}|{: <35}|{: <6}|".format(*row))
    print("‾"*85)

# fungsi tambah
def tambah(a,b,c,d):
    baru = buku.append([a,b,c,d])
    print("\n<<<< Berhasil Menambahkan >>>>\n")
    input("\n<<<< Klilk Enter >>>>")
    return baru

# fungsi edit
def edit() :
    banyak_buku = len(buku) -1
    nomor = int(input("\nMasukan Nomor yang Diganti : "))
    while (banyak_buku >= 0):
        if (nomor == buku[banyak_buku][0]):
            break
        else:
            banyak_buku -= 1
    if (banyak_buku >= 0):
        jud = input("Masukan Judul Baru :")
        kat = input("Masukan Kategori :")
        jum = int(input("Masukan Jumlah :"))
        buku[banyak_buku][0] = nomor
        buku[banyak_buku][1] = jud
        buku[banyak_buku][2] = kat
        buku[banyak_buku][3] = jum
        print("\n<<<< Berhasil Memperbarui >>>>\n")
        input("\n<<<< Klilk Enter >>>>")
        return buku

# fungsi hapus
def hapus():
    banyak_buku = len(buku) -1
    nomor = int(input("\nMasukan Nomor yang Ingin Dihapus : "))
    while (banyak_buku >= 0):
        if (nomor == buku[banyak_buku][0]):
            break
        else:
            banyak_buku -= 1
    if (banyak_buku >= 0):
        kali=3
        while a >= 0:
                buku[banyak_buku].pop(kali)
                kali -= 1
        buku.sort()
        del buku[0]
        print("\n<<<< Berhasil Menghapus >>>>\n")
        input("\n<<<< Klilk Enter >>>>")
        return buku

# prosedur menu
def menu():
    print("\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|             Data Buku Perpustakaan            |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Lihat Data Buku                        |\n"
        "|     2. Tambah Buku                            |\n"
        "|     3. Edit Buku                              |\n"
        "|     4. Hapus Buku                             |\n"
        "|     5. Keluar                                 |\n"
        "|_______________________________________________|\n")
    pilihan = int(input("Pilih pilihan dibawah ini :\n"
    "1. Lihat Data Buku\n"
    "2. Tambah Data Buku\n"
    "3. Edit Data Buku\n"
    "4. Hapus Data Buku\n"
    "5. Keluar\n"
    "Masukkan Pilihan Anda(angka) : "))

    if pilihan == 1 :
        lihat()
        input("\n<<<< Klilk Enter >>>>")
    elif pilihan == 2 :
        lihat()
        Nomor = int(input("\nMasukan Nomor Baru : "))
        Judul = input("Masukkan Judul Buku : ")
        Kategori = (input("Masukkan Kategori Buku : "))
        Jumlah = int(input("Masukkan Jumlah : "))
        tambah(Nomor,Judul,Kategori,Jumlah)
    elif pilihan == 3 :
        lihat()
        edit()
    elif pilihan == 4 :
        lihat()
        hapus()
    elif pilihan == 5 :
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
            "|                  Terimakasih                  |\n"
            "|_______________________________________________|\n")
        exit()
    else : 
        print("\n<<<< Pilihan Anda Tidak Tersedia >>>>\n")
        menu()

if __name__ == "__main__":
    while(True):
        menu()
