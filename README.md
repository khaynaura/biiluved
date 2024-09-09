# biiLUVed: Tugas PBP Ganjil 2024/2025
**Nama: Khayla Naura Ulya Luqyana**

**NPM: 2306275310**

**Kelas: PBP A**

Link to pws: http://khayla-naura-biiluved.pbp.cs.ui.ac.id/

## **TUGAS 2: Implementasi Model-View-Template (MVT) pada Django**

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**CHECKLIST 1: Membuat proyek django baru**
1. Menentukan ide e-commerce yang ingin dibuat dan menentukan poin-poin utama yang harus dimiliki oleh e-commerce tersebut. Di tugas ini, saya membuat e-commerce khusus untuk produk preloved atau thrift melihat kepopuleran jenis produk tersebut di kalangan masyarakat. 
2. Setelah menentukan nama e-commerce, saya memulai dengan membuat direktori utama bernama bii-lu-ved. Penamaan tersebut saya lakukan agar saya bisa membedakan direktori utama dan proyek django. Setelah itu, saya membuat dan mengaktifkan _virtual environment_.
3. Saya melanjutkannya dengan membuat requirements.txt yang berisi dependencies. Saya juga menginstall requirements.txt guna menginstall dependencies yang ada.
4. Saya membuat projek django baru bernama biiluved dengan menjalankan perintah `django-admin startproject biiluved .`
5. Setalah membuat projek django tersebut, saya menambahkan ALLOWED_HOST dalam settings.py yang berada dalam projek django dengan `ALLOWED_HOST = [“localhost”, “127.0.0.1”].`
6. Memastikan bahwa proyek berhasil dibuat dengan **menjalankan perintah python3 manage.py runserver. Setelah mengecek http://localhost:8000 dan berhasil, saya menjalankan `deactivate` untuk menonaktifkan virtual environment.
7. Selanjutnya, saya membuat repository di github dengan nama biiluved dan menghubungkannya dengan direktori utama. Untuk menjalankan hal tersebut, saya melakukan perintah `git init, git branch -M, dan git add remote origin https://github.com/khaynaura/biiluved.git`. 
8. Setelah itu, saya menambahkan .gitignore ke dalam direktori utama dan melakukan `git add, commit, dan push ke repository`. Berkas tersebut berguna agar git bisa mengabaikan berkas-berkas tertentu.
9. Karena awalnya ingin melakukan deployment ke PWS, saya membuat proyek baru di PWS. Setelah itu, saya menambahkan url PWS di ALLOWED_HOST hingga menjadi ALLOWED_HOST = [“localhost”, “127.0.0.1”, “khayla-naura-biiluved.pbp.cs.ui.ac.id”] 
10. Setelah itu, saya melakukan `git add, commit, dan push ke repository`. Setelah itu, saya menjalankan project command yang ada di PWS. Saya menyadari bahwa PWS tidak meminta username dan password project seperti biasanya dan saat saya cek di situs PWS, proyek tersebut gagal untuk di build. Setelah itu, saya mengecek discord PBP dan mengetahui bahwa error yang saya dapatkan berasal dari PWS dan permasalahan ini akan diabaikan untuk tugas 2 ini.

**CHECKLIST 2 & 3: Membuat aplikasi main dan melakukan routing pada proyek agar dapat menjalankan aplikasi**
1. Saya mengaktifkan kembali virtual environment sebelum membuat aplikasi. 
2. Untuk membuat aplikasi main, saya menjalankan perintah `django-admin startapp main`.
3. Setelah itu, saya menambahkan ‘main’ pada INSTALLED_APPS di settings.py yang berada dalam direktori proyek. 
4. Membuat direktori templates di dalam main yang berisi main.html. main.html tersebut berisi nama aplikasi, nama, dan kelas. Berikut isi dari main.html:
```
<h1> biiLUVed</h1>
<h4>from preloved to beloved, an item needs to be loved too </h4>

<h3>Name: </h3>
<p> Khayla Naura Ulya Luqyana </p>

<h3>Class: </h3>
<p> PBP A </p>
```
5. Setelah itu, saya membuka main.html dan memastikan bahwa hal yang terbuka sesuai dengan apa yang saya buat.

**CHECKLIST 4: Membuat model pada aplikasi main dengan nama Product yang memiliki atribut wajib _name, description,_ dan _price_**
1. Setelah saya menyesuaikan kebutuhan aplikasi, saya memodifikasi models.py yang berada pada direktori main menajadi:
   ```
   from django.db import models

   class Product(models.Model):
    category_choices = [
        ("clothing", "Clothing"),
        ("shoes", "Shoes"),
        ("bags", "Bags"),
        ("acc", "Accessories"),
        ("others", "Others")
    ]
    gender_choices = [
        ("women", "Women"),
        ("men", "Men"),
        ("unisex", "Unisex")
    ]


    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=15,choices=category_choices)
    # image = to be added later
    conditions = models.DecimalField
    brand = models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=gender_choices)

    # @property
    # to be added later
    ```
2. Setelah itu, saya menjalankan `python manage.py makemigrations` dan `puthon manage.py migrate`.
   
