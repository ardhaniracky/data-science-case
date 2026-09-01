# forecasting adalah sebuah metode yang untuk memprediksi nilai atau tren dimasa depan berdasarkan historis.
# file ini digunakan untuk melakukan forecasting penjualan selama tiga bulan kedepan menggunakan regresi linier

import pandas as pd
import matplotlib.pyplot as plt

# scikit-learn adalah sebuah library python yang digunakan untuk machine learning dan analisis data.
# library ini menyediakan berbagai algoritma dan tools untuk melakukan regresi, klarifikasi, clustering, dan evaluasi model.

# Regresi linier adalah sebuah metode statisik yang digunakan untuk memodelkan hubungan antara variabel independen (fitur).
# dan variabel dependen (target) dengan menggunakan garis lurus.

# inti dri regresi linier adalah meneumukan garis terbaik yang dapat memprediksi nilai target n=berdasarkan nilai fitur.

# memanggil library LineraRegression dri scikit learn untuk membuat model regresi linier dan mean_absolute_error
# utk mengevaluasi performa model.
from sklearn.linear_model import LinearRegression

# mean_absolute_error adalah sebuah metrik evaluasi yang digunakan untuk mengukur seberapa akurat prediksi model
# dibandingkan dengan nilai aktual.
from sklearn.metrics import mean_absolute_error

# =========================
# 1. DATA PENJUALAN
# =========================

data = {

    'bulan': [
        '2025-01-01',
        '2025-02-01',
        '2025-03-01',
        '2025-04-01',
        '2025-05-01',
        '2025-06-01',
        '2025-07-01',
        '2025-08-01',
        '2025-09-01',
        '2025-10-01',
        '2025-11-01',
        '2025-12-01'
    ],
    
    'penjualan': [
        120,
        128,
        135,
        142,
        150,
        157,
        165,
        172,
        180,
        188,
        195,
        205
    ]
}

df = pd.DataFrame(data)

# Mengubah kolom bulan menjadi tipe datetime
df['bulan'] = pd.to_datetime(df['bulan'])

# Membuat nomor periode
df['periode'] = range(1, len(df) + 1)

print('Data Penjualan')
print(df)

# =========================
# 2. MEMERIKSA DATA
# =========================

print("\nJUMLAH DATA KOSONG")
print(df.isnull().sum())

print("|INFORMASI PENJUALAN")
print("Penjualan rendah :", df["penjualan"].max())
print("Penjualan tinggi:", df["penjualan"].min())
print("Rata-rata :", round(df["penjualan"].mean()))

# =========================
# 3. MEMBAGI DATA TRAINING 
# =========================

# 9 bulan pertama untuk training
data_training = df.iloc[:9]

# 3 bulan terakhir unutk testing
data_testing = df.iloc[9:]

x_training = data_training[['periode']]
y_training = data_training[['penjualan']]

x_testing = data_testing[['periode']]
y_testing = data_testing[['penjualan']]

# =========================
# 4. MEMBUAT MODEL LINEAR REGRESSION
# =========================

model = LinearRegression()

model.fit(x_training,y_training)

# =========================
# 5. PREDIKSI DATA TESTING
# =========================

prediksi_testing = model.predict(x_testing)

hasil_testing = data_testing.copy()
hasil_testing['prediksi'] = prediksi_testing.round(2)
hasil_testing['selisih'] = (
    hasil_testing['penjualan'] - hasil_testing['prediksi']
).abs().round(2)

print('\nHasil Testing')
print(
    hasil_testing[
        ['bulan','penjualan','prediksi','selisih']
    ].to_string(index=False)
)