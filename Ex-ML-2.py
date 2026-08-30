import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# =========================
# 1. DATA PENJUALAN
# =========================

data = {
    "Bulan": list(range(1, 13)),
    "Penjualan": [100, 120, 125, 140, 150, 165, 170, 185, 195, 210, 220, 235]
}

df = pd.DataFrame(data)

print(df)


# =========================
# 2. MENENTUKAN FITUR DAN TARGET
# =========================

X = df[["Bulan"]]
y = df["Penjualan"]


# =========================
# 3. MEMBUAT MODEL
# =========================

model = LinearRegression()


# =========================
# 4. TRAINING MODEL
# =========================

model.fit(X, y)


# =========================
# 5. PREDIKSI DATA HISTORIS
# =========================

y_pred = model.predict(X)

print("\nPrediksi:")
print(y_pred)


# =========================
# 6. EVALUASI MODEL
# =========================

mae = mean_absolute_error(y, y_pred)

print("\nMAE:", mae)


# =========================
# 7. FORECAST 3 BULAN KE DEPAN
# =========================

bulan_depan = pd.DataFrame({
    "Bulan": [13, 14, 15]
})

prediksi_3_bulan = model.predict(bulan_depan)

bulan_depan["Prediksi_Penjualan"] = prediksi_3_bulan

print("\nForecast 3 Bulan ke Depan:")
print(bulan_depan)


# =========================
# 8. VISUALISASI
# =========================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Bulan"],
    df["Penjualan"],
    label="Data Aktual"
)

plt.plot(
    df["Bulan"],
    y_pred,
    label="Garis Regresi"
)

plt.scatter(
    bulan_depan["Bulan"],
    bulan_depan["Prediksi_Penjualan"],
    label="Forecast"
)

plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.title("Forecasting Penjualan dengan Regresi Linier")

plt.legend()
plt.grid()

plt.show()