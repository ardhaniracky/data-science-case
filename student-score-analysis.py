import numpy as np
import pandas as pd
import mysql.connector
from tabulate import tabulate
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="rumah_it"
)

# maksud dri dictionary=True adalah agar hasil query yang dikembalikan berupa dictionary,
# sehingga kita bisa mengakses kolom-kolomnya dengan nama kolom, bukan dengan indeks.
# hal ini memudahkan dalam pengolahan data dan membuat kode lebih mudah dibaca.
cursor = connection.cursor(dictionary=True)

query = """
    SELECT
    students.student_id,
    students.student_name,
    students.class_name,
    programming_scores.assessment_name,
    programming_scores.score
FROM students
INNER JOIN programming_scores
    ON students.student_id = programming_scores.student_id
ORDER BY 
    students.student_id ASC,
    programming_scores.score_id ASC
    ;
"""

# eksekusi query
cursor.execute(query)

# ambil semua hasil query
results = cursor.fetchall()

# menutup cursor dan koneksi ke database
cursor.close()
connection.close()

# memeriksa ketersedian data
if not results:
    # digunakan untuk mengecek apakah ada hasil / tidak
    print("Data nilai santri belum tersedia.")
    # raise SystemExit digunakan untuk menghentikan eksekusi program jika tidak ada data yang ditemukan.
    raise SystemExit

# mengubah data Mysql menjadi DataFrame Pandas
df = pd.DataFrame(results)

# mengubah tipe data kolom score menjadi numerik(float) agar bisa dilakukan analisis statisik dan visualisasi.
df['score'] = df["score"].astype(float)

# menampilkan data dalam bentuk tabel menggunakan tabulate agar lebih mudah dibaca
print(tabulate(df, headers='keys', tablefmt='rounded_grid', showindex=True))