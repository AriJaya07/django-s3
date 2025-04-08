Berikut adalah contoh README.md untuk proyek Django + AWS S3, lengkap dan profesional sesuai standar GitHub. Ini mencakup deskripsi proyek, cara instalasi, konfigurasi S3, contoh penggunaan, dan struktur folder termasuk template HTML & CSS dan zebra config.

# 🖼️ Django + AWS S3 Image Upload

Proyek ini adalah contoh implementasi **upload gambar menggunakan Django** dan menyimpannya langsung ke **Amazon S3** menggunakan `django-storages` dan `boto3`. Cocok untuk digunakan dalam aplikasi produksi yang memerlukan **penyimpanan file skala besar**, seperti galeri, e-commerce, atau file manager.

---

## 🚀 Fitur

- Upload gambar langsung ke Amazon S3
- Konfigurasi dengan `django-storages` + `boto3`
- Template HTML sederhana untuk form upload
- Dukungan styling dasar dengan CSS
- Konfigurasi aman menggunakan environment variables
- Zebra settings pattern untuk file `settings.py`

---

## 🧱 Tech Stack

- Python 3.x
- Django 4.x
- AWS S3 (Amazon Web Services)
- `boto3` & `django-storages`
- HTML + CSS (minimal template)

---

## 📁 Struktur Proyek

django-s3-upload/ │ ├── core/ # App utama │ ├── templates/ │ │ └── upload_form.html │ ├── static/ │ │ └── css/style.css │ ├── models.py │ ├── views.py │ └── urls.py │ ├── media/ # Disarankan kosong, file akan tersimpan di S3 ├── project_name/ │ ├── settings/ │ │ ├── base.py │ │ ├── dev.py │ │ └── prod.py │ └── ... ├── .env # Berisi AWS config & secret key ├── requirements.txt └── README.md


---

## ⚙️ Instalasi & Setup

### 1. Clone Repository

git clone https://github.com/username/django-s3-upload.git
cd django-s3-upload
2. Install Dependencies
pip install -r requirements.txt
requirements.txt

Django>=4.0
boto3
django-storages
python-dotenv
3. Buat File .env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=ap-southeast-1
DEBUG=True
SECRET_KEY=your-django-secret
Jangan lupa untuk menambahkan .env ke .gitignore
📦 Konfigurasi settings/base.py (Zebra Pattern)

import os
from dotenv import load_dotenv
load_dotenv()

INSTALLED_APPS += [
    'storages',
    'core',
]

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'ap-southeast-1')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
✍️ Model Upload (core/models.py)

from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
📤 View & URL (core/views.py & urls.py)

from django.shortcuts import render, redirect
from .models import Photo

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            Photo.objects.create(image=image)
            return redirect('upload')
    return render(request, 'upload_form.html')
core/urls.py

from django.urls import path
from .views import upload_image

urlpatterns = [
    path('', upload_image, name='upload'),
]
🧾 Template (core/templates/upload_form.html)

<!DOCTYPE html>
<html>
<head>
  <title>Upload Image to S3</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <div class="container">
    <h2>Upload Image</h2>
    <form method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      <input type="file" name="image" required>
      <button type="submit">Upload</button>
    </form>
  </div>
</body>
</html>
🎨 CSS Styling (core/static/css/style.css)

body {
  font-family: sans-serif;
  background: #f9f9f9;
  display: flex;
  justify-content: center;
  padding: 40px;
}
.container {
  background: #fff;
  padding: 20px 40px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
button {
  padding: 10px 20px;
  background-color: #0e76a8;
  border: none;
  color: white;
  cursor: pointer;
}
✅ Testing

Jalankan server lokal:
python manage.py runserver
Akses di browser: http://localhost:8000/
Upload gambar dan cek di AWS S3 Console
📌 Catatan Tambahan

Pastikan bucket S3 Anda sudah memiliki permission untuk public read access (atau atur sesuai kebutuhan).
Jangan commit file .env ke repo publik.
Untuk lingkungan produksi, gunakan HTTPS dan domain khusus (CDN optional).
📮 License

MIT License © 2025 Your Name

💬 Feedback & Kontribusi

Feel free to fork, raise an issue, or submit a pull request. Let's build better tools together!


Kalau kamu kasih nama proyek dan akun GitHub kamu, aku bisa bantu sesuaikan branding-nya juga. Mau aku buatin juga file `.gitignore` dan `zebra config` lengkap?
