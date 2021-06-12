import os
import sys


def pembuka():
    print("        Selamat Datang di Perpustakaan FT 11 Maret          ")
    x = input("daftar sebagai anggota dulu, ya(Y/N)!")
    if x == "Y":
        daftar()
    elif x == "N":
        name = input("Masukkan nama peminjam: ")
        NIM = input("maukkan 5 digit terakhir NIM Anda")
        a = "Pinjaman-" + name + NIM + ".txt"
        try:
            with open(a, "r") as f:
                lines = f.readlines()
                lines = [a.strip("Rp") for a in lines]

            with open(a, "r") as f:
                data = f.read()
                print(data)
        except:
            print("Nama anggota salah")
            kembalikan_buku()

        b = "Pengembalian-" + name + NIM + ".txt"
        with open(b, "w+")as f:
            f.write("                Perpustakaan FT 11 Maret \n")
            f.write("                   Dikembalikan oleh: " + name + "\n")
            f.write("    Tanggal: " + getDate() + "    Waktu:" + getTime() + "\n\n")
            f.write("S.N.\t\tJudul Buku\t\tTotal\n")
        menu_awal()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()


def menu_awal():
    print("------------------------------------------------------")
    print(" 1 Daftar Buku dan Toko Buku")
    print(" 2 Peminjaman Buku")
    print(" 3 Pengembalian Buku")
    print(" 4 Pencarian Buku")
    print(" 5 Kritik dan Saran")
    print(" 6 Keluar")
    print("------------------------------------------------------")
    choice = input("pilih nomor fitur yang ingin Anda gunakan (1/2/3/4/5):")

    if choice == "1":
        display_buku()
        menu_awal()

    if choice == "2":
        pinjamkan_buku()
        menu_awal()

    if choice == "3":
        kembalikan_buku()
        menu_awal()

    if choice == '4':
        referensi_buku()
        menu_awal()

    if choice == '5':
        kritik_saran()
        menu_awal()


def daftar():
    success = False
    while (True):
        NamaDepan = input("Masukkan nama depan peminjam: ")
        if NamaDepan.isalpha():
            break
    while (True):
        NIM = input("masukkan 5 digit terakhir NIM anda: ")
        if NIM.isnumeric():
            menu_awal()
            break
        print("")

    filepinjam = "Pinjaman-" + NamaDepan + NIM + ".txt"


def listSplit():
    global judul_buku
    global pengarang
    global tahunterbit
    global toko
    global harga
    global jumlah_stok
    judul_buku = []
    pengarang = []
    tahunterbit = []
    toko = []
    harga = []
    jumlah_stok = []
    with open("daftarbuku_toko", "r+") as f:

        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]

        for i in range(len(lines)):
            ind = 0
            for a in lines[i].split(','):
                if (ind == 0):
                    judul_buku.append(a)
                elif (ind == 1):
                    pengarang.append(a)
                elif (ind == 2):
                    toko.append(a)
                elif (ind == 3):
                    tahunterbit.append(a)
                elif (ind == 4):
                    harga.append(a.strip("Rp"))
                elif (ind == 5):
                    jumlah_stok.append(a)

                ind += 1


def getDate():
    import datetime
    now = datetime.datetime.now
    return str(now().date())


def getTime():
    import datetime
    now = datetime.datetime.now
    return str(now().time())


def display_buku():
    with open("daftarbuku_toko", "r+") as f:
        lines = f.read()
        print(lines)
        print()


# meminjamkan buku

