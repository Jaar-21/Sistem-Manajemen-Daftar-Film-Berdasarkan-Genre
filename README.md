# Sistem-Manajemen-Daftar-Film-Berdasarkan-Genre



```python
film_data = {
    "Action": [
        ("Avengers Endgame", "Marvel Studio", "Pertarungan melawan Thanos.", "2019-04-26", "Robert Downey Jr, Chris Evans"),
        ("John Wick", "Lionsgate", "Seorang mantan pembunuh bayaran membalas dendam.", "2014-10-24", "Keanu Reeves"),
    ],
    "Drama": [
        ("The Pursuit of Happyness", "Columbia Pictures", "Seorang ayah berjuang untuk masa depan anaknya.", "2006-12-15", "Will Smith, Jaden Smith"),
        ("Forrest Gump", "Paramount Pictures", "Kisah hidup Forrest yang penuh inspirasi.", "1994-07-06", "Tom Hanks"),
    ],
    "Comedy": [
        ("Mr. Bean's Holiday", "Universal Pictures", "Petualangan kocak Mr. Bean di Prancis.", "2007-03-30", "Rowan Atkinson"),
        ("Jumanji: Welcome to the Jungle", "Sony Pictures", "Empat remaja masuk ke dalam permainan video ajaib.", "2017-12-20", "Dwayne Johnson, Kevin Hart"),
    ]
}

tier_list = [
    ("Avengers Endgame", "Marvel Studio", "Pertarungan melawan Thanos.", "2019-04-26", "Robert Downey Jr, Chris Evans"),
    ("The Pursuit of Happyness", "Columbia Pictures", "Seorang ayah berjuang untuk masa depan anaknya.", "2006-12-15", "Will Smith, Jaden Smith"),
    ("Jumanji: Welcome to the Jungle", "Sony Pictures", "Empat remaja masuk ke dalam permainan video ajaib.", "2017-12-20", "Dwayne Johnson, Kevin Hart"),
]

while True:
    print("Pilih Menu:")
    print("1. Lihat Genre & Film")
    print("2. List Film Terlaris")
    print("3. Tambah Film")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("Daftar Genre:")
        for genre in film_data:
            print("-", genre)

        pilih_genre = input("Ketik genre yang dipilih: ")
        if pilih_genre in film_data:
            print(f"Film di genre {pilih_genre}:")
            for film in film_data[pilih_genre]:
                print("-", film[0])

            pilih_film = input("Ketik judul film yang dipilih: ")
            for film in film_data[pilih_genre]:
                if pilih_film == film[0]:
                    print("=== Detail Film ===")
                    print("Judul     :", film[0])
                    print("Pembuat   :", film[1])
                    print("Sinopsis  :", film[2])
                    print("Tgl Rilis :", film[3])
                    print("Pemeran   :", film[4])
                    print("===================")
                    break
            else:
                print("Film tidak ditemukan!")
        else:
            print("Genre tidak ditemukan!")

    elif pilihan == "2":
        print("=== List Film Terlaris ===")
        for film in tier_list:
            print("-", film[0])

        pilih_film = input("Ketik judul film yang dipilih: ")
        for film in tier_list:
            if pilih_film == film[0]:
                print("=== Detail Film ===")
                print("Judul     :", film[0])
                print("Pembuat   :", film[1])
                print("Sinopsis  :", film[2])
                print("Tgl Rilis :", film[3])
                print("Pemeran   :", film[4])
                print("===================")
                break
        else:
            print("Film tidak ditemukan!")

    elif pilihan == "3": 
        genre = input("Masukkan genre: ")
        judul = input("Masukkan judul: ")
        pembuat = input("Masukkan pembuat: ")
        sinopsis = input("Masukkan sinopsis: ")
        tgl_rilis = input("Masukkan tanggal rilis: ")
        pemeran = input("Masukkan pemeran: ")

        film_data[genre] = []
        film_data[genre].append((judul, pembuat, sinopsis, tgl_rilis, pemeran))
        print("Film berhasil ditambahkan!")

    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

 ```python
