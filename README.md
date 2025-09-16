# PBP C 2025
```
Nama : Raida Khoyyara
NPM : 2406495445 
Kelas : PBP C
```

<details>
<summary>Tugas Individu 2</summary>

## TUGAS 2
Aplikasi dapat diakses di: https://raida-khoyyara-soccerest.pbp.cs.ui.ac.id/ 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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
Pertama, ketika user mengakses aplikasi lewat browser, request itu masuk ke urls.py di level project.
Di sini, Django ngecek dulu apakah URL yang diminta sesuai dengan pola yang sudah kita definisikan. Kalau tidak sesuai, Django langsung balikin Error 404 – Page Not Found.

Kalau sesuai, request diteruskan ke urls.py di level aplikasi. Dari sini, Django tahu view mana yang harus dijalankan.

Selanjutnya masuk ke views.py, yang berfungsi sebagai otak logika aplikasi. Kalau view ini butuh data, dia akan memanggil models.py, yang jadi jembatan ke database lewat ORM.

Database akan ngasih balik data ke models, lalu diteruskan lagi ke views.
Di views, data itu dibungkus dalam bentuk context dan dikirim ke templates (HTML).

Templates ini kemudian dirender jadi halaman HTML final, dan akhirnya dikembalikan lagi ke client, sehingga user bisa lihat hasilnya di browser.

Tambahan, ada juga settings.py yang sebenarnya nggak dilewati langsung oleh request, tapi penting karena ngatur konfigurasi seperti database, template, dan apps yang aktif.

## Jelaskan peran settings.py dalam proyek Django!
settings.py berfungsi sebagai pusat pengaturan proyek Django. Semua konfigurasi penting ada di situ, mulai dari daftar aplikasi yang dipakai (INSTALLED_APPS), pengaturan database, bahasa, zona waktu, sampai konfigurasi keamanan seperti ALLOWED_HOSTS. Dengan kata lain, settings.py mengatur bagaimana proyek Django berjalan dan berinteraksi dengan lingkungan sekitarnya.

## Bagaimana cara kerja migrasi database di Django?
Migrasi pada Django merupakan mekanisme untuk memastikan struktur database selalu sesuai dengan model yang didefinisikan di models.py. Prosesnya terdiri atas dua tahap:
makemigrations – Django membuat file migrasi yang berisi instruksi perubahan database berdasarkan model yang dibuat atau diubah.
migrate – Django menjalankan instruksi tersebut agar tabel dan kolom di database benar-benar diperbarui sesuai dengan definisi model.
Dengan demikian, migrasi menjaga konsistensi antara kode program dengan database yang digunakan.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai permulaan karena memiliki beberapa keunggulan:

Lengkap tapi tetap sederhana: Sudah banyak fitur bawaan, seperti autentikasi, admin panel, dan ORM. Jadi kita bisa fokus ke konsep inti pengembangan.

Struktur proyek yang jelas: Django menekankan keteraturan melalui struktur folder dan file yang konsisten, sehingga membantu untuk memahami alur kerja proyek.

Dokumentasi dan komunitas yang kuat: ada banyak referensi resmi dan bantuan dari komunitas kalau ketemu masalah.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya
Asisten dosen sudah sangat membantu dan memudahkan saya dalam memahami alur pembuatan proyek Django dari awal(Thank you so much esp Ka Marla). Saran saya, mungkin akan lebih membantu jika ditambahkan contoh kasus error yang umum terjadi saat praktik dan cara penanganannya.
</details>


## TUGAS INDIVIDU 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting karena platform itu kan isinya banyak komponen (frontend, backend, database, API, dll). Nah biar semuanya nyambung, kita butuh mekanisme buat nganterin data. Kalau nggak ada data delivery, nanti datanya bisa nyasar, lambat, atau malah nggak sinkron. Intinya data delivery itu kaya kurir, yang pastiin info dari satu sisi (misalnya dari database ke tampilan web/UI).

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Keduanya memiliki kelebihan dan kekurangan masing masing
XML: detail banget, bisa simpen data kompleks + atribut, tapi verbose/banyak syntaxnya, sulit dibaca, agak berat.
JSON: simpel, ringan, gampang dibaca, dan udah nyambung sama JavaScript.

