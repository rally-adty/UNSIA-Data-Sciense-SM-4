# main.py
import pandas as pd

# Data sederhana
data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [80, 90, 75]
}

df = pd.DataFrame(data)

# Tampilkan data
print("Data:")
print(df)

# Rata-rata
rata_rata = df["Nilai"].mean()
print("\nRata-rata nilai:", rata_rata)