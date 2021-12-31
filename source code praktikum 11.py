# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 20:31:55 2021

nama :sarah sakinah
nim:065002100033
prodi:sistem informasi
"""

namafile = input("Masukkan nama file: ") 

file = open(namafile, 'r')
data = file.readlines()
file.close()

updates = []
	
while True:
	print("""\n-------- M e n u --------
| 1. BACA Data
| 2. Mencari Nilai Rata-Rata Praktikum Mahasiswa/i
| 3. Update Nilai Praktikum Mahasiswa/i
| 4. Simpan Perubahan Nilai praktikum mahasiswa
| 5. Exit""")
	menu = int(input("Silahkan pilih menu: "))
	
	if menu == 1:
		print("\n[1. BACA DATA ]\n")
		for line in data:
			print(line.strip())
			
	elif menu == 2:
		print("\n[2. MENCARI NILAI RATA RATA PRAKTIKUM MAHASISWA/I ]\n")
		inputnama = input("Masukkan nama mahasiswa/i: ")
		for line in data:
			dataline = line.strip().split(' ')
			nilai1, nilai2, nilai3 = dataline[-3], dataline[-2], dataline[-1]
			nama = ' '.join(dataline[0:dataline.index(nilai1)])
			if inputnama == nama:
				rerata = (int(nilai1) + int(nilai2) + int(nilai3)) / 3
				print(f"Nilai: [{nilai1}, {nilai2}, {nilai3}]")
				print(f"Rerata nilai praktikum {inputnama}: {rerata}")
				
	elif menu == 3:
		print ("\n[3. UPDATE NILAI PRAKTIKUM MAHASISWA/I ]\n")
		inputnama = input("Masukkan nama mahasiswa/i: ")
		nilaiKe = int(input("Update nilai praktikum ke-: "))
		nilaiBaru = int(input("Masukkan nilai baru: "))
		for line in data:
			dataline = line.strip().split(' ')
			nilai1, nilai2, nilai3 = dataline[-3], dataline[-2], dataline[-1]
			nama = ' '.join(dataline[0:dataline.index(nilai1)])
			if inputnama == nama:
				tempdata = [nama, int(nilai1), int(nilai2), int(nilai3)]
				nilailama = tempdata[nilaiKe]
				tempdata[nilaiKe] = nilaiBaru
				data[data.index(line)] = f"{nama} {tempdata[1]} {tempdata[2]} {tempdata[3]}\n"
				print(f"Berhasil update nilai {nilailama} >> {nilaiBaru}")
				updates.append(f"[{nama}] Update nilai prak {nilaiKe} | {nilailama} >> {nilaiBaru}")
				
	elif menu == 4:
		print("\n[4. SIMPAN PERUBAHAN NILAI MAHASISWA ]")
		file = open(namafile, 'w')
		file.write(''.join(data))
		file.close()
		for x in updates:
			print(x)
		print("\nPerubahan berhasil disimpan.")
		updates = []
		
	elif menu == 5:
		if len(updates) > 0:
			print("\n-------- I n f o --------\n| 1. Kembali\n| 2. Tetap Keluar")
			menu2 = int(input("Terdapat update nilai yang belum tersimpan ke file, tetap keluar?: "))
			if menu2 == 1:
				continue
			elif menu2 == 2:
				print("\n[5. EXIT ]")
				print("Thankyou")
				break
		else:
			print("\n[5. EXIT ]")
			print("Thankyou")
			break