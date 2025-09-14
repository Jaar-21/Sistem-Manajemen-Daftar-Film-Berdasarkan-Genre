# Sistem-Manajemen-Daftar-Film-Berdasarkan-Genre
Program ini berguna untuk mengelola daftar film melalui menu utama Pengguna yang dapat melihat daftar film berdasarkan genre, menampilkan film-film terlaris, menambah film baru, serta menampilkan detail informasi setiap film.

<img width="1231" height="952" alt="Flowchart Ahmad Fajar" src="https://github.com/user-attachments/assets/84a615bd-e3e8-46a1-8b7a-1e18b03e7dcd" />

FLOWCHART


CODE
```python
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


 ```
<p> ==================================================================================== <p>
Kondisi jika Opsi 1 dipilih dan memasukkan pilihan yang sesuai <br/>
> 1. Pilih Opsi 1 <br/>
> 2. Masukkan Film yang ingin dilihat detail filmnya <br/>
> 3. Detail film muncul <br/>
    - Judul <br/>
    - Genre <br/>
    - Pembuat <br/>
    - Sinopsis <br/>
    - Tanggal rilis <br/>
    - Pemeran <br/>
> 4. kembali ke Menu <br/>

<img width="405\" height="400" alt="image" src="https://github.com/user-attachments/assets/4c814e8b-ae51-4f10-9dd5-341f57d66f24" />

<p> ==================================================================================== <p>
Kondisi jika Opsi 1 dipilih dan memasukkan pilihan yang tidak sesuai <br/>
> 1. pilih Opsi 1 <br/>
> 2. Memasukkan Film atau Kata yang salah <br/>
> 3. Sistem akan melihat bahwa anda salah menginput "Film tidak ditemukan!" <br/>

<img width="400" height="400" alt="Screenshot 2025-09-14 142013" src="https://github.com/user-attachments/assets/2fb902a3-8e56-4a7a-b999-03a30bc798aa" />

<p> ==================================================================================== <p>
Kondisi jika memilih Opsi 2 <br/>
> 1. Pilih Opsi 2 <br/>
> 2. Masukkan judul<br/>
> 3. Masukkan Genre<br/>
> 4. Masukkan Pembuat<br/>
> 5. Masukkan sinopsis<br/>
> 6. Masukkan Tanggal rilis<br/>
> 7. Masukkan pemeran<br/>
> 8. Jika sudah semua maka Film sudah ditambahkan dan sistem akan membaca nya"Film berhasil ditambahkan!" <br/>
> 9. Film bisa di lihat di Opsi 1 <br/>

<img width="400" height="400" alt="Screenshot 2025-09-14 143357" src="https://github.com/user-attachments/assets/0486805f-055c-4c8b-8147-29f7d332a2c7" />

<p> ==================================================================================== <p>
Kondisi jika memilih Opsi 3 dan memasukkan film yang sesuai <br/>
> 1. Pilih Opsi 3 <br/>
> 2. Masukkan judul_film yang sesuai<br/>
> 3. Sistem akan Melihat apakah film ada di dalam list jika sesuai Film akan dihapus <br/>
> 4. "Judul_Film berhasil dihapus!" <br/>
> 5. Film bisa dilihat di Opsi 1 apakah sudah dihapus oleh sistem <br/>

<img width="602" height="639" alt="Screenshot 2025-09-14 144024" src="https://github.com/user-attachments/assets/26831e97-d6ae-4a37-8369-8e422c33272a" />

<p> ==================================================================================== <p>
Kondisi jika memilih Opsi 3 dan memasukkan film yang tidak sesuai <br/>
> 2. Masukkan judul_film yang tidak sesuai atau Kata yang salah<br/>
> 3. Sistem akan Melihat apakah film ada di dalam list jika Film tidak ada dilist <br/>
> 4. "Film tidak ditemukan!" <br/>

<img width="625" height="445" alt="Screenshot 2025-09-14 144627" src="https://github.com/user-attachments/assets/2d951257-4491-4f51-a5d1-f65fe65976f1" />

<p> ==================================================================================== <p>
