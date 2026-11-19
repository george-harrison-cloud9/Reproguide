"""
Modul Sistem Rekomendasi Pembelajaran ReproGuide
Menganalisis hasil evaluasi kuis dan hasil prediksi Decision Tree untuk
menghasilkan rekomendasi belajar adaptif per topik dan rekomendasi umum.
"""

TOPIC_TITLES = {
    "pubertas": "Pubertas",
    "perubahan_tubuh": "Perubahan Tubuh dan Reproduksi",
    "kebersihan_menstruasi": "Kebersihan dan Menstruasi",
    "pencegahan_ims": "Pencegahan Infeksi Menular Seksual (IMS)",
    "pencegahan_kekerasan_seksual": "Pencegahan Kekerasan Seksual"
}


def get_recommendation_for_score(score):
    """
    Menghasilkan teks rekomendasi dan status berdasarkan rentang nilai kuis:
    - 0-50: Pelajari kembali materi dari awal.
    - 51-75: Baca kembali bagian yang belum dipahami dan pelajari pembahasan jawaban yang salah.
    - 76-100: Penguatan pemahaman melalui materi lanjutan atau aktivitas pengayaan.
    """
    if score <= 50:
        return {
            "status": "Perlu Belajar Lagi",
            "warna": "#E53935",  # Merah bersahabat
            "badge_class": "badge-danger",
            "pesan": (
                "Sebaiknya pelajari kembali materi topik ini dari awal. "
                "Jangan berkecil hati, kamu bisa membaca kembali ringkasan materi dan memahami "
                "poin-poin penting sebelum mencoba kuis ini sekali lagi!"
            ),
            "tindakan": "Pelajari ulang materi secara menyeluruh",
            "fokus": "Ulangi membaca tujuan pembelajaran dan penjelasan konsep dasar."
        }
    elif score <= 75:
        return {
            "status": "Cukup Memahami",
            "warna": "#FB8C00",  # Oranye hangat
            "badge_class": "badge-warning",
            "pesan": (
                "Pemahamanmu sudah cukup baik! Kamu disarankan membaca kembali bagian materi "
                "yang masih ragu dan mencermati pembahasan jawaban soal yang belum tepat "
                "agar semakin percaya diri."
            ),
            "tindakan": "Fokus pada pembahasan jawaban kuis yang keliru",
            "fokus": "Baca kembali poin penting dan pelajari alasan jawaban yang benar."
        }
    else:
        return {
            "status": "Sudah Memahami",
            "warna": "#43A047",  # Hijau positif
            "badge_class": "badge-success",
            "pesan": (
                "Luar biasa! Kamu sudah memahami materi topik ini dengan sangat baik. "
                "Pertahankan prestasimu dengan melakukan pengayaan wawasan dan saling berbagi "
                "informasi positif yang benar kepada teman-teman sebaya."
            ),
            "tindakan": "Penguatan pemahaman dan pengayaan wawasan",
            "fokus": "Bagikan pengetahuan yang benar dan jadilah contoh bagi teman sebaya."
        }


def analyze_learning_profile(scores_dict, ml_prediction=None, user_class=8):
    """
    Menganalisis hasil kuis seluruh topik dan menyusun profil pembelajaran lengkap.
    scores_dict: dict {topic_id: score_int}
    ml_prediction: hasil dict dari ReproGuideClassifier.predict()
    """
    topic_items = []
    for topic_id, score in scores_dict.items():
        title = TOPIC_TITLES.get(topic_id, topic_id.replace("_", " ").title())
        rec = get_recommendation_for_score(score)
        topic_items.append({
            "topic_id": topic_id,
            "judul": title,
            "skor": score,
            "status": rec["status"],
            "warna": rec["warna"],
            "pesan": rec["pesan"],
            "tindakan": rec["tindakan"],
            "fokus": rec["fokus"]
        })

    # Urutkan berdasarkan skor
    sorted_by_score = sorted(topic_items, key=lambda x: x["skor"], reverse=True)

    topik_tertinggi = sorted_by_score[0] if sorted_by_score else None
    topik_terendah = sorted_by_score[-1] if sorted_by_score else None

    # Topik yang perlu dipelajari kembali (skor <= 75, terutama <= 50)
    perlu_dipelajari_lagi = [t for t in sorted_by_score if t["skor"] <= 75]

    rata_rata = sum(scores_dict.values()) / max(1, len(scores_dict))
    rata_rata = round(rata_rata, 1)

    # Pesan umum berdasarkan profil
    if rata_rata >= 80:
        pesan_umum = (
            f"Selamat! Sebagai siswa kelas {user_class}, kamu menunjukkan tingkat pemahaman kesehatan reproduksi "
            "yang sangat matang. Terus pertahankan sikap peduli dan bijak dalam menjaga diri."
        )
    elif rata_rata >= 60:
        pesan_umum = (
            f"Hasil yang bagus! Pemahaman dasar kamu di kelas {user_class} sudah terbentuk dengan baik. "
            "Fokuslah meninjau topik yang nilainya masih di bawah 75 untuk menyempurnakan pemahamanmu."
        )
    else:
        pesan_umum = (
            f"Tetap semangat! Mempelajari kesehatan reproduksi membutuhkan waktu dan ketelitian. "
            "Manfaatkan rangkuman materi dan pelajari kembali topik-topik utama secara bertahap."
        )

    # Interpretasi Prediksi ML
    ml_info = ""
    if ml_prediction:
        kat_pred = ml_prediction.get("kategori_prediksi", "Sedang")
        if kat_pred == "Tinggi":
            ml_info = (
                "Model Decision Tree mengelompokkan profil pemahamanmu ke dalam kategori **Tinggi**. "
                "Artinya, pola jawabanmu secara keseluruhan konsisten menunjukkan penguasaan materi yang matang."
            )
        elif kat_pred == "Sedang":
            ml_info = (
                "Model Decision Tree mengelompokkan profil pemahamanmu ke dalam kategori **Sedang**. "
                "Pola pemahamanmu cukup merata, namun ada beberapa materi spesifik yang perlu diperkuat."
            )
        else:
            ml_info = (
                "Model Decision Tree mengelompokkan profil pemahamanmu ke dalam kategori **Rendah**. "
                "Sistem menyarankan kamu meluangkan waktu mempelajari kembali materi modul sebelum tes ulang."
            )

    return {
        "rata_rata": rata_rata,
        "topik_tertinggi": topik_tertinggi,
        "topik_terendah": topik_terendah,
        "perlu_dipelajari_lagi": perlu_dipelajari_lagi,
        "detail_per_topik": topic_items,
        "pesan_umum": pesan_umum,
        "ml_info": ml_info
    }
