import datetime, sys, os
import tkinter.messagebox
from tkinter import *

def clr():
	os.system('cls' if os.name == 'nt' else 'clear')

def getDate():
	return str(datetime.datetime.now().date())


def getTime():
	return str(datetime.datetime.now().time())

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

def display_buku(root, x=0, num=0, prev=0, y=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6, back, daftar_buku,\
	btn_prev, index, btn_next, pinjam
	if x:
		menu1.grid_forget()
		menu2.grid_forget()
		menu3.grid_forget()
		menu4.grid_forget()
		menu5.grid_forget()
		menu6.grid_forget()
	if not x and num != 0:
		btn_prev.grid_forget()
		index.grid_forget()
		btn_next.grid_forget()
		daftar_buku.grid_forget()
		back.grid_forget()

	if y and num != 0:
		pinjam.grid_forget()

	with open("daftarbuku_toko", "r") as f:
		lines = f.read().split('\n')
	data = []
	for i in lines:
		i = i.split(',')
		if len(i) < 5: continue
		data.append(
			"Judul : {}\nPengarang : {}\nToko : {}\nTahun : {}\nHarga : {}\nStok : {}".format(
				i[0], i[1], i[2], i[3], i[4], i[5])
			)
	if prev:
		if num < 2: num = 6
		num-=1
	else:
		if num > 4: num = 0
		num+=1
	daftar_buku = Label(root, text=data[num-1])
	btn_prev = Button(root, text="<<", padx=20, pady=10,
						command=lambda: display_buku(root, num=num, prev=1, y=y))
	index = Label(root, text="\t"+str(num)+"\t")
	btn_next = Button(root, text=">>", padx=20, pady=10,
						command=lambda: display_buku(root, num=num, y=y))
	back = Button(root, text="\t\tKembali\t\t\t", padx=20,
					pady=10, command=lambda: menu_awal(root, forget_lihat=1))
	daftar_buku.grid(column=0, row=1, columnspan=3)
	btn_prev.grid(column=0, row=2)
	index.grid(column=1, row=2)
	btn_next.grid(column=2, row=2)
	if y:
		back.grid(column=0, row=4, columnspan=3)
		pinjam = Button(root, text="\t\tPinjam\t\t\t", padx=20,
						pady=10, command=lambda: sub_handle_pinjamkan_buku(num))
		pinjam.grid(column=0, row=3, columnspan=3)
	else:
		back.grid(column=0, row=3, columnspan=3)

def menu_awal(root, x=1, write_data=0, forget_cari=0, forget_lihat=0, forget_KS=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6, judulL, writerL, tahunL,\
	judul, writer, tahun, submit, back, daftar_buku, kritikL, saranL, kritik,\
	saran, pinjamL, pinjam, btn_prev, index, btn_next, pinjam

	if write_data:
		data = "Perpustakaan FT 11 Maret\nDikembalikan oleh : \
		"+write_data[0]+"\nTanggal : "+getDate()+"\nWaktu:"+getTime()+"\
		\nJudul Buku : "+judul+"\nTotal : "+str(p)+" rupiah"
		with open(write_data[1], "w+")as f:
			f.write(data)

	if forget_cari:
		judulL.grid_forget()
		writerL.grid_forget()
		tahunL.grid_forget()
		judul.grid_forget()
		writer.grid_forget()
		tahun.grid_forget()
		submit.grid_forget()
		back.grid_forget()

	if forget_lihat:
		btn_prev.grid_forget()
		index.grid_forget()
		btn_next.grid_forget()
		daftar_buku.grid_forget()
		back.grid_forget()
		try:
			pinjam.grid_forget()
		except:
			pass

	if forget_KS:
		kritikL.grid_forget()
		saranL.grid_forget()
		kritik.grid_forget()
		saran.grid_forget()
		submit.grid_forget()
		back.grid_forget()


	menu1 = Button(root, text="Daftar Buku dan Toko Buku\t\t\t", padx=10,
					pady=10, command=lambda: display_buku(root, x=1))
	menu2 = Button(root, text="Peminjaman Buku\t\t\t\t", padx=10,
					pady=10, command=lambda: pinjamkan_buku(root, x=1))
	menu3 = Button(root, text="Pengembalian Buku\t\t\t", padx=10,
					pady=10, command=lambda: kembalikan_buku(root, x=1))
	menu4 = Button(root, text="Pencarian Buku\t\t\t\t", padx=10,
					pady=10, command=lambda: referensi_buku(root, x=1))
	menu5 = Button(root, text="Kritik dan Saran\t\t\t\t", padx=10,
					pady=10, command=lambda: kritik_saran(root, x=1))
	menu6 = Button(root, text="\t\tKeluar\t\t\t", padx=10,
					pady=10, command=lambda: exit())
	menu1.grid(column=0, row=1)
	menu2.grid(column=0, row=2)
	menu3.grid(column=0, row=3)
	menu4.grid(column=0, row=4)
	menu5.grid(column=0, row=5)
	menu6.grid(column=0, row=6)

def sub_handle_pinjamkan_buku(num):
	global submit, pinjam, daftar_buku, pinjamL, back
	listSplit()
	t = "Pinjaman-"+name.get()+nim.get()+".txt"
	try:
		if int(jumlah_stok[num-1]) > 0:
			with open(t, "a") as f:
				f.write(judul_buku[num-1]+" : "+pengarang[num-1]+"\n")
			jumlah_stok[num-1] = int(jumlah_stok[num-1])-1
			with open("daftarbuku_toko", "r+") as f:
				for i in range(len(pengarang)):
					f.write(judul_buku[i]+","+pengarang[i]+","+toko[i]+","+
						tahunterbit[i]+","+"Rp"+harga[i]+","+str(jumlah_stok[i])+"\n")
			tkinter.messagebox.showinfo("Info", "Terimakasih telah meminjam buku")
		elif int(pinjam.get()) < 1:
			tkinter.messagebox.showinfo("Warning", "Inputan salah")
		else:
			tkinter.messagebox.showinfo("Warning", "Buku tidak tersedia")
	except Exception as e:
		tkinter.messagebox.showinfo("Warning", "Inputan salah")


def handle_pinjamkan_buku(root):
	global nameL, nimL, name, nim, submit, pinjam, daftar_buku, pinjamL, back
	nameL.grid_forget()
	nimL.grid_forget()
	name.grid_forget()
	nim.grid_forget()
	submit.grid_forget()
	if not str(name.get()).isalpha():
		pinjamkan_buku(root)
	else:
		if str(nim.get()).isnumeric():
			t = "Pinjaman-"+name.get()+nim.get()+".txt"
			try:
				with open(t, 'r') as f:
					pass
			except Exception as e:
				with open(t, "w+") as f:
					data = "Perpustakaan FT 11 Maret\nDipinjam oleh: "+name.get()+" "+nim.get()+"\n"
					f.write(data)
			display_buku(root, y=1)
		else:
			pinjamkan_buku(root)

def pinjamkan_buku(root, x=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6, nameL, nimL, name,\
	nim, submit
	if x:
		menu1.grid_forget()
		menu2.grid_forget()
		menu3.grid_forget()
		menu4.grid_forget()
		menu5.grid_forget()
		menu6.grid_forget()
	nameL = Label(root, text="Nama")
	nimL = Label(root, text="NIM")
	name = Entry(root, width=20)
	nim = Entry(root, width=20)
	submit = Button(root, text="Submit", padx=20,
					pady=10, command=lambda: handle_pinjamkan_buku(root))
	nameL.grid(column=0, row=1)
	nimL.grid(column=0, row=2)
	name.grid(column=1, row=1)
	nim.grid(column=1, row=2)
	submit.grid(column=0, row=3, columnspan=2)


def kritik_saran(root, x=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6, kritikL, saranL, kritik,\
	saran, submit, back
	if x:
		menu1.grid_forget()
		menu2.grid_forget()
		menu3.grid_forget()
		menu4.grid_forget()
		menu5.grid_forget()
		menu6.grid_forget()
	kritikL = Label(root, text="Kritik")
	saranL = Label(root, text="Saran")
	kritik = Text(root, height=7.5, width=40)
	saran = Text(root, height=7.5, width=40)
	submit = Button(root, text="\tSubmit\t\t", padx=10,
					pady=10, command=lambda: tkinter.messagebox.showinfo(
						"Kritik, Saran", kritik.get("1.0", "end-1c")+'\n\
						'+saran.get("1.0", "end-1c")))
	back = Button(root, text="\tKembali\t\t", padx=10,
					pady=10, command=lambda: menu_awal(root, forget_KS=1))

	kritikL.grid(column=0, row=1, columnspan=2)
	saranL.grid(column=0, row=3, columnspan=2)
	kritik.grid(column=0, row=2, columnspan=2)
	saran.grid(column=0, row=4, columnspan=2)
	back.grid(column=0, row=5)
	submit.grid(column=1, row=5)

def handle_referensi_buku(judul, writer, tahun):
	listSplit()
	if (judul.title() in judul_buku) and (writer.title() in pengarang) and (tahun in tahunterbit):
		i = judul_buku.index(judul.title())
		data = "Buku dengan judul {}\ntahun terbit {}\ndengan pengarang {}\
		\ndapat ditemukan di {}".format(judul, tahun, writer, toko[i])
		try:
			tkinter.messagebox.showinfo("Info", data)
		except:
			pass
	else:
		try:
			tkinter.messagebox.showinfo("Warning", "Maaf buku tidak ditemukan di toko manapun")
		except:
			pass

def referensi_buku(root, x=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6, judulL, writerL, tahunL,\
	judul, writer, tahun, submit, back
	if x:
		menu1.grid_forget()
		menu2.grid_forget()
		menu3.grid_forget()
		menu4.grid_forget()
		menu5.grid_forget()
		menu6.grid_forget()
	listSplit()
	judulL = Label(root, text="Judul Buku    ")
	writerL = Label(root, text="Pengarang Buku ")
	tahunL = Label(root, text="tahun terbit   ")
	judul = Entry(root, width=20)
	writer = Entry(root, width=20)
	tahun = Entry(root, width=20)
	submit = Button(root, text="Cari", padx=20,
					pady=10, command=lambda: handle_referensi_buku(
						judul.get(), writer.get(), tahun.get()))
	back = Button(root, text="Kembali", padx=20,
					pady=10, command=lambda: menu_awal(root, forget_cari=1))

	judulL.grid(column=0, row=1)
	writerL.grid(column=0, row=2)
	tahunL.grid(column=0, row=3)
	judul.grid(column=1, row=1)
	writer.grid(column=1, row=2)
	tahun.grid(column=1, row=3)
	submit.grid(column=0, row=4)
	back.grid(column=1, row=4)

def sub_handle_kembalikan_buku(root, data, d):
	global aL, a, dL, dx, dy
	if d == 'y':
		p = 2000+(a*500)
	elif d == 'n':
		p = a*500
	dL.grid_forget()
	dx.grid_forget()
	dy.grid_forget()
	try:
		with open(b, 'r') as f:
			data = f.read()
			data_buku_kembali = data+"\nDikembalikan oleh : "+nameX+"\nTanggal :  "+getDate()+"\nWaktu:"+getTime()+"\n"
	except:
		data_buku_kembali = "Perpustakaan FT 11 Maret\nDikembalikan oleh : "+nameX+"\nTanggal : \
		"+getDate()+"\nWaktu:"+getTime()+"\n"
	with open("Pinjaman-"+nameX+nimX+".txt", 'r') as f:
		data = f.read()[:-1].split('\n')[2:]
	for i in data:
		data_buku_kembali+="Judul buku : "+i.split(' : ')[0]+"\n"
	data_buku_kembali+="Total : "+str(p)+" rupiah\n"
	try:
		tkinter.messagebox.showinfo("Info", "Total yang harus anda bayar\n\
			adalah sebesar "+str(p)+" rupiah")
		with open(b, "w")as f:
			f.write(data_buku_kembali)
		with open('daftarbuku_toko', 'r') as f:
			listBuku = f.read()[:-1].split('\n')
		for i in jumlahX:
			for j in listBuku:
				if i in j:
					angka = listBuku[listBuku.index(j)].split(',')[-1]
					angkaBaru = int(angka)+1
					listBuku[listBuku.index(j)] = listBuku[listBuku.index(j)].replace(","+angka, ","+str(angkaBaru))
		result = ""
		for i in listBuku:
			result+=i+'\n'
		with open('daftarbuku_toko', 'w') as f:
			f.write(result)
		os.remove("Pinjaman-"+nameX+nimX+".txt")
	except Exception as e:
		pass
	menu_awal(root)

def handle_kembalikan_buku(root, name, nim, nameL, nimL, submit):
	global aL, a, b, dL, dx, dy, nameX, nimX, jumlahX
	a = "Pinjaman-"+str(name.get())+str(nim.get())+".txt"
	b = "Pengembalian-"+str(name.get())+".txt"
	nameX, nimX = str(name.get()), str(nim.get())
	listSplit()
	name.grid_forget()
	nim.grid_forget()
	nameL.grid_forget()
	nimL.grid_forget()
	submit.grid_forget()
	try:
		with open(a, "r") as f:
			lines = f.readlines()
			lines = [a.strip("Rp") for a in lines]
		with open(a, "r") as f:
			data = f.read()
			data_jumlah = data.split('\n')[2:-1]
			a = len(data[:-1].split('\n'))-2
			data = "\n"+data
		tkinter.messagebox.showinfo("Info", data)
		jumlahX = []
		for i in data_jumlah:
			jumlahX.append(i.split(' : ')[0])
		dL = Label(root, text="Apakah anda mengembalikan\nsetelah lebih dari 3 hari?")
		dx = Button(root, text=" Ya ", padx=20, pady=10,
			command=lambda: sub_handle_kembalikan_buku(root, [nameX, b], 'y'))
		dy = Button(root, text="Tidak", padx=20, pady=10,
			command=lambda: sub_handle_kembalikan_buku(root, [nameX, b], 'n'))

		dL.grid(column=0, row=1, columnspan=2)
		dx.grid(column=0, row=2)
		dy.grid(column=1, row=2)
	except Exception as e:
		tkinter.messagebox.showinfo("Warning", "Nama anggota salah")
		kembalikan_buku(root)

def kembalikan_buku(root, x=0):
	global menu1,  menu2, menu3, menu4, menu5, menu6
	if x:
		menu1.grid_forget()
		menu2.grid_forget()
		menu3.grid_forget()
		menu4.grid_forget()
		menu5.grid_forget()
		menu6.grid_forget()
	nameL = Label(root, text="Nama")
	nimL = Label(root, text="NIM")
	name = Entry(root, width=20)
	nim = Entry(root, width=20)
	submit = Button(root, text="Submit", padx=20, pady=10,
		command=lambda: handle_kembalikan_buku(root, name, nim, nameL, nimL, submit))
	nameL.grid(column=0, row=1)
	nimL.grid(column=0, row=2)
	name.grid(column=1, row=1)
	nim.grid(column=1, row=2)
	submit.grid(column=0, row=3, columnspan=2)

def not_daftar(root, x=1):
	global registL, registY, registN, bannerA, bannerB
	if x:
		bannerA.grid_forget()
		bannerB.grid_forget()
		registL.grid_forget()
		registY.grid_forget()
		registN.grid_forget()
	kembalikan_buku(root)


def handle_daftar(nameL, nimL, name, nim, submit):
	if not str(name.get()).isalpha():
		nameL.grid_forget()
		nimL.grid_forget()
		name.grid_forget()
		nim.grid_forget()
		submit.grid_forget()
		daftar(root, x=0)
	else:
		nameL.grid_forget()
		nimL.grid_forget()
		name.grid_forget()
		nim.grid_forget()
		submit.grid_forget()
		if str(nim.get()).isnumeric():
			menu_awal(root)
		else:
			daftar(root, x=0)

def daftar(root, x=1):
	global registL, registY, registN, bannerA, bannerB
	if x:
		bannerA.grid_forget()
		bannerB.grid_forget()
		registL.grid_forget()
		registY.grid_forget()
		registN.grid_forget()
	root.title("PerpusApp")
	nameL = Label(root, text="Nama")
	nimL = Label(root, text="NIM")
	name = Entry(root, width=20)
	nim = Entry(root, width=20)
	submit = Button(root, text="Submit", padx=20, pady=10,
					command=lambda: handle_daftar(nameL, nimL, name, nim, submit))
	nameL.grid(column=0, row=1)
	nimL.grid(column=0, row=2)
	name.grid(column=1, row=1)
	nim.grid(column=1, row=2)
	submit.grid(column=0, row=3, columnspan=2)
	filepinjam = "Pinjaman-"+str(name.get())+str(nim.get())+".txt"


clr()
root = Tk()
root.title("PerpusApp")
bannerA = Label(root, text="      Selamat datang di")
bannerB = Label(root, text="   Perpustakaan FT 11 Maret")
registL = Label(root, text="Daftar sebagai anggota dulu, Ya!\n")
registY = Button(root, text="Ya", padx=20, pady=10, command=lambda: daftar(root))
registN = Button(root, text="Tidak", padx=20, pady=10, command=lambda: not_daftar(root))
bannerA.grid(column=0, row=1, columnspan=2)
bannerB.grid(column=0, row=2, columnspan=2)
registL.grid(column=0, row=3, columnspan=2)
registY.grid(column=0, row=4)
registN.grid(column=1, row=4)


root.mainloop()