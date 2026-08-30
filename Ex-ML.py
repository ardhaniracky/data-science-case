import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "bulan" : list(range(1,13)),
    "penjualan": [100, 120, 125, 140, 150, 165, 170, 185, 195, 210, 220, 235]
}

df = pd.DataFrame(data)

print(tabulate(df, headers="keys", tablefmt="rounded_grid", showindex=True))


# Membut Variabel yang menyimpan nilai bulan dan penjualan
x = df[["bulan"]]
y = df[["penjualan"]]

model = LinearRegression()

model.fit(x,y)

y_pred = model.predict(x)

print("\nPrediksi:")
print(y_pred)

mae = mean_absolute_error(y,y_pred)

print("\nMAE ", round(mae,2))

prediksi_bulan = pd.DataFrame({
    "bulan" : [13,14,15]
})

prediksi_3_bulan = model.predict(prediksi_bulan)

prediksi_bulan['prediksi_3_bulan'] = prediksi_3_bulan

print(tabulate(prediksi_bulan,headers="keys",showindex=True))