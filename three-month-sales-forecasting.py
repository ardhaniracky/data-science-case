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