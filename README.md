# techsmart-backend

## Add your files
```
cd existing_repo
git remote add origin https://gitlab.com/nabeelarrafi/techsmart-backend.git
git branch -M main
git push -uf origin main
```

## Getting started

Pastikan di perangkat kalian telah terinstall MySQL atau PostgreSQL untuk database nya, bisa pilih salah satu, gunakan (XAMPP) jika ingin menggunakan MySQL dan (pgAdmin 4) jika ingin menggunakan PostgreSQL.

## Environment Setup

- Buat python virtual environment **.venv** di root directory project, (**.venv** sudah ada di .gitignore)
    ```
    python -m venv .venv
    ```
    OR
    ```
    python3 -m venv .venv
    ```

- Jalankan virtual environment **.venv**
    ```
    .venv/bin/activate
    ```
    Untuk keluar dari virtual environment:
    ```
    deactivate
    ```

## Database Setup
- Paket yang perlu di install jika ingin menggunakan MySQL :
    ```
    pip install mysqlclient
    ```
    Paket yang perlu di install jika ingin menggunakan PostgreSQL :
    ```
    pip install psycopg2
    ```

- Jika ingin menggunakan PostgreSQL, ubah kodingan **settings.py** seperti dibawah ini :
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'database_name',
            'USER': 'user_name',
            'PASSWORD': 'password_user',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
    ```

- Jika ingin menggunakan MySQL, ubah kodingan **settings.py** seperti dibawah ini :
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'database_name',
            'USER': 'user_name',
            'PASSWORD': 'password_user',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }
    ```

- Setelah selesai setting kode seperti di atas jangan lupa jalankan migrasi sebelum running server nya dengan perintah :
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    OR
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```


## Run local server
```
python manage.py runserver
```
OR
```
python3 manage.py runserver
```

## Committing Your Changes
> Selalu gunakan commit message yang jelas. Dalam konteks OOP, awali dengan nama **model**, lalu **method**, lalu **nama_file**, lalu deskripsikan perubahan/penambahan yang dilakukan:
```
git commit -m "tours:tour_details@mengubah json response"
```