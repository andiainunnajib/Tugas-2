nama_kontak = ['Farhan', 'Joko']
nomor_telp = ['08123456789',  '08987654321']




n = 1
while n != 3 :
    print("Selamat datang\n==============================\n")
    print ("1. Daftar Kontak.")
    print ("2. Tambah Kontak.")
    print ("3. Keluar.")

    n = int(input("Pilih menu : "))
    print('')
    

    if n == 1 :

        for i in range (len(nama_kontak)):
           
            print('Nama : {} ,\nNo.Telepon: {} \n'.format(nama_kontak[i], nomor_telp[i]))

    elif n == 2:
        masuk_nama = input ("Nama: ")
        nama_kontak.append(masuk_nama)
        masuk_nomor = input ("Nomor Telepon: ")
        nomor_telp.append(masuk_nomor)

        print("\nKontak Berhasil ditambahkan\n\n")

    elif n ==3:
        print("Program Selesai, Sampai Jumpa!")

    else:
        print("Menu tidak tersedia")
