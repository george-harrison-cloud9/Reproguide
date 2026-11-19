# ReproGuide: Adaptive Reproductive Health Education Platform (MVP 1.0)

Platform edukasi kesehatan reproduksi adaptif berbasis web yang dirancang khusus untuk pelajar Sekolah Menengah Pertama (SMP kelas 7, 8, dan 9) di Indonesia. ReproGuide menyajikan materi ilmiah terpercaya, evaluasi kuis interaktif, klasifikasi tingkat pemahaman berbasis Machine Learning (*Decision Tree CART*), serta rekomendasi belajar yang dipersonalisasi.

---

## 📋 Daftar Isi

1. [Deskripsi Proyek](#-deskripsi-proyek)
2. [Tujuan Aplikasi](#-tujuan-aplikasi)
3. [Fitur Utama](#-fitur-utama)
4. [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
5. [Struktur Folder Proyek](#-struktur-folder-proyek)
6. [Penjelasan Model Machine Learning (Decision Tree CART)](#-penjelasan-model-machine-learning-decision-tree-cart)
7. [Penjelasan Dataset Simulasi](#-penjelasan-dataset-simulasi)
8. [Panduan Instalasi dan Menjalankan Aplikasi di Windows PowerShell](#-panduan-instalasi-dan-menjalankan-aplikasi-di-windows-powershell)
9. [Batasan Pengembangan MVP 1.0](#-batasan-pengembangan-mvp-10)
10. [Lisensi & Sumber Medis](#-lisensi--sumber-medis)

---

## 📖 Deskripsi Proyek

Kesehatan reproduksi merupakan bagian krusial dalam tumbuh kembang remaja, namun sering kali dianggap tabu dan sulit dibicarakan secara terbuka di lingkungan keluarga maupun sekolah. Banyak remaja akhirnya mencari informasi melalui internet tanpa verifikasi, yang berisiko menimbulkan salah paham, mitos keliru, ketakutan berlebih, atau bahkan terjerumus ke dalam perilaku berisiko.

**ReproGuide** (MVP 1.0) hadir sebagai platform pembelajaran ramah remaja (*youth-friendly*) yang:
- Menggunakan **100% Bahasa Indonesia** yang santun, sederhana, dan tidak menghakimi (*non-judgmental*).
- Menghindari istilah medis asing yang membingungkan tanpa penjelasan bahasa sehari-hari.
- Mengadopsi pedoman kesehatan terpercaya dari Kementerian Kesehatan Republik Indonesia (Kemenkes RI), UNICEF, dan World Health Organization (WHO).
- Menerapkan kecerdasan buatan (*Machine Learning*) dengan model **Decision Tree (CART)** untuk memetakan capaian belajar dan memberikan bimbingan belajar personal.

---

## 🎯 Tujuan Aplikasi

1. **Edukasi Inklusif & Akurat:** Menyediakan informasi kesehatan reproduksi yang mudah dipahami oleh pelajar SMP dengan beragam latar belakang literasi.
2. **Pengenalan Tumbuh Kembang Diri:** Membantu remaja memahami fase pubertas, perubahan anatomi, serta fungsi reproduksi alami tanpa rasa cemas atau malu.
3. **Pencegahan Berbasis Pengetahuan:** Membekali remaja dengan pemahaman preventif terhadap Infeksi Menular Seksual (IMS) dan langkah perlindungan diri dari kekerasan seksual.
4. **Evaluasi Berkelanjutan:** Menguji daya serap siswa melalui sistem kuis 50 soal pilihan ganda (10 soal per topik) disertai pembahasan edukatif.
5. **Rekomendasi Adaptif:** Mengidentifikasi topik yang paling dikuasai dan topik yang memerlukan pengulangan materi secara otomatis.

---

## 🌟 Fitur Utama

### 1. Modul 5 Topik Pembelajaran Komprehensif
Tersedia 5 topik utama yang terstruktur dengan format: Judul, Pengantar, Tujuan Belajar, Penjelasan Materi, Poin Penting, Ringkasan, dan Sumber Referensi:
1. **Pubertas:** Masa transisi menuju kedewasaan, peran hormon (testosteron & estrogen), dan penyesuaian emosi.
2. **Perubahan Tubuh dan Reproduksi:** Ciri kelamin primer dan sekunder, mimpi basah, siklus tubuh, serta *body positivity*.
3. **Kebersihan dan Menstruasi:** Pemahaman siklus haid alami, tata cara membasuh yang higienis, manajemen pembalut, dan kebersihan organ laki-laki.
4. **Pencegahan Infeksi Menular Seksual (IMS):** Pengertian IMS, fakta vs mitos penularan HIV/AIDS, serta sikap empati bagi ODHA.
5. **Pencegahan Kekerasan Seksual:** Batas area pribadi tubuh, konsep sentuhan aman vs tidak aman, langkah *TOLAK - LARI - LAPOR*, anti-*victim blaming*, dan UU TPKS No. 12 Tahun 2022.

### 2. Modul Kuis Interaktif (50 Pertanyaan)
- Tepat **10 soal per topik** dengan 4 pilihan ganda (A, B, C, D) dan 1 jawaban benar.
- Soal ditampilkan satu per satu dilengkapi bilah kemajuan (*progress indicator*).
- Sistem penilaian transparan: Benar = 10 poin, Salah = 0 poin (Maksimal 100 poin per topik).
- Kategori hasil kuis:
  - `0 - 50`: **Perlu Belajar Lagi**
  - `51 - 75`: **Cukup Memahami**
  - `76 - 100`: **Sudah Memahami**
- Pembahasan lengkap setelah kuis dikirim, serta opsi untuk mengulang kuis kapan saja.

### 3. Klasifikasi Machine Learning (CART Decision Tree)
- Memanfaatkan Scikit-learn `DecisionTreeClassifier` dengan kriteria pemisahan *Gini Impurity*.
- Memprediksi kategori tingkat pemahaman keseluruhan (*Rendah*, *Sedang*, atau *Tinggi*) berdasarkan kelas siswa dan skor 5 topik kuis.
- Menyajikan visualisasi *feature importance* dan logika percabangan pohon keputusan secara transparan.

### 4. Dashboard Rapor Hasil Pembelajaran
- Tampilan metrik rata-rata skor keseluruhan, topik paling dikuasai, dan topik yang perlu ditingkatkan.
- Visualisasi interaktif menggunakan grafik batang (*Bar Chart*) dan grafik radar kompetensi (*Radar Chart*) dari Plotly.
- Rekomendasi per topik dengan panduan langkah konkrit yang ramah dan memotivasi.

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Bahasa Pemrograman** | Python 3.9+ | Inti logika aplikasi dan pemodelan |
| **Framework Aplikasi Web** | Streamlit | Antarmuka web responsif dan interaktif |
| **Manajemen Data** | Pandas | Membaca dan memproses dataset tabular |
| **Machine Learning** | Scikit-learn | Model DecisionTreeClassifier (CART) |
| **Visualisasi Data** | Plotly | Grafik batang dan grafik radar interaktif |
| **Penyimpanan Status** | Streamlit Session State | Menyimpan sesi kuis dan nilai pengguna secara lokal |
| **Format Dataset** | CSV | `dataset_simulasi.csv` (300 baris data sintetis) |

> 💡 **Bebas Ketergantungan Eksternal:** Aplikasi ini **tidak memerlukan API Key**, tidak menggunakan database luar, dan dapat dijalankan secara luring (*offline*) setelah dependensi terpasang.

---

## 📂 Struktur Folder Proyek

```text
ReproGuide/
│
├── app.py                      # File utama aplikasi Streamlit (Router & UI)
├── dataset_simulasi.csv        # Dataset simulasi (300 baris, 7 kolom)
├── requirements.txt            # Daftar pustaka Python yang dibutuhkan
├── README.md                   # Dokumentasi teknis & panduan lengkap (Bahasa Indonesia)
├── .gitignore                  # Berkas pengecualian Git
│
├── modules/
│   ├── __init__.py             # Inisialisasi paket modul Python
│   ├── data_loader.py          # Modul pemuatan, validasi, dan ringkasan dataset
│   ├── learning_materials.py   # Modul konten 5 topik pembelajaran terverifikasi
│   ├── quiz.py                 # Bank soal 50 pertanyaan, skoring, & evaluasi kuis
│   ├── machine_learning.py     # Pelatihan dan inferensi model Decision Tree (CART)
│   └── recommendation.py       # Logika sistem rekomendasi belajar adaptif
│
└── assets/
    └── logo.png                # Logo resmi ReproGuide
```

---

## 🧠 Penjelasan Model Machine Learning (Decision Tree CART)

Algoritma yang digunakan dalam ReproGuide adalah **CART (Classification and Regression Trees)** yang diimplementasikan melalui `sklearn.tree.DecisionTreeClassifier`.

### Mengapa Decision Tree?
1. **Dapat Diinterpretasikan (*White-Box Model*):** Sangat cocok untuk bidang edukasi karena pendidik dan siswa dapat melihat secara persis aturan percabangan (*if-then rules*) yang mendasari keputusan model.
2. **Cepat dan Ringan:** Dapat dilatih dalam hitungan milidetik secara lokal di komputer tanpa memerlukan akselerator grafis (GPU).
3. **Mampu Menangani Hubungan Non-Linear:** Mengakomodasi variasi pemahaman antar-mata uji secara alami.

### Parameter Model:
- `criterion='gini'`: Mengukur kemurnian pemisahan (*Gini Impurity*).
- `max_depth=4`: Membatasi kedalaman pohon untuk mencegah *overfitting* dan menjaga aturan tetap mudah dipahami.
- `random_state=42`: Menjamin hasil pembagian data latih/uji dan pembentukan pohon dapat direproduksi (*reproducible*).

### Fitur Input:
1. `kelas`: Tingkat kelas SMP (7, 8, atau 9).
2. `skor_pubertas`: Nilai kuis topik Pubertas (0 - 100).
3. `skor_perubahan_tubuh`: Nilai kuis topik Perubahan Tubuh dan Reproduksi (0 - 100).
4. `skor_kebersihan_menstruasi`: Nilai kuis topik Kebersihan dan Menstruasi (0 - 100).
5. `skor_pencegahan_ims`: Nilai kuis topik Pencegahan IMS (0 - 100).
6. `skor_pencegahan_kekerasan_seksual`: Nilai kuis topik Pencegahan Kekerasan Seksual (0 - 100).

### Target Prediksi:
- `kategori_pemahaman`: **Rendah**, **Sedang**, atau **Tinggi**.

---

## 📊 Penjelasan Dataset Simulasi

File `dataset_simulasi.csv` berisi **300 baris data sintetis** yang dimodelkan berdasarkan pola logis hasil evaluasi siswa SMP:
- Distribusi kelas seimbang (Kelas 7, 8, dan 9).
- Distribusi target: 90 baris kategori *Rendah*, 110 baris kategori *Sedang*, dan 100 baris kategori *Tinggi*.
- Setiap nilai kuis berkisar kelipatan 10 (antara 0 hingga 100) sesuai bobot 10 soal kuis.

> ⚠️ **Catatan Penting Akademis:** Dataset ini merupakan data simulasi sintetis murni untuk keperluan pengujian fungsionalitas algoritma (*Proof of Concept* MVP). Data ini **bukan** berasal dari rekam medis siswa dan tidak memiliki klaim validitas klinis.

---

## 💻 Panduan Instalasi dan Menjalankan Aplikasi di Windows PowerShell

Ikuti langkah-langkah di bawah ini untuk menginstal dan menjalankan ReproGuide pada terminal **Windows PowerShell**:

### 1. Masuk ke Direktori Proyek
Buka VS Code atau Windows PowerShell, lalu navigasikan ke folder ReproGuide:
```powershell
cd C:\Users\USER\.gemini\antigravity\scratch\ReproGuide
```

### 2. (Opsional namun Disarankan) Membuat Virtual Environment
Buat dan aktifkan lingkungan virtual terisolasi:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(Jika muncul peringatan Execution Policy pada PowerShell, jalankan: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` lalu ulangi perintah aktivasi di atas).*

### 3. Menginstal Seluruh Dependensi
Jalankan instalasi pustaka dari berkas `requirements.txt`:
```powershell
pip install -r requirements.txt
```

### 4. Menjalankan Aplikasi Streamlit
Jalankan aplikasi dengan perintah:
```powershell
streamlit run app.py
```

Setelah perintah dijalankan, Streamlit akan otomatis membuka aplikasi di peramban web (*browser*) default Anda pada alamat:
`http://localhost:8501`

---

## 🛡️ Batasan Pengembangan MVP 1.0

Sebagai rilis versi pertama (*Minimum Viable Product* 1.0), batasan lingkup berikut berlaku:
1. **Sesi Berbasis Memori (*In-Memory*):** Progres evaluasi dan nilai kuis disimpan selama tab peramban aktif melalui `st.session_state`. Menutup peramban akan mereset progres (tidak menggunakan database SQL/NoSQL eksternal).
2. **Tidak Menggunakan Sistem Autentikasi/Login:** Tidak ada formulir registrasi atau kata sandi demi menjaga kenyamanan dan privasi anak.
3. **Data Sintetis:** Model dilatih menggunakan `dataset_simulasi.csv`.
4. **Bukan Rekomendasi Medis/Diagnosis:** Hasil prediksi ditujukan semata-mata untuk bimbingan belajar dan pemetaan kurikulum literasi remaja.

---

## 📚 Lisensi & Sumber Medis

Materi edukatif disusun berdasarkan pedoman resmi:
- **Kementerian Kesehatan Republik Indonesia (Kemenkes RI)**: *Buku Saku Kesehatan Reproduksi Remaja* & *Modul Pelayanan Kesehatan Peduli Remaja (PKPR)*.
- **World Health Organization (WHO)**: *Adolescent Health and Development Guidelines*.
- **UNICEF**: *Manajemen Kebersihan Menstruasi (MKM) dan Sanitasi Sekolah di Indonesia*.
- **Hukum Indonesia**: *Undang-Undang Tindak Pidana Kekerasan Seksual (UU TPKS) No. 12 Tahun 2022*.

---
*Dikembangkan dengan penuh dedikasi untuk kemajuan edukasi kesehatan reproduksi remaja Indonesia yang bermartabat, sehat, dan berdaya.*
