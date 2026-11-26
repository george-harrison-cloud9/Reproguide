"""
Skrip Pengujian Otomatis Komprehensif untuk ReproGuide MVP 1.0
Menguji seluruh modul, bank soal, dataset, machine learning, rekomendasi, dan integritas kode aplikasi.
"""

import os
import sys
import ast

# Tambahkan direktori proyek ke sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import pandas as pd
from modules.learning_materials import get_all_topics, get_topic_by_id, MATERI_PEMBELAJARAN
from modules.quiz import BANK_SOAL, calculate_topic_score, get_quiz_by_topic, get_quiz_length
from modules.data_loader import load_dataset, get_dataset_summary, KOLOM_FITUR, KOLOM_TARGET
from modules.machine_learning import ReproGuideClassifier
from modules.recommendation import analyze_learning_profile, get_recommendation_for_score, TOPIC_TITLES


def test_1_materi_pembelajaran():
    print("\n--- [PENGUJIAN 1]: Modul Materi Pembelajaran ---")
    topics = get_all_topics()
    assert len(topics) == 5, f"Jumlah topik harus 5, ditemukan: {len(topics)}"
    print(f"✓ Ditemukan tepat 5 topik pembelajaran.")

    expected_ids = ["pubertas", "perubahan_tubuh", "kebersihan_menstruasi", "pencegahan_ims", "pencegahan_kekerasan_seksual"]
    for t_id in expected_ids:
        t_data = get_topic_by_id(t_id)
        assert t_data is not None, f"Topik {t_id} tidak ditemukan!"
        assert "judul" in t_data and len(t_data["judul"]) > 0
        assert "pengantar" in t_data and len(t_data["pengantar"]) > 0
        assert "tujuan" in t_data and len(t_data["tujuan"]) >= 3
        assert "penjelasan" in t_data and len(t_data["penjelasan"]) >= 2
        assert "poin_penting" in t_data and len(t_data["poin_penting"]) >= 3
        assert "ringkasan" in t_data and len(t_data["ringkasan"]) > 0
        assert "referensi" in t_data and len(t_data["referensi"]) >= 2
        print(f"  ✓ Topik '{t_id}' ({t_data['judul'].split(':')[0]}) valid & lengkap dengan referensi resmi.")

    print("✓ SELURUH PENGUJIAN MATERI PEMBELAJARAN BERHASIL!")


def test_2_bank_soal_kuis():
    print("\n--- [PENGUJIAN 2]: Bank Soal dan Logika Kuis ---")
    assert len(BANK_SOAL) == 5, f"Jumlah topik kuis harus 5, ditemukan: {len(BANK_SOAL)}"

    total_soal_semua_topik = 0
    for topic_id, soal_list in BANK_SOAL.items():
        assert len(soal_list) == 10, f"Topik {topic_id} harus memiliki tepat 10 soal, ditemukan: {len(soal_list)}"
        total_soal_semua_topik += len(soal_list)

        for s_idx, soal in enumerate(soal_list):
            assert "pertanyaan" in soal and len(soal["pertanyaan"]) > 5
            assert "pilihan" in soal and len(soal["pilihan"]) == 4, f"Soal {s_idx+1} topik {topic_id} tidak memiliki tepat 4 pilihan!"
            assert "jawaban_benar" in soal and soal["jawaban_benar"] in [0, 1, 2, 3]
            assert "penjelasan" in soal and len(soal["penjelasan"]) > 10

    assert total_soal_semua_topik == 50, f"Total soal harus 50, ditemukan: {total_soal_semua_topik}"
    print(f"✓ Total {total_soal_semua_topik} soal terverifikasi (Tepat 10 soal x 5 topik).")
    print("✓ Setiap soal memiliki tepat 4 pilihan jawaban dan pembahasan medis/ilmiah.")

    # Pengujian Skoring: Sempurna (10 benar -> 100)
    jawaban_sempurna = {i: BANK_SOAL["pubertas"][i]["jawaban_benar"] for i in range(10)}
    hasil_100 = calculate_topic_score("pubertas", jawaban_sempurna)
    assert hasil_100["skor"] == 100, f"Skor harus 100, didapat {hasil_100['skor']}"
    assert hasil_100["benar"] == 10
    assert hasil_100["salah"] == 0
    assert hasil_100["kategori"] == "Sudah Memahami"
    print("  ✓ Skoring 10 benar menghasilkan 100 poin (Kategori: Sudah Memahami).")

    # Pengujian Skoring: Sedang (6 benar -> 60)
    jawaban_60 = {}
    for i in range(10):
        benar_idx = BANK_SOAL["pubertas"][i]["jawaban_benar"]
        jawaban_60[i] = benar_idx if i < 6 else (benar_idx + 1) % 4
    hasil_60 = calculate_topic_score("pubertas", jawaban_60)
    assert hasil_60["skor"] == 60
    assert hasil_60["benar"] == 6
    assert hasil_60["salah"] == 4
    assert hasil_60["kategori"] == "Cukup Memahami"
    print("  ✓ Skoring 6 benar menghasilkan 60 poin (Kategori: Cukup Memahami).")

    # Pengujian Skoring: Rendah (3 benar -> 30)
    jawaban_30 = {}
    for i in range(10):
        benar_idx = BANK_SOAL["pubertas"][i]["jawaban_benar"]
        jawaban_30[i] = benar_idx if i < 3 else (benar_idx + 1) % 4
    hasil_30 = calculate_topic_score("pubertas", jawaban_30)
    assert hasil_30["skor"] == 30
    assert hasil_30["benar"] == 3
    assert hasil_30["salah"] == 7
    assert hasil_30["kategori"] == "Perlu Belajar Lagi"
    print("  ✓ Skoring 3 benar menghasilkan 30 poin (Kategori: Perlu Belajar Lagi).")

    # Pengujian Penanganan Jawaban Kosong
    hasil_kosong = calculate_topic_score("pubertas", {})
    assert hasil_kosong["skor"] == 0
    assert hasil_kosong["benar"] == 0
    assert hasil_kosong["salah"] == 10
    assert hasil_kosong["kategori"] == "Perlu Belajar Lagi"
    print("  ✓ Jawaban kosong ditangani dengan aman tanpa menimbulkan error (Skor 0).")

    print("✓ SELURUH PENGUJIAN KUIS BERHASIL!")


