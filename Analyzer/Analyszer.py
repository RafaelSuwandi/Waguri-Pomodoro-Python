import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# NOTE contoh visualisasi data matplot

# data1 = [1,3,5,7,9]
# data2 = [2,4,6,8,10]

# # plt.plot(data1,data2)
# plt.bar(data1,data2)
# plt.title("My first matplot design")
# plt.xlabel("TANGGAL")
# plt.ylabel("TOTAL MENIT")
# plt.show()

df = pd.read_csv("../TIMER/data_belajar.csv")

# Filter string "selesai" dari data 
df_sukses = df[df["Status"] == "Selesai"]

# Mencari values "Menit" lalu di masukkan kedalam series yang sama
progress = df_sukses.groupby("Tanggal")["Menit"].sum()
# print(progress)

jumlah = np.sum(progress.values) # Total menit
rata = np.mean(progress.values) # rata rata menit
# print(jumlah)
# print(rata)

# Menampilkan total fokus dan rata rata fokus per hari
# Menampilkan total fokus dan rata-rata fokus per hari di terminal
print("=================== STATISTIK WAGURI ===================")
print(f"Total Fokus: {jumlah} Menit | Rata-rata: {rata:.1f} Menit/Hari")
print("========================================================")

# Visual chart
plt.figure(figsize=(12,5))
plt.bar(progress.index , progress.values, color= "brown") # index adalah tanggal dan values adalah menit

plt.title("Waguri Pomodoro Tracker - Progres Belajar Harian")
plt.xlabel("Tanggal")
plt.ylabel("Durasi Fokus (Menit)")
plt.tight_layout()

plt.show()