def pinjamkan_buku():
    listSplit()
    success = False
    while (True):
        NamaDepan = input("Masukkan nama depan peminjam: ")
        if NamaDepan.isalpha():
            break
        print("Masukkan huruf A-Z")
    while (True):
        NIM = input("masukkan 5 digit terakhir NIM: ")
        if NIM.isnumeric():
            break
        print("Masukkan huruf A-Z")
        print("")
    display_buku()

    t = "Pinjaman-" + NamaDepan + NIM + ".txt"
    with open(t, "w+") as f:
        f.write("               Perpustakaan FT 11 Maret \n")
        f.write("                   Dipinjam oleh: " + NamaDepan + " " + NIM + "\n")
        f.write("    Tanggal: " + getDate() + "    Waktu:" + getTime() + "\n\n")
        f.write("S.N. \t\t Judul buku \t      Pengarang \n")

    while success == False:
        print("Pilih menu di bawah ini :")
        for i in range(len(judul_buku)):
            print("Masukkan", i, "untuk meminjam buku", judul_buku[i])

        try:
            a = int(input())
            try:
                if (int(jumlah_stok[a]) > 0):
                    print("Buku Tersedia")
                    with open(t, "a") as f:
                        f.write("1. \t\t" + judul_buku[a] + "\t\t  " + pengarang[a] + "\n")

                    jumlah_stok[a] = int(jumlah_stok[a]) - 1
                    with open("daftarbuku_toko", "r+") as f:
                        for i in range(len(pengarang)):
                            f.write(
                                judul_buku[i] + "," + pengarang[i] + "," + toko[i] + "," + tahunterbit[i] + "," + "Rp" +
                                harga[i] + "," + str(jumlah_stok[i]) + "\n")

                    # jika buku yang dipinjam lebih dari 1
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Apakah ingin pinjam buku lagi ? Masukkan y jika ya dan n jika tidak."))
                        if (choice.upper() == "Y"):
                            count = count + 1
                            print("Pilih menu di bawah ini :")
                            for i in range(len(judul_buku)):
                                print("Masukkan", i, "untuk meminjam buku", judul_buku[i])
                            a = int(input())
                            if (int(jumlah_stok[a]) > 0):
                                print("Buku tersedia")
                                with open(t, "a") as f:
                                    f.write(str(count) + ". \t\t" + judul_buku[a] + "\t\t  " + pengarang[a] + "\n")

                                jumlah_stok[a] = int(jumlah_stok[a]) - 1
                                with open("daftarbuku_toko", "r+") as f:
                                    for i in range(len(pengarang)):
                                        f.write(judul_buku[i] + "," + pengarang[i] + "," + toko[i] + "," + tahunterbit[
                                            i] + "," + "Rp" + harga[i] + "," + str(jumlah_stok[i]) + "\n")
                                        success = False
                                        continue
                            else:
                                loop = False
                                continue
                        elif (choice.upper() == "N"):
                            print("Terimakasih telah meminjam buku. ")
                            print("")
                            loop = False
                            success = True
                        else:
                            print("Masukkan sesuai petunjuk !")

                else:
                    print("Buku tidak tersedia")
                    pinjamkan_buku()
                    success = False
                    continue
            except IndexError:
                print("")
                print("Pilih buku sesuai nomor.")
                sys.exit()
        except ValueError:
            print("")
            print("Pilih sesuai petunjuk !.")


# mengembalikan buku
def kembalikan_buku():
    name = input("Masukkan nama peminjam: ")
    NIM = input("Masukkan 5 NIM terakhir: ")
    a = "Pinjaman-" + name + NIM + ".txt"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("Rp") for a in lines]

        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("Nama peminjam salah")
        kembalikan_buku()

    b = "Pengembalian-" + name + ".txt"
    with open(b, "w+")as f:
        f.write("                Perpustakaan FT 11 Maret \n")
        f.write("                   Dikembalikan oleh: " + name + "\n")
        f.write("    Tanggal: " + getDate() + "    Waktu:" + getTime() + "\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")
    a = int(input("berapa total buku Anda?"))
    d = str(input("apakah Anda mengembalikan setelah lebih dari 3 hari?(y/n)"))
    if d == 'y':
        p = (2000 + (a * 500))
    elif d == 'n':
        p = (a * 500)

    print("total yang harus anda bayar adalah sebesar", p, "rupiah")


# referensi buku
def referensi_buku():
    listSplit()
    ulang = "Y"
    while ulang.upper() == "Y":
        judul = str(input("Masukkan judul buku : "))
        writer = str(input("Masukkan pengarang buku : "))
        tahun = str(input("Masukkan tahun terbit buku : "))
        if (judul.title() in judul_buku) and (writer.title() in pengarang) and (tahun in tahunterbit):
            i = judul_buku.index(judul.title())
            print(f"Buku dengan judul {judul}, tahun terbit {tahun}, dengan pengarang{writer} dapat ditemukan di {toko[i]}")
        else:
            print("Maaf buku tidak ditemukan di toko manapun")
        ulang = str(input("Ulangi pencarian [Y/T] : "))
    print("Program selesai, terima kasih")
pembuka()


# kritikdansaran
def kritik_saran():
    kritik = input("Masukkan kritik : ")
    saran = input("Masukkan saran : ")

    print(kritik, saran)


menu_awal()