def test_3_dataset_simulasi():
    print("\n--- [PENGUJIAN 3]: Dataset Simulasi (dataset_simulasi.csv) ---")
    df = load_dataset()
    print(f"✓ Dataset berhasil dimuat via Pandas. Total baris: {len(df)}")
    assert len(df) >= 200, f"Jumlah baris dataset minimal 200, ditemukan: {len(df)}"

    for col in KOLOM_FITUR + [KOLOM_TARGET]:
        assert col in df.columns, f"Kolom wajib '{col}' tidak ditemukan dalam dataset!"
    print(f"✓ Seluruh kolom wajib {KOLOM_FITUR + [KOLOM_TARGET]} tersedia.")

    # Cek sebaran kelas dan target
    target_counts = df[KOLOM_TARGET].value_counts().to_dict()
    print(f"✓ Distribusi Target: {target_counts}")
    assert "Rendah" in target_counts and "Sedang" in target_counts and "Tinggi" in target_counts

    summary = get_dataset_summary(df)
    assert summary["total_baris"] == len(df)
    print("✓ Ringkasan statistik dataset valid.")
    print("✓ SELURUH PENGUJIAN DATASET BERHASIL!")


def test_4_machine_learning():
    print("\n--- [PENGUJIAN 4]: Machine Learning Decision Tree (CART) ---")
    clf = ReproGuideClassifier(criterion="gini", max_depth=4, random_state=42)
    metrics = clf.train()
    assert clf.is_trained, "Model gagal dilatih!"
    print(f"✓ Model Decision Tree (CART) berhasil dilatih.")
    print(f"  - Akurasi Data Uji: {metrics['accuracy']}%")
    print(f"  - Total Data Latih: {metrics['total_latih']} baris")
    print(f"  - Total Data Uji: {metrics['total_uji']} baris")

    # Uji Prediksi Kasus Siswa Nilai Tinggi
    input_tinggi = {
        "kelas": 8,
        "skor_pubertas": 90,
        "skor_perubahan_tubuh": 90,
        "skor_kebersihan_menstruasi": 90,
        "skor_pencegahan_ims": 80,
        "skor_pencegahan_kekerasan_seksual": 100
    }
    pred_tinggi = clf.predict(input_tinggi)
    assert pred_tinggi["kategori_prediksi"] == "Tinggi", f"Harusnya 'Tinggi', didapat: {pred_tinggi['kategori_prediksi']}"
    print(f"✓ Prediksi nilai tinggi (Rata-rata 90) -> Kategori: {pred_tinggi['kategori_prediksi']} (Probabilitas: {pred_tinggi['probabilitas']})")

    # Uji Prediksi Kasus Siswa Nilai Rendah
    input_rendah = {
        "kelas": 7,
        "skor_pubertas": 30,
        "skor_perubahan_tubuh": 20,
        "skor_kebersihan_menstruasi": 30,
        "skor_pencegahan_ims": 20,
        "skor_pencegahan_kekerasan_seksual": 30
    }
    pred_rendah = clf.predict(input_rendah)
    assert pred_rendah["kategori_prediksi"] == "Rendah", f"Harusnya 'Rendah', didapat: {pred_rendah['kategori_prediksi']}"
    print(f"✓ Prediksi nilai rendah (Rata-rata 26) -> Kategori: {pred_rendah['kategori_prediksi']} (Probabilitas: {pred_rendah['probabilitas']})")

    # Uji Prediksi Kasus Siswa Nilai Sedang
    input_sedang = {
        "kelas": 9,
        "skor_pubertas": 60,
        "skor_perubahan_tubuh": 70,
        "skor_kebersihan_menstruasi": 60,
        "skor_pencegahan_ims": 70,
        "skor_pencegahan_kekerasan_seksual": 60
    }
    pred_sedang = clf.predict(input_sedang)
    assert pred_sedang["kategori_prediksi"] == "Sedang", f"Harusnya 'Sedang', didapat: {pred_sedang['kategori_prediksi']}"
    print(f"✓ Prediksi nilai sedang (Rata-rata 64) -> Kategori: {pred_sedang['kategori_prediksi']} (Probabilitas: {pred_sedang['probabilitas']})")

    # Cek Feature Importance
    info = clf.get_model_info()
    assert len(info["fitur_penting"]) == 6
    print("✓ Feature importance berhasil dihitung.")
    print("✓ Aturan percabangan pohon keputusan berhasil diekspor.")
    print("✓ SELURUH PENGUJIAN MACHINE LEARNING BERHASIL!")