**CHECKLIST 5: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
1. Memodifikasi views.py yang ada di direktori main menjadi:
```
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'biiLUVed',
        'name': 'Khayla Naura Ulya Luqyana',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```
2. Modifikasi tersebut akan mengembalikan tampilan yang sesuai dengan context/data yang ada dalam fungsi tersebut. Karena fungsi tersebut akan meneruskan data ke main.html, maka saya juga akan memodifikasi main.html
3. Memodifikasi main.html dalam direktori templates menjadi:
```
<h1>{{app_name}}</h1>
<h4>from preloved to beloved, an item needs to be loved too </h4>

<h3>Name: </h3>
<p>{{name}}</p>

<h3>Class: </h3>
<p>{{class}}</p>
```
**CHECKLIST 6: Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
1. Saya mengatur _routing_ URL agar aplikasi main dapat diakses dengan menambahkan kode di urls.py di direktori main:
```
from django.urls import path
from .views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Setelah itu, saya menambahkan kode dalam urls.py yang berda di dalam direktori proyek biluved:
```
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
]
```
3. Untuk memastikan bahwa routing berhasil, saya menjalankan perintah `python manage.py runserver`
4. Saya mencoba membuka http://localhost:8000/ dan melihat bahwa sudah berhasil.
5. Setelah berhasil, saya melakukan ` git add, commit, dan push`
   
<img width="424" alt="Screenshot 2024-09-07 at 18 55 56" src="https://github.com/user-attachments/assets/dc0c43d1-5733-4972-93e2-e0bc32b4f302">


**CHECKLIST 7: Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
1. Sebelumnya, saya telah mencoba melakukan deployment ke PWS. Seharusnya, setelah ini saya bisa langsung menjalankan perintah `git push pws main:master`. Namun, PWS yang error membuat deployment tidak berhasil dan tugas 2 cukup hanya sampai dapat diakses dalam local host. Setelah mendapat informasi bahwa PWS dapat bekerja, saya menjalankan `git push pws main:master` dan status pws berubah menjadi running. Hal tersebut berarti bahwa PWS telah berhasil di deploy dan projek dapat dilihat melalui link yang tertera di awal.

### **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**

<img width="532" alt="Screenshot 2024-09-07 at 21 05 51" src="https://github.com/user-attachments/assets/64534267-8ba6-42c7-aed6-e6cba0661df2">

Penjelasan: Alur dimulai dari client yang melakuakn request melalui url yang telah didefinisikan pada `urls.py`. `urls.py` berguna untuk mendefinisikan url pattern dan juga akan menentukan view yang harus dipanggil untuk url pattern-nya. Setelah itu, django akan menerima request dan kan meneruskan ke `views.py` untuk memproses request yang ada. Lalu, views.py akan berinteraksi dengan `models.py`. Hal tersebut berguna untuk mendapatkan data pada model. Setelah mendapatkan data, `views.py` akan menggunakan template, yang mana jika di tugas ini ialah `main.html` untuk melakukan render tampilan html. Template tersebut akan menggunakan data dari `views.py`. Lalu, template html yang telah di render tersebut yang akan menjadi jawaban dari request atau response ke client. 

### **Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git merupakan sebuah alat yang digunakan untuk mengatur sumber code yang digunakan untuk pengembangan perangkat lunak. Git dapat melakukan tracking code, yaitu memberi tahu _history_ dari code yang ada, seperti perubahan yang pernah dilakukan dalam pengembangan perangkat lunak tersebut. Dengan adanya git, developer juga memiliki backup code. Hal tersebut tentunya memudahkan developer jika ingin melanjutkan pengemangan perangkat lunak di device lain. 

Selain itu, pengembangan perangkat lunak biasanya membutuhkan banyak developer. Git juga memudahkan para developer untuk bekerja sama dengan developer lain sehingga pengembangan perangkat lunak menjadi lebih efisien dan cepat. Hal tersebut dapat dilakukan dengan menggunakan _commands_ yang ada dalam git. 

### **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Django merupakan sebuah framework yang berbasis bahasa python. Python sendiri sudah dikenal sebagai bahasa yang mudah dipelajari untuk para pemula. Tak hanya itu, framework Django juga sudah menyiapkan fitur penting yang berguna untuk pengembangan perangkat lunak, seperti fitur authentication dan pengelolaan database. Hal tersebut tentunya sangat memudahkan orang yang baru belajar mengenai pengembangan perangkat lunak.

Tak hanya itu, Django juga mempunyai konsep Model-View-Template (MVT) yang dapat membantu pemula untuk mengerti konsep awal dalam pengembangan aplikasi. Selain itu, Django juga memiliki dokumentasi yang lengkap dan komunitas besar. Hal tersebut tentunya memberikan pemula sumber yang cukup luas untuk memahami Django secara lebih mendalam ataupun untuk mengatasi kesulitan yang dihadapi.

### **Mengapa model pada Django disebut sebagai ORM?**

Model Django ORM (_object-relational mapper)_ merupakan model yang memudahkan developer untuk berinteraksi dengan database apapun dengan menggunakan python. Dengan mengggunakan Django, developer tidak perlu menggunakan SQL untuk berinteraksi dengan database. Hal tersebut memudahkan developer dalam pengembangan backendnya.



