# biiLUVed: Tugas PBP Ganjil 2024/2025
**Nama: Khayla Naura Ulya Luqyana**

**NPM: 2306275310**

**Kelas: PBP A**

Link to pws: http://khayla-naura-biiluved.pbp.cs.ui.ac.id/

## **TUGAS 4: Implementasi Form dan Data Delivery pada Django**

### **Apa perbedaan antara HttpResponseRedirect() dan redirect()**
Secara garis besar `HttpsResponseRedirect()` dan `redirect()` tidak memiliki perbedaan yang signifikan karena kedua hal tersebut sama-sama berguna untuk mengarahkan user ke sebuah url. Akan tetapi,  `HttpsResponseRedirect()` hanya bisa menerima parameter dengan sebuah `url`. Di lain sisi,  `redirect()` bisa menerima parameter berupa `model`, `view`, dan `url`. Pada akhirnya,  `redirect()` juga akan menuju ke `HttpsResponseRedirect()`.  

### **Jelaskan cara kerja penghubungan model Product dengan User!**

Cara kerja hubungan antara model Product dan user dilakuakn dengan melakukan import modul `from django.contrib.auth.modesl import User` di file model Product. Setelah itu, kita bisa menggunakan ForeignKey dengan `user = models.ForeignKey(User, on_delete=models.CASCADE)`. Hal tersebut berguna untuk mengasosiasikan satu user dengan satu model product. 

Setelah hal tersebut dilakukan, kita bisa melakukan modifikasi pada views.py khususnya pada function pembuatan product. Perubahan yang dilakukan ialah dengan melalukan assign user menjadi `request.user`. Hal tersebut berguna agar product tersebut tersimpan di user tersebut. Setelah itu, untuk menampilkan product yang dimiliki oleh user tersebut, kita bisa melakukan sort  `Product.objects.filter(user=request.user)`. 

### **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Django memiliki sebuah authentication system yang secara langsung telah menghandle authentication dan authorization. Auth system tersebut terdiri atas users, permissions (penandaan apakah user dapat melakukan tugas tertentu atau tidak), groups, konfigurasi passowords, form dan views untuk loggin, dan backend system. Auth system tersebut berada dalam module bernama `django-contrib-auth`. Secara langsung, Django telah memberikan konfigurasi untuk penggunaan modul tersebut pada `settings.py` yang tergenerate saat kita membuat proyek django.

### **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**


### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**


## **TUGAS 3: Implementasi Form dan Data Delivery pada Django**

### **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery dibutuhkan dalam implementasi sebuah platform karena bagian inilah yang memastikan bahwa data yang dikirim dan diterima ke pengguna maupun server sudah akurat. Tak hanya itu, data delivery yang efektif dapt membantu platform dalam mebuat keputusan yang berdasarkan dengan adanya data yang selalu terupdate dan sesuai dengan kebutuhan pengguna. Data delivery juga sangat dibutuhkan karena memberikan responsivitas yang cepat serta menjaga keamanan data. Maka dari itu, data delivery sangatlah dibutuhkan untuk mendukung fungsi dan performa platform.

### **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya, baik JSON dan XML memiliki kelebihannya masing-masing. Sebagai contoh, XML sendiri memiliki struktur data yang lebih kompleks karena XML memberikan pengorganisasisan data yang hierarkis. Namun karena hal tersebut, XML memiliki kompleksitas yang lebih rumit. Di lain sisi, JSON memiliki struktur yang lebih sederhana dan lebih mudah untuk digunakan oleh para pemula. Maka dari itu, saya merasa bahwa JSON lebih baik dibandingkan dengan XML.

Kepopuleran JSON sendiri diakrenakan JSON memiliki kompatibilitas dengan JavaScript, bahasa yang sangat sering digunakan untuk pengembangan web. Selain itu, JSON cenderung lebih ringan dan sering dipakai dalam penggunaan API. API sendiri sangat penting untuk dalam pengembangan aplikasi khususnnya dalam transformasi data.

### **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

Fungsi dari method `is_valid` ialah untuk memvalidasi data yang dikirim oleh pengguna. Fungsi tersebut akan menjalankan validasi data yang diisi. Validasi yang dijalankan akan menyesuaikan dengan format yang telah ditetapkan oleh developer. Sebagai contoh, dalam biiLUVed, bagian price berupa integer field, method ini akan memastikan bahwa input pengguna benar berupa integer. Method `is_valid` akan mengembalikan `return` berupa boolean, yang akan mengembalikan nilai `True` jika semuanya telah memenuhi kriterai dan akan mengembalikan nilai `False` jika tidak ada yang sesuai dan biasanya akan menampilkan error yang ada. 

### **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

