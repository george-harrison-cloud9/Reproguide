"""
Modul Pemuat Data ReproGuide
Bertanggung jawab membaca, memvalidasi, dan menyediakan statistik ringkasan
dari dataset simulasi (dataset_simulasi.csv).
"""

import os
import pandas as pd

KOLOM_FITUR = [
    "kelas",
    "skor_pubertas",
    "skor_perubahan_tubuh",
    "skor_kebersihan_menstruasi",
    "skor_pencegahan_ims",
    "skor_pencegahan_kekerasan_seksual"
]

KOLOM_TARGET = "kategori_pemahaman"

KOLOM_WAJIB = KOLOM_FITUR + [KOLOM_TARGET]


def get_default_dataset_path():
    """Mengembalikan jalur default file dataset_simulasi.csv."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "dataset_simulasi.csv")


def load_dataset(file_path=None):
    """
    Membaca dataset simulasi menggunakan Pandas.
    Mengembalikan DataFrame jika valid, atau None jika gagal.
    """
    if file_path is None:
        file_path = get_default_dataset_path()

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File dataset simulasi tidak ditemukan di lokasi: {file_path}. "
            "Pastikan file dataset_simulasi.csv berada di direktori utama proyek."
        )

    df = pd.read_csv(file_path)

    # Validasi kelengkapan kolom
    missing_cols = [col for col in KOLOM_WAJIB if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Dataset tidak memiliki kolom wajib berikut: {', '.join(missing_cols)}"
        )

    # Validasi jumlah baris minimal (200 baris)
    if len(df) < 200:
        raise ValueError(
            f"Dataset hanya memiliki {len(df)} baris. "
            "Persyaratan minimum adalah 200 baris data simulasi."
        )

    return df


def get_dataset_summary(df):
    """
    Menghasilkan ringkasan statistik dataset simulasi untuk kebutuhan eksplorasi.
    """
    total_baris = len(df)
    distribusi_kategori = df[KOLOM_TARGET].value_counts().to_dict()
    distribusi_kelas = df["kelas"].value_counts().sort_index().to_dict()

    rata_rata_skor = {
        "Pubertas": round(df["skor_pubertas"].mean(), 1),
        "Perubahan Tubuh": round(df["skor_perubahan_tubuh"].mean(), 1),
        "Kebersihan Menstruasi": round(df["skor_kebersihan_menstruasi"].mean(), 1),
        "Pencegahan IMS": round(df["skor_pencegahan_ims"].mean(), 1),
        "Pencegahan Kekerasan Seksual": round(df["skor_pencegahan_kekerasan_seksual"].mean(), 1),
    }

    return {
        "total_baris": total_baris,
        "distribusi_kategori": distribusi_kategori,
        "distribusi_kelas": distribusi_kelas,
        "rata_rata_skor": rata_rata_skor,
        "deskripsi": (
            "Dataset ini berisi data simulasi sintetis siswa SMP (Kelas 7, 8, dan 9) "
            "yang dibuat khusus untuk melatih model Decision Tree ReproGuide MVP 1.0. "
            "Data ini tidak menggunakan data pribadi siswa sungguhan dan tidak memiliki akurasi klinis."
        )
    }
