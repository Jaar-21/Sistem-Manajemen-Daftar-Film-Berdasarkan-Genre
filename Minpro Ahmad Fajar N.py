film_list = [
    ("Avengers Endgame", "Action", "Marvel Studio", "Pertarungan melawan Thanos.", "2019-04-26", "Robert Downey Jr, Chris Evans"),
    ("John Wick", "Action", "Lionsgate", "Seorang mantan pembunuh bayaran membalas dendam.", "2014-10-24", "Keanu Reeves"),
    ("The Pursuit of Happyness", "Drama", "Columbia Pictures", "Seorang ayah berjuang untuk masa depan anaknya.", "2006-12-15", "Will Smith, Jaden Smith"),
    ("Forrest Gump", "Drama", "Paramount Pictures", "Kisah hidup Forrest yang penuh inspirasi.", "1994-07-06", "Tom Hanks"),
    ("Mr. Bean's Holiday", "Comedy", "Universal Pictures", "Petualangan kocak Mr. Bean di Prancis.", "2007-03-30", "Rowan Atkinson"),
    ("Jumanji: Welcome to the Jungle", "Comedy", "Sony Pictures", "Empat remaja masuk ke dalam permainan video ajaib.", "2017-12-20", "Dwayne Johnson, Kevin Hart")
]

while True:
    print("Menu:")
    print("1. Lihat Film")
    print("2. Tambah Film")
    print("3. Hapus Film")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("Daftar Film:")
        for film in film_list:
            print(">" ,film[0])

        pilih_film = input("Ketik judul film:")
        if pilih_film:
            for film in film_list:
                if film[0] == pilih_film:
                    print("=== Detail Film ===")
                    print("Judul     :", film[0])
                    print("Genre     :", film[1])
                    print("Pembuat   :", film[2])
                    print("Sinopsis  :", film[3])
                    print("Tgl Rilis :", film[4])
                    print("Pemeran   :", film[5])
                    print("===================")
                    break
            else:
                print("Film tidak ditemukan!")

    elif pilihan == "2":
        judul = input("Masukkan judul: ")
        genre = input("Masukkan genre: ")
        pembuat = input("Masukkan pembuat: ")
        sinopsis = input("Masukkan sinopsis: ")
        tgl_rilis = input("Masukkan tanggal rilis: ")
        pemeran = input("Masukkan pemeran: ")

        film_list.append((judul, genre, pembuat, sinopsis, tgl_rilis, pemeran))
        print("Film berhasil ditambahkan!")

    elif pilihan == "3":
        for film in film_list:
            print(">",film[0])
        judul_hapus = input("Masukkan judul film yang ingin dihapus: ")
        for film in film_list:
            if film[0] == judul_hapus:
                film_list.remove(film)
                print(judul_hapus ,"berhasil dihapus!")
                break
        else:
            print("Film tidak ditemukan!")

    elif pilihan == "4":
        print("Selesai")
        break

    else:
        print("Pilihan tidak valid!")