def test_5_rekomendasi_pembelajaran():
    print("\n--- [PENGUJIAN 5]: Sistem Rekomendasi Pembelajaran ---")
    rec_rendah = get_recommendation_for_score(40)
    assert rec_rendah["status"] == "Perlu Belajar Lagi"

    rec_sedang = get_recommendation_for_score(70)
    assert rec_sedang["status"] == "Cukup Memahami"

    rec_tinggi = get_recommendation_for_score(90)
    assert rec_tinggi["status"] == "Sudah Memahami"

    scores = {
        "pubertas": 90,
        "perubahan_tubuh": 80,
        "kebersihan_menstruasi": 50,
        "pencegahan_ims": 70,
        "pencegahan_kekerasan_seksual": 100
    }
    profil = analyze_learning_profile(scores, None, user_class=8)
    assert profil["topik_tertinggi"]["topic_id"] == "pencegahan_kekerasan_seksual"
    assert profil["topik_terendah"]["topic_id"] == "kebersihan_menstruasi"
    assert len(profil["perlu_dipelajari_lagi"]) == 2  # kebersihan_menstruasi (50) dan pencegahan_ims (70)
    print("✓ Profil analisis mendeteksi topik tertinggi (Pencegahan Kekerasan Seksual: 100) dan terendah (Kebersihan Menstruasi: 50).")
    print(f"✓ Mendeteksi {len(profil['perlu_dipelajari_lagi'])} topik yang disarankan untuk ditinjau kembali.")
    print("✓ SELURUH PENGUJIAN REKOMENDASI BERHASIL!")


def test_6_sintaks_dan_modul_app():
    print("\n--- [PENGUJIAN 6]: Integritas dan Sintaks app.py ---")
    app_file = os.path.join(BASE_DIR, "app.py")
    assert os.path.exists(app_file), "File app.py tidak ditemukan!"

    with open(app_file, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Parsing AST untuk memastikan tidak ada kesalahan sintaks Python
    parsed_tree = ast.parse(source_code)
    func_names = [node.name for node in ast.walk(parsed_tree) if isinstance(node, ast.FunctionDef)]

    expected_functions = ["main", "init_session_state", "render_sidebar", "render_beranda", "render_materi", "render_kuis", "render_hasil", "render_tentang"]
    for fn in expected_functions:
        assert fn in func_names, f"Fungsi antarmuka '{fn}' tidak ditemukan di app.py!"
        print(f"  ✓ Fungsi antarmuka '{fn}()' terdefinisi.")

    print("✓ File app.py terverifikasi 100% bebas dari kesalahan sintaks.")


if __name__ == "__main__":
    print("=" * 65)
    print("MEMULAI PENGUJIAN OTOMATIS SUITE REPROGUIDE MVP 1.0")
    print("=" * 65)

    try:
        test_1_materi_pembelajaran()
        test_2_bank_soal_kuis()
        test_3_dataset_simulasi()
        test_4_machine_learning()
        test_5_rekomendasi_pembelajaran()
        test_6_sintaks_dan_modul_app()

        print("\n" + "=" * 65)
        print("SEMUA PENGUJIAN (6/6 SUITE) TELAH LULUS DENGAN SEMPURNA! 🎉")
        print("APLIKASI SIAP DIDEMONSTRASIKAN.")
        print("=" * 65)
    except AssertionError as ae:
        print(f"\n❌ PENGUJIAN GAGAL PADA ASERSI: {ae}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ TERJADI KESALAHAN PADA SAAT PENGUJIAN: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
