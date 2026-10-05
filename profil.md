# Yusuf Leo Rizaldy

Sarjana Teknologi Informasi Universitas Brawijaya, lulus Agustus 2026, IPK 3,85 dari 4,00.
Fokus: data engineering, machine learning terapan, dan AI engineering.
Kontak: yusufl.rizaldy@gmail.com
linkedin.com/in/yusufleor, github.com/YusufLeoR.
Domisili Yogyakarta, bersedia relokasi. Sedang mencari peran penuh waktu sebagai
Data Scientist, Data Analyst, Data Engineer, atau AI Engineer.

## Pengalaman kerja

### Data Scientist Intern, PT Telkom Indonesia (Maret 2025 - Mei 2025)
- Membangun chatbot retrieval-augmented generation dengan LangChain dan Azure OpenAI
  untuk proyek LPGenius, pendukung program subsidi LPG nasional.
- Melatih dan men-deploy model YOLOv8 untuk mendeteksi serta mengklasifikasi kondisi
  tabung LPG bagi pemantauan operasional.
- Merancang dan mengimplementasikan data mart MyPertamina Subsidi Tepat, termasuk
  pipeline ETL dan dashboard analitik untuk pelaporan.
- Menyusun dokumentasi teknis dan mengelola pengarsipan data OLTP serta OLAP.

### Asisten Praktikum Internet of Things, Laboratorium FILKOM UB (Agustus - Desember 2025)
Mendampingi mahasiswa mengonfigurasi sensor, mikrokontroler Arduino dan ESP, serta
protokol MQTT dan HTTP ke platform cloud. Membedah masalah integrasi perangkat keras
dan perangkat lunak, menyiapkan materi dan evaluasi praktikum.

### Asisten Praktikum SQL Programming, Laboratorium FILKOM UB (Agustus - Desember 2025)
Mendampingi penulisan query, perancangan skema, dan normalisasi basis data. Membimbing
latihan DDL, DML, join, subquery, indexing, dan optimasi query.

## Proyek

### Prediksi Harga Properti Kabupaten Sleman (skripsi, solo)
Live di rumah.yusufleo.my.id. Kode di github.com/YusufLeoR/Web-Prediksi-Harga-Rumah-Sleman.
Data dikumpulkan sendiri dengan web scraping properti123 dan OLX (undetected-chromedriver,
Selenium, BeautifulSoup) untuk 17 kecamatan, periode Februari sampai Maret 2026.
Pembersihan: dedup lalu pembuangan outlier IQR multiplier 2,5.
Rekayasa fitur aksesibilitas: jarak Haversine dari centroid kecamatan BPS ke 7 perguruan
tinggi, plus skor akses berbobot jumlah mahasiswa.
Seleksi fitur lewat voting empat metode (SelectKBest f_regression, RFE Random Forest,
LassoCV, importance Random Forest), diambil yang dipilih minimal dua metode: 16 dari 29 fitur.
Preprocessing di-fit hanya pada data latih untuk mencegah kebocoran data.
Sembilan algoritma dibandingkan dengan RepeatedKFold 5x6 dan diuji signifikansinya pakai
5x2cv paired t-test Dietterich serta combined F-test Alpaydin. XGBoost menang dengan
rata-rata rank 1,25; setara secara statistik dengan Random Forest, Gradient Boosting,
dan LightGBM, tetapi signifikan lebih baik dari semua model linear dan KNN.
Tuning RandomizedSearchCV 300 iterasi. Hasil akhir pada data uji: R2 0,8907,
RMSE Rp296,4 juta, MAE Rp154,1 juta, MAPE 13,28 persen, median galat absolut Rp51,8 juta.
Interpretasi SHAP: interaksi luas dengan jumlah kamar paling berpengaruh (Rp284,1 juta),
disusul luas tanah (Rp138,4 juta) dan jumlah kamar mandi (Rp130,2 juta). Jarak ke UGM
bertahan di sepuluh besar (Rp33,0 juta).
Batasan yang diakui: target adalah harga penawaran iklan bukan transaksi riil; data hanya
satu periode sehingga tidak menangkap tren waktu; lokasi didekati dengan centroid kecamatan
bukan koordinat presisi; galat besar terpusat pada rumah miliaran; cakupan hanya rumah
tapak di Kabupaten Sleman.

### Sistem Rekomendasi Kuliner Video Pendek (tim 3 orang, Datathon)
Kode di github.com/YusufLeoR/sistem-rekomendasi_mie-ayam-rohimah. Bersama Muhammad Varel
Antoni dan Rivaro Farrelino. Neural Collaborative Filtering hybrid: embedding untuk user,
video, toko, kategori, dan lokasi, digabung fitur numerik (jarak, koordinat, likes video,
durasi, rating), lalu Dense 64 ke 32 ke sigmoid. Binary crossentropy, Adam, 20 epoch,
batch 512. Hasil notebook: AUC uji 0,9766, akurasi 96 persen, F1 kelas positif 0,95,
dari 32.723 baris (26.178 latih, 6.545 uji).
Batasan yang diakui: dataset sintetis hasil generate, bukan perilaku pengguna nyata;
fitur likes_video berpotensi bocor terhadap label; keluaran Top-N masih memuat duplikat
dan probabilitas yang jenuh di 1,000; belum ada penanganan cold start.

### Personal Color Detector (capstone CC25-CF139, tim 6 orang, Yusuf di jalur Machine Learning)
Demo di color-tone-detector.vercel.app. Klasifikasi empat musim warna pribadi: Spring,
Summer, Autumn, Winter. Dataset 33.772 gambar dari Kaggle dan Roboflow. Label disusun dari
Hue ruang HSV untuk undertone dan Lightness ruang LAB untuk brightness. CNN dilatih 20 epoch,
akurasi latih 72,8 persen dan validasi 68 persen. Confusion matrix paling bersih di kelas
Spring dan Winter; Autumn, Spring, dan Summer sering tertukar.
Batasan yang diakui: sensitif terhadap pencahayaan, belum ada auto-cropping wajah,
dan rentang skintone pada dataset masih terbatas.

### Infrastruktur portofolio ini
Semua demo di situs ini berjalan di satu VPS 2 vCPU dan 2 GB RAM yang dikelola sendiri:
SSH key-only, root login dimatikan, UFW, unattended-upgrades, Docker Compose, dan Caddy
sebagai reverse proxy dengan sertifikat Let's Encrypt otomatis. Image dibangun di luar VPS
supaya tidak kehabisan memori. Chatbot yang kamu pakai sekarang juga salah satu kontainernya.

## Keterampilan
Bahasa: Python, SQL, PHP, TypeScript.
Data dan model: pandas, scikit-learn, XGBoost, SHAP, TensorFlow, YOLOv8.
AI terapan: LangChain, Azure OpenAI, retrieval-augmented generation.
Data engineering: pipeline ETL, pemodelan data mart, BigQuery, MySQL.
Penyajian: Streamlit, Next.js, Google Looker Studio.
Infrastruktur: Docker, Docker Compose, Caddy, Linux, Git.

## Organisasi
KBMDSI LKMM-TD dan Shaping the Future 2023, Staff Student Quality Control
(Agustus - November 2023).
Forum Komunikasi Pengurus OSIS DIY, Wakil Ketua dan Kepala Divisi Program
(Desember 2019 - Februari 2022).