Makanya sekarang JSON jauh lebih populer. Soalnya lebih efisien buat komunikasi antar sistem, parsing lebih cepat, dan semua bahasa modern udah dukung JSON. Kalau XML lebih cocok buat dokumen yang super kompleks, tapi di web/API, JSON lebih oke.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() itu buat ngecek input user udah sesuai aturan validasi apa belum. Kalau valid return True dan kita bisa akses datanya lewat cleaned_data. Kalau nggak return False dan error-nya bisa langsung ditampilin di form. Kenapa penting? Biar data yang masuk ke sistem tuh bener, nggak ada yang aneh-aneh (contoh: harga negatif, email kosong, atau input random untuk nyerang sistem).

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token itu sejenis keamanan. Jadi setiap kali kita bikin form (misalnya buat login atau nambah produk), kode itu ikut terkirim dan server akan ngecek apakah kodenya cocok sama yang sebelumnya diberikan. Kalau cocok, berarti request memang dari user. Kalau nggak cocok, server langsung nolak karena bisa aja itu dari pihak luar yang berbahaya.
Tanpa CSRF token, aplikasi bisa kena serangan Cross-Site Request Forgery (CSRF). Misalnya, kita lagi login di aplikasi bank, terus buka website lain yang diam-diam ngirim request transfer uang. Karena nggak ada CSRF token, server bank nggak bisa bedain mana request asli dan palsu, yang bisa aja bikin transaksi jalan tanpa sadar. Jadi, CSRF token adalah lapisan keamanan penting yang memastikan setiap request form benar-benar datang dari user, bukan dari penyerang.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama, saya memastikan bahwa struktur repository sudah sesuai.

2. Selanjutnya, saya menambahkan direktori templates pada direktori utama. Di dalamnya, saya membuat berkas baru bernama base.html dan mengisinya dengan kode berikut:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>

<body>
    {% block content %} {% endblock content %}
</body>
</html>
```

3. Setelah itu, saya menambahkan konfigurasi pada file settings.py di direktori soccerest agar Django dapat mengenali direktori templates:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
```

4. Kemudian, saya menambahkan atau mengubah beberapa baris kode pada main.html, views.py, dan urls.py yang berada di dalam direktori main.

5. Untuk membuat dan menampilkan data pada HTML, saya juga membuat berkas baru bernama forms.py di dalam direktori main.

6. Selanjutnya, saya menambahkan dua berkas HTML baru, yaitu create_product.html dan product_detail.html, untuk kebutuhan tampilan form dan detail produk.

7. Agar aplikasi dapat berjalan dengan baik di PWS, saya menambahkan konfigurasi CSRF_TRUSTED_ORIGINS tepat setelah ALLOWED_HOSTS pada settings.py:
```
CSRF_TRUSTED_ORIGINS = [
    "<url-deployment-pws-kamu>"
]
```

8. Dan saya melakukan pengecekan secara lokal dengan menjalankan perintah:
```
python manage.py runserver 
```

9. Setelah bikin tampilan dasar dan form, sekarang saya tambahin fitur untuk menampilkan data dalam format XML.
Pertama, saya buka views.py di direktori main lalu import dulu:
```
from django.http import HttpResponse
from django.core import serializers
```

10. Lalu saya bikin fungsi baru show_xml dan show_json untuk ambil semua data dari model News.

11. Setelah  bikin fungsi saya selalu buka urls.py untuk nambahin path 

12. Saya cek data pake postman juga. pertama run server dulu dengan masukin url ini :
```
http://localhost:8000/xml/ → semua data XML

http://localhost:8000/json/ → semua data JSON

http://localhost:8000/xml/[id]/ atau http://localhost:8000/json/[id]/ → data per ID
```

13. Terakhir saya push kode ini ke git dan pws 

14. Pada hari selasa(16/09) Saya menambahkan validasi bahwa input price tidak boleh negatif dengan menambahkan kode: 
```
<script>
  const priceInput = document.getElementById('id_price');

  if (priceInput) {
    priceInput.addEventListener('input', function() {
      if (this.value < 0) {
        this.setCustomValidity('Harga produk tidak boleh negatif.');
      } else {
        this.setCustomValidity('');
      }
    });
  }
</script>
```
kode ini berfungsi untuk menampilkan pesan validasi error bahwa price tidak boleh negatif. Lalu push lagi ke pws


### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

1. JSON (Semua Data)
http://127.0.0.1:8000/xml → endpoint yang balikin data dalam format XML.
![JSON ALL](JSON.png)
2. XML (Semua Data)
http://127.0.0.1:8000/json → endpoint yang balikin data dalam format JSON.
![XML ALL](XML.png)
3. JSON (Detail by UUID)
http://127.0.0.1:8000/json/ddceace3-ab84-4f28-aae0-ad6b5aef72b6 → ambil data detail tertentu (misalnya satu produk/objek) dalam JSON berdasarkan UUID.
![JSON Detail](JSONDetails.png)
4. XML (Detail by UUID) 
http://127.0.0.1:8000/xml/ddceace3-ab84-4f28-aae0-ad6b5aef72b6 → sama kayak nomor 3 tapi formatnya XML.
![XML Detail](XMLDetails.png)