Kita membutuhkan `csrf_token` dikarenakan token itulah yang memberikan verifikasi bahwa setiap form yang masuk ke server memang diisi oleh user yang terautentikasi dan bukan dari sumber yang berbahaya. Jika kita tidak menambahkan `csrf_token`, maka aplikasi yang kita buat dapat menjadi rentan terhadap attacker dan serangan-serangan lain yang bisa mengrahkan pengguna untuk melakukan hal-hal yang tidak diinginkan. Sebagai contoh, serangan-serangan yang dapat dimanfaatkan oleh penyerang seperti memberikan informasi penting, seperti kata sandi dari pengguna serta permintaan lain yang mengarahkan ke situs-situs berbahaya.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**CHEKLIST 1: Membuat input form untuk menambahkan objek model pada app sebelumnya.**
1. Sebelum saya memulai untuk membuat program, saya mengaktifkan _virtual environment_ terlebih dahulu. Setelah itu, saya melanjutkan dengan membuat `base.html` di dalam direktori baru bernama `templates` yang berada di root direktori. Agar `base.html` dapat digunakan, saya menambahkan `'DIRS': [BASE_DIR / 'templates'],` pada settings.py yang berada dalam direktori proyek django.
2. Setelah itu, saya memodifikasi models.py untuk menambahkan import uuid yang digunakan agar setiap produk nantinya memiliki id yang unik yang sudah digenerate secara otomatis. Tak lupa, saya melakukan makemigrations dan migrate.
3. Selanjutnya, saya menambahkan  `forms.py` dalam main untuk membuat struktur form yang nantinya akan menjadi modal utama untuk mengantarkan data ke template yang ada. Berikut isi dari forms.py:
```
from django.forms import ModelForm
from main.models import Product

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "conditions", "category", "brand", "gender"]
```
4. Setelah itu, saya menambahkan import `redirect` dalam `views.py` dan menambahkan fungsi bernama `create_product_form` yang digunakan untuk membuat/mengarahkan ke page untuk membuat form mengisi produk.  Fungsi inilah yang digunakan agar dapat menambahkan produk baru secara otomatis ketika men-submit data di form. Tak hanya itu, saya juga memodifikasi fungsi `show_main` sehingga nantinya dapat mendapatkan data dari product yang telah diisi melalui form.
5. Setelah memeperbarui `views.py`, saya melakukan import fungsi tersebut ke `urls.py` dan menambahkannya ke `urlpatterns` 
6. Saya juga memodifikasi `main.html` sehingga nanti bisa menampilkan produk-produk yang telah diisi dalam bentuk tabel. Lalu, saya juga menambahkan button untuk mengarahkan ke page pengisian produk baru.
7. Setelah itu, saya menambahkan `create_product_form.html` yang nantinya menjadi tampilan untuk menambahkan produk baru.

**CHEKLIST 2: Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
1. Saya melakukannya dengan memodifiaksi `views.py` dengan melakukan import `HttpResponse` dan `serializers`. Setelah itu, saya menambahkan empat fungso baru, yaitu `show_xml`,  `show_json`, `show_xml_by_id`, `show_json_by_id`. Berikut isi dari masing-masing fungsi:
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Keempat fungsi tersebut memiliki variabel data yang nantinya digunakan untuk menyimpan hasil query. Untuk fungsi show_xml_by_id dan show_json_by_id menggunakan .filter(pk=id) untuk menyesuaikan dengan id yang ada. Keempat fungsi tersebut akan mengembalikan hasil query yang sesuai dengan format data.

**CHEKLIST 3: Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
1. Setelah menambahkan keempat fungsi ke `views.py`, saya melanjutkan dengan memodifikasi `urls.py`. Saya melanjutkannya dengan mengimpor fungs-fungsi tersebut.
2. Setelah itu, saya melakuakn routing URL dengan menambahkan path pada urlpatterns. Berikut isi dari `urls.py`:
```
from django.urls import path
from .views import show_main, create_product_form, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-form', create_product_form, name='create_product_form'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

### **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md**
#### **AKSES URL HTML**
<img width="1512" alt="Screenshot 2024-09-15 at 19 21 42" src="https://github.com/user-attachments/assets/72fd22ef-9601-415a-b7d3-52e325226852">

#### **AKSES URL XML**
<img width="1509" alt="Screenshot 2024-09-15 at 19 22 04" src="https://github.com/user-attachments/assets/7485b448-1a84-4df0-9a30-90d4d2254d21">

#### **AKSES URL JSON**
<img width="1512" alt="Screenshot 2024-09-15 at 19 22 11" src="https://github.com/user-attachments/assets/9d81352f-6e48-47d5-82d6-74e209a676d4">

#### **AKSES URL XML BY ID**
<img width="1512" alt="Screenshot 2024-09-15 at 19 22 53" src="https://github.com/user-attachments/assets/e76a611a-d922-4534-8114-666ab5b9491b">

#### **AKSES URL JSON BY ID**
<img width="1512" alt="Screenshot 2024-09-15 at 19 23 15" src="https://github.com/user-attachments/assets/6145b91b-62a7-405a-80bf-699e33253134">

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



