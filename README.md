# 🌍 Explorasi Dataset Gempa Bumi Indonesia

---

## 📌 Deskripsi Dataset

Dataset ini merupakan gabungan dari dua sumber utama:

- 🔍 **USGS (United States Geological Survey)** — data diperoleh melalui scraping manual.
- 📦 **Kaggle**: [Earthquakes in Indonesia](https://www.kaggle.com/datasets/kekavigi/earthquakes-in-indonesia/data)

📁 _Script scraping data USGS tersedia di:_ `script/USGS_ID.py`

Dataset ini mencakup informasi:

- ⏰ Waktu kejadian
- 📍 Lokasi geografis
- 📏 Magnitudo
- 🕳️ Kedalaman
- 🧭 Deskripsi lokasi kejadian gempa di Indonesia

## 🛠️ Struktur Folder

📂 **Struktur direktori proyek ini adalah sebagai berikut:**

```
📦 Projek_Visdat
 ┣ 📂 collectiondata/                      # Berisi kumpulan dataset gempa bumi dari berbagai sumber
 ┃  ┣ 📜 combined_earthquakes_ID.csv
 ┃  ┣ 📜 combined_earthquakes_raw.csv
 ┃  ┣ 📜 kaggle_earthquakes_ID.csv
 ┃  ┗ 📜 usgs_earthquake_data_ID.csv
 ┣ 📂 script/                              # Berisi script Python untuk pemrosesan data atau analisis
 ┃  ┗ 📜 USGS_ID.py
 ┣ 📜 .gitignore                           # File konfigurasi untuk mengabaikan file/folder tertentu oleh Git
 ┣ 📜 earthquakesID.ipynb                  # Notebook eksplorasi atau analisis gempa bumi di Indonesia
 ┣ 📜 main.ipynb                           # Notebook utama (diabaikan dalam version control)
 ┗ 📜 README.md                            # File ini (panduan proyek)
```

---

## 🎯 Tujuan Preprocessing

Preprocessing ini **tidak hanya untuk mengatasi missing value**, tapi lebih difokuskan untuk:

> ✅ **Merapikan struktur data** agar siap digunakan dalam **visualisasi interaktif berbasis web**.

---

## 🔄 Langkah-Langkah Preprocessing

1. **Gabungkan Data dari USGS dan Kaggle**

   - Seragamkan nama kolom
   - Tambahkan kolom `source` sebagai penanda asal data

2. **Simpan Dataset Gabungan (Raw)**

   - 📄 Output: `combined_earthquakes_raw.csv`

3. **Bersihkan Kolom Lokasi (`place`)**

   - Hapus noise seperti arah/arah mata angin (`"62 km W of..."`)
   - Hapus `"Indonesia"` jika berada di akhir string

4. **Kategorisasi Lokasi Berdasarkan Region**

   - Contoh: `Sumatra`, `Java`, `Papua`, dll

5. **Kategorisasi Magnitudo Gempa (`magnitude_category`)**

   - Contoh label: `Light`, `Moderate`, `Strong`

6. **Kategorisasi Kedalaman Gempa (`depth_category`)**

   - Contoh: `Shallow`, `Intermediate`, `Deep`

7. **Susun Ulang Kolom**
   - Untuk struktur data yang lebih rapi & konsisten

---

## 📦 Output Akhir

📁 Dataset akhir yang telah dibersihkan dan dikategorikan disimpan sebagai:

```
collectiondata/combined_earthquakes_ID.csv
```

Dataset ini siap untuk digunakan dalam analisis dan visualisasi interaktif.

---

## 📊 Visualisasi Interaktif

🔧 Visualisasi akan dibangun dengan teknologi **[D3.js](https://d3js.org/)** dan mencakup:

- 📍 Sebaran geografis gempa
- 🕒 Distribusi waktu kejadian
- 📊 Analisis magnitudo dan kedalaman

🎯 _Tujuan utama visualisasi:_

> Membantu pengguna memahami **tren dan pola gempa bumi di Indonesia** secara intuitif.

---

## 🚀 Cara Menjalankan

1. Clone repository ini:

   ```bash
   git clone https://github.com/Hidayattt24/Projek_Visdat.git
   cd Projek_Visdat
   ```

2. Install dependensi:

   ```bash
   pip install pandas numpy requests
   ```

3. Jalankan script preprocessing:

   ```bash
   python preprocessing.py
   ```

4. Lalu ke file earthquakesID.ipynb

---

## 🛠 Teknologi yang Digunakan

- 🐍 **Python**: `pandas`, `numpy`, `re`
- 📓 **Jupyter Notebook** _(opsional untuk eksplorasi interaktif)_
- 🌐 **D3.js** untuk visualisasi berbasis web

---

## 🤝 Kontribusi

Kontribusi sangat terbuka!  
Silakan `fork`, buat `branch`, dan `pull request` untuk saran, fitur baru, atau perbaikan bug 🔧

---

## 👨‍💻 Tim Pengembang

Kelompok ini terdiri dari mahasiswa aktif kelas A:

- 👤 **Muhammad Mahatir** — `2208107010056`
- 👤 **Hidayat Nur Hakim** — `2208107010063`
- 👤 **M. Agradika Ridhal Eljatin** — `2208107010020`
- 👤 **Muhammad Ridho** — `2208107010064`

---

📬 Untuk pertanyaan lebih lanjut, silakan hubungi salah satu anggota tim.  
Terima kasih telah mengunjungi proyek ini! 🙌