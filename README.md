# TUGAS 2

Nama : Raida Khoyyara
NPM : 2406495445 
Kelas : PBP C

Aplikasi dapat diakses di: https://raida-khoyyara-soccerest.pbp.cs.ui.ac.id/ 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat folder proyek dan inisialisasi Git
Pertama saya membuat folder dulu untuk proyek ini dan langsung  diinisialisasi ke Git.
```
mkdir soccerest
cd soccerest
git init
```

2. Membuat dan mengaktifkan Virtual Environment
Supaya package-package nggak bentrok sama proyek lain, saya membuat virtual environment lalu diaktifin.
```
python -m venv env
env\Scripts\activate
```

3. Menginstal dependencies dan membuat proyek Django
Saya menginstall dulu semua kebutuhan dari requirements.txt, terus bikin proyek Django baru dengan nama soccerest.
```
pip install -r requirements.txt
django-admin startproject soccerest .
```

4. Membuat aplikasi main
Setelah itu saya membuat aplikasi baru namanya main, lalu ditambahin ke INSTALLED_APPS di settings.py.
```
python manage.py startapp main
```

5. Membuat model Product
Di file models.py aplikasi main, saya membuat model Product dengan atribut:
name (CharField)
price (IntegerField)
description (TextField)
thumbnail (URLField)
category (CharField)
is_featured (BooleanField)

6. Migrasi database
Supaya modelnya tersimpan ke database, saya menajlankan perintah ini:
```
python manage.py makemigrations
python manage.py migrate
```

7. Mengedit views.py dan routing di urls.py
Sya membuat fungsi di views.py buat nampilin nama aplikasi plus nama, NPM, dan kelas. Terus routing di urls.py biar bisa diakses lewat browser.

8. Testing secara lokal
Saya test dulu secara lokal untuk memastikan aplikasi bisa berjalan dengan benar.
```
python manage.py runserver
```
Kemudian saya membuka http://127.0.0.1:8000/ untuk mengecek apakah main.html sudah tampil.

9. Deployment ke PWS
Terakhir, Saya melakukan deployment ke PWS. Sebelum itu, saya menambahkan domain PWS ke ALLOWED_HOSTS pada settings.py. Setelah itu, proyeknya dipush ke repository GitHub yang terhubung dengan PWS agar aplikasi bisa diakses secara online.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
link bagan: https://drive.google.com/file/d/1k8htoqWfiT6n4lfWice-SIryXT5wU8v3/view?usp=sharing 

## Jelaskan peran settings.py dalam proyek Django!
settings.py berfungsi sebagai pusat pengaturan proyek Django. Semua konfigurasi penting ada di situ, mulai dari daftar aplikasi yang dipakai (INSTALLED_APPS), pengaturan database, bahasa, zona waktu, sampai konfigurasi keamanan seperti ALLOWED_HOSTS. Dengan kata lain, settings.py mengatur bagaimana proyek Django berjalan dan berinteraksi dengan lingkungan sekitarnya.

## Bagaimana cara kerja migrasi database di Django?
Migrasi pada Django merupakan mekanisme untuk memastikan struktur database selalu sesuai dengan model yang didefinisikan di models.py. Prosesnya terdiri atas dua tahap:
makemigrations – Django membuat file migrasi yang berisi instruksi perubahan database berdasarkan model yang dibuat atau diubah.
migrate – Django menjalankan instruksi tersebut agar tabel dan kolom di database benar-benar diperbarui sesuai dengan definisi model.
Dengan demikian, migrasi menjaga konsistensi antara kode program dengan database yang digunakan.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai permulaan karena memiliki beberapa keunggulan:

Lengkap tapi tetap sederhana: Django menyediakan banyak fitur bawaan, seperti autentikasi, admin panel, dan ORM, sehingga memudahkan untuk fokus memahami konsep inti pengembangan perangkat lunak.

Struktur proyek yang jelas: Django menekankan keteraturan melalui struktur folder dan file yang konsisten, sehingga membantu untuk memahami alur kerja proyek.

Dokumentasi dan komunitas yang kuat: Dukungan dokumentasi resmi serta komunitas yang luas membuat proses belajar lebih mudah.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya
Asisten dosen sudah sangat membantu dan memudahkan saya dalam memahami alur pembuatan proyek Django dari awal(Thank you so much esp Ka Marla). Saran saya, mungkin akan lebih membantu jika ditambahkan contoh kasus error yang umum terjadi saat praktik dan cara penanganannya.