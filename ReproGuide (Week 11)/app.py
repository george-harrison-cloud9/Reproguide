"""
ReproGuide - Adaptive Reproductive Health Education Platform
Aplikasi Edukasi Kesehatan Reproduksi Berbasis Streamlit dan Machine Learning (CART Decision Tree)
Seluruh antarmuka menggunakan Bahasa Indonesia yang ramah, santun, dan mudah dipahami pelajar SMP.
"""

import os
import sys

# Memastikan direktori proyek terdaftar dalam sys.path agar modul lokal selalu ditemukan
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from modules.data_loader import load_dataset, get_dataset_summary
from modules.learning_materials import get_all_topics, get_topic_by_id, MATERI_PEMBELAJARAN
from modules.quiz import BANK_SOAL, calculate_topic_score, get_quiz_by_topic
from modules.machine_learning import ReproGuideClassifier
from modules.recommendation import analyze_learning_profile, get_recommendation_for_score, TOPIC_TITLES

# ==============================================================================
# GAYA CSS KUSTOM (Tema Biru Modern, Minimalis, Ramah Remaja)
# ==============================================================================
CUSTOM_CSS = """
<style>
    /* Font dan Warna Global */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header & Hero Card */
    .hero-card {
        background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(30, 136, 229, 0.22);
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #FFFFFF;
    }
    
    .hero-subtitle {
        font-size: 1.15rem;
        opacity: 0.95;
        line-height: 1.6;
        color: #E3F2FD;
    }
    
    /* Kartu Konten */
    .content-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .content-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    }
    
    /* Kartu Topik Beranda */
    .topic-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 6px solid #1E88E5;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    
    .topic-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #0F172A;
        margin-bottom: 0.4rem;
    }
    
    .topic-desc {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.5;
    }
    
    /* Badge Status */
    .badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        font-size: 0.85rem;
        font-weight: 600;
        border-radius: 9999px;
    }
    
    .badge-success {
        background-color: #E8F5E9;
        color: #2E7D32;
        border: 1px solid #C8E6C9;
    }
    
    .badge-warning {
        background-color: #FFF3E0;
        color: #E65100;
        border: 1px solid #FFE0B2;
    }
    
    .badge-danger {
        background-color: #FFEBEE;
        color: #C62828;
        border: 1px solid #FFCDD2;
    }
    
    .badge-info {
        background-color: #E3F2FD;
        color: #1565C0;
        border: 1px solid #BBDEFB;
    }
    
    /* Poin Penting Box */
    .highlight-box {
        background-color: #F0F9FF;
        border-left: 4px solid #0284C7;
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #0369A1;
    }
    
    /* Disclaimer Box */
    .disclaimer-box {
        background-color: #FFFBEB;
        border-left: 4px solid #F59E0B;
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin: 1.25rem 0;
        color: #92400E;
        font-size: 0.92rem;
    }
    
    /* Tombol Utama Streamlit */
    div.stButton > button {
        background-color: #1E88E5;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.6rem 1.4rem;
        border: none;
        transition: all 0.2s ease;
    }
    
    div.stButton > button:hover {
        background-color: #1565C0;
        box-shadow: 0 4px 12px rgba(21, 101, 192, 0.3);
        transform: translateY(-1px);
    }
    
    /* Metrik Dashboard */
    .metric-container {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E88E5;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #64748B;
        margin-top: 0.25rem;
    }

    /* Penyesuaian Responsif untuk Layar Telepon Seluler (Mobile) */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 1.6rem !important;
        }
        .hero-subtitle {
            font-size: 0.95rem !important;
            line-height: 1.5 !important;
        }
        .hero-card {
            padding: 1.3rem !important;
            border-radius: 12px !important;
            margin-bottom: 1.2rem !important;
        }
        .content-card {
            padding: 1rem !important;
            border-radius: 10px !important;
        }
        .metric-value {
            font-size: 1.5rem !important;
        }
        .metric-label {
            font-size: 0.8rem !important;
        }
        div.stButton > button {
            padding: 0.5rem 1rem !important;
            font-size: 0.9rem !important;
        }
    }
</style>
"""

# ==============================================================================
# INISIALISASI SESSION STATE
# ==============================================================================
def init_session_state():
    """Menginisialisasi seluruh variabel session state yang dibutuhkan aplikasi."""
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Beranda"

    if "user_class" not in st.session_state:
        st.session_state["user_class"] = 8  # Default siswa kelas 8 SMP

    if "selected_topic_material" not in st.session_state:
        st.session_state["selected_topic_material"] = "pubertas"

    if "selected_topic_quiz" not in st.session_state:
        st.session_state["selected_topic_quiz"] = "pubertas"

    # Status jawaban kuis per topik
    topic_keys = list(BANK_SOAL.keys())
    if "quiz_answers" not in st.session_state:
        st.session_state["quiz_answers"] = {k: {} for k in topic_keys}

    if "quiz_current_q" not in st.session_state:
        st.session_state["quiz_current_q"] = {k: 0 for k in topic_keys}

    if "quiz_scores" not in st.session_state:
        # Default 0 untuk setiap topik kuis
        st.session_state["quiz_scores"] = {k: 0 for k in topic_keys}

    if "quiz_submitted" not in st.session_state:
        st.session_state["quiz_submitted"] = {k: False for k in topic_keys}

    if "ml_classifier" not in st.session_state:
        # Inisialisasi dan latih model Decision Tree
        try:
            clf = ReproGuideClassifier(criterion="gini", max_depth=4, random_state=42)
            clf.train()
            st.session_state["ml_classifier"] = clf
            st.session_state["ml_ready"] = True
        except Exception as e:
            st.session_state["ml_classifier"] = None
            st.session_state["ml_ready"] = False
            st.session_state["ml_error"] = str(e)


# ==============================================================================
# SIDEBAR / NAVIGASI UTAMA
# ==============================================================================
def render_sidebar():
    """Menampilkan panel navigasi samping dan profil siswa."""
    with st.sidebar:
        # Menampilkan Logo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(base_dir, "assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=90)
        else:
            st.markdown("### 🩺 ReproGuide")

        st.markdown("### **ReproGuide**")
        st.caption("Platform Edukasi Kesehatan Reproduksi Adaptif untuk Pelajar SMP")
        st.markdown("---")

        # Pengaturan Profil Singkat
        st.markdown("##### 👤 Profil Belajar")
        kelas_pilihan = st.selectbox(
            "Tingkat Kelas SMP:",
            options=[7, 8, 9],
            index=[7, 8, 9].index(st.session_state["user_class"]),
            format_func=lambda x: f"Kelas {x} SMP"
        )
        st.session_state["user_class"] = kelas_pilihan

        st.markdown("---")

        # Menu Navigasi Radio
        st.markdown("##### 🧭 Navigasi Menu")
        menu_options = [
            "Beranda",
            "Materi Pembelajaran",
            "Kuis",
            "Hasil Pembelajaran",
            "Tentang ReproGuide"
        ]

        current_index = menu_options.index(st.session_state["nav_page"]) if st.session_state["nav_page"] in menu_options else 0
        selected_menu = st.radio(
            "Pilih Menu:",
            options=menu_options,
            index=current_index,
            label_visibility="collapsed"
        )

        if selected_menu != st.session_state["nav_page"]:
            st.session_state["nav_page"] = selected_menu
            st.rerun()

        st.markdown("---")
        # Ringkasan Kuis Selesai
        selesai_count = sum(1 for v in st.session_state["quiz_submitted"].values() if v)
        st.markdown(f"**Progres Kuis:** {selesai_count} dari 5 Topik Selesai")
        st.progress(selesai_count / 5.0)

        # Tombol Cepat: Muat Contoh Nilai Simulasi (Sangat membantu pengujian demonstrasi)
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🧪 Tombol Pengujian Demo", expanded=False):
            st.caption("Isi nilai kuis secara otomatis untuk menguji prediksi Machine Learning dan Dashboard.")
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                if st.button("Nilai Bagus", use_container_width=True):
                    st.session_state["quiz_scores"] = {
                        "pubertas": 90,
                        "perubahan_tubuh": 80,
                        "kebersihan_menstruasi": 90,
                        "pencegahan_ims": 80,
                        "pencegahan_kekerasan_seksual": 100
                    }
                    for k in st.session_state["quiz_submitted"]:
                        st.session_state["quiz_submitted"][k] = True
                    st.success("Nilai tinggi terisi!")
                    st.rerun()
            with col_d2:
                if st.button("Nilai Cukup", use_container_width=True):
                    st.session_state["quiz_scores"] = {
                        "pubertas": 60,
                        "perubahan_tubuh": 70,
                        "kebersihan_menstruasi": 50,
                        "pencegahan_ims": 60,
                        "pencegahan_kekerasan_seksual": 70
                    }
                    for k in st.session_state["quiz_submitted"]:
                        st.session_state["quiz_submitted"][k] = True
                    st.info("Nilai sedang terisi!")
                    st.rerun()

            if st.button("Atur Ulang Semua Nilai", use_container_width=True):
                for k in st.session_state["quiz_scores"]:
                    st.session_state["quiz_scores"][k] = 0
                    st.session_state["quiz_submitted"][k] = False
                    st.session_state["quiz_answers"][k] = {}
                    st.session_state["quiz_current_q"][k] = 0
                st.warning("Semua nilai diatur ulang ke 0.")
                st.rerun()


# ==============================================================================
# HALAMAN 1: BERANDA
# ==============================================================================
def render_beranda():
    """Menampilkan halaman utama ReproGuide."""
    # Banner Hero
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">🩺 Selamat Datang di ReproGuide</div>
        <div class="hero-subtitle">
            Platform Pembelajaran Kesehatan Reproduksi Adaptif yang Ramah, Ilmiah, dan Mudah Dipahami untuk Pelajar SMP.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Pengantar Singkat
    col_intro1, col_intro2 = st.columns([3, 2])
    with col_intro1:
        st.markdown("### Mengapa Kesehatan Reproduksi Itu Penting?")
        st.write(
            "Memasuki masa remaja (pubertas), tubuh kita mengalami berbagai perubahan yang wajar dan menakjubkan. "
            "Namun, sering kali informasi di internet membingungkan atau bahkan keliru. "
            "**ReproGuide** hadir sebagai ruang belajar yang aman dan terpercaya tanpa stigma, "
            "membantu kamu mengenali perubahan diri, menjaga kebersihan dan kesehatan tubuh, serta melindungi diri dari bahaya."
        )

        st.markdown("""
        <div class="highlight-box">
            <b>🌟 Ciri Khas ReproGuide:</b>
            <ul>
                <li><b>Bahasa Sederhana:</b> Menggunakan istilah sehari-hari tanpa istilah asing yang rumit.</li>
                <li><b>Materi Teruji:</b> Berpedoman pada sumber resmi Kementerian Kesehatan RI, WHO, dan UNICEF.</li>
                <li><b>Rekomendasi Pintar:</b> Dilengkapi Decision Tree Machine Learning yang menyesuaikan saran belajar sesuai kemampuanmu.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("📖 Mulai Baca Materi", use_container_width=True):
                st.session_state["nav_page"] = "Materi Pembelajaran"
                st.rerun()
        with col_b2:
            if st.button("✏️ Kerjakan Kuis Evaluasi", use_container_width=True):
                st.session_state["nav_page"] = "Kuis"
                st.rerun()

    with col_intro2:
        st.markdown("### 📊 Status Belajarmu")
        st.markdown(f"**Tingkat:** Kelas {st.session_state['user_class']} SMP")
        selesai_count = sum(1 for v in st.session_state["quiz_submitted"].values() if v)
        st.metric(label="Kuis yang Diselesaikan", value=f"{selesai_count} / 5 Topik")

        # Rata-rata skor saat ini
        skor_list = list(st.session_state["quiz_scores"].values())
        rata_rata = sum(skor_list) / max(1, len(skor_list)) if selesai_count > 0 else 0
        st.metric(label="Rata-rata Skor Kuis", value=f"{rata_rata:.1f} Poin")

        if selesai_count > 0:
            if st.button("Lihat Rapor Hasil Pembelajaran", use_container_width=True):
                st.session_state["nav_page"] = "Hasil Pembelajaran"
                st.rerun()

    st.markdown("---")

    # Kartu Lima Topik Pembelajaran Utama
    st.markdown("### 📚 5 Topik Pembelajaran Utama")
    st.write("Klik tombol pada masing-masing topik untuk langsung membaca materi:")

    topics = get_all_topics()
    cols = st.columns(len(topics))

    for idx, topic in enumerate(topics):
        with cols[idx]:
            topic_score = st.session_state["quiz_scores"].get(topic["id"], 0)
            is_done = st.session_state["quiz_submitted"].get(topic["id"], False)

            status_badge = (
                f"<span class='badge badge-success'>Skor: {topic_score}</span>"
                if is_done
                else "<span class='badge badge-info'>Belum Tes</span>"
            )

            st.markdown(f"""
            <div class="content-card" style="min-height: 250px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{'🌱' if idx==0 else '🧍' if idx==1 else '🧼' if idx==2 else '🛡️' if idx==3 else '🤝'}</div>
                <div style="font-weight: 700; font-size: 1.05rem; color: #1E88E5; margin-bottom: 0.3rem;">Topik {topic['nomor']}</div>
                <div style="font-weight: 600; font-size: 1rem; margin-bottom: 0.5rem; color: #1E293B;">{topic['judul'].split(':')[0]}</div>
                <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 0.8rem; line-height: 1.4;">
                    {topic['pengantar'][:110]}...
                </div>
                <div>{status_badge}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Baca Topik {topic['nomor']}", key=f"btn_read_{topic['id']}", use_container_width=True):
                st.session_state["selected_topic_material"] = topic["id"]
                st.session_state["nav_page"] = "Materi Pembelajaran"
                st.rerun()


# ==============================================================================
# HALAMAN 2: MATERI PEMBELAJARAN
# ==============================================================================
def render_materi():
    """Menampilkan modul 5 topik materi pembelajaran lengkap."""
    st.markdown("## 📖 Materi Pembelajaran Kesehatan Reproduksi")
    st.write("Pilih salah satu dari lima topik di bawah ini untuk mempelajari materinya secara mendalam:")

    topic_keys = list(MATERI_PEMBELAJARAN.keys())
    topic_labels = [
        f"Topik {MATERI_PEMBELAJARAN[k]['nomor']}: {MATERI_PEMBELAJARAN[k]['judul'].split(':')[0]}"
        for k in topic_keys
    ]

    # Tab pilihan topik
    active_idx = topic_keys.index(st.session_state["selected_topic_material"]) if st.session_state["selected_topic_material"] in topic_keys else 0
    selected_label = st.radio(
        "Pilih Topik Pembelajaran:",
        options=topic_labels,
        index=active_idx,
        horizontal=True
    )
    chosen_topic_id = topic_keys[topic_labels.index(selected_label)]
    st.session_state["selected_topic_material"] = chosen_topic_id

    topic_data = get_topic_by_id(chosen_topic_id)

    st.markdown("---")

    # Judul Topik & Pengantar
    st.markdown(f"### 📘 {topic_data['judul']}")
    st.info(f"💡 **Pengantar Singkat:** {topic_data['pengantar']}")

    # Tujuan Pembelajaran
    st.markdown("#### 🎯 Tujuan Pembelajaran")
    for tujuan in topic_data["tujuan"]:
        st.markdown(f"- {tujuan}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Penjelasan Materi
    st.markdown("#### 📝 Penjelasan Materi Lengkap")
    for section in topic_data["penjelasan"]:
        with st.expander(f"📌 {section['subjudul']}", expanded=True):
            st.markdown(section["isi"])

    # Poin Penting
    st.markdown("#### ⭐ Poin-Poin Penting yang Wajib Diingat")
    poin_html = "<ul>" + "".join([f"<li>{p}</li>" for p in topic_data["poin_penting"]]) + "</ul>"
    st.markdown(f"""
    <div class="highlight-box">
        {poin_html}
    </div>
    """, unsafe_allow_html=True)

    # Ringkasan Topik
    st.markdown("#### 📋 Ringkasan Topik")
    st.success(topic_data["ringkasan"])

    # Referensi Sumber
    st.markdown("#### 📚 Sumber Referensi Resmi")
    for ref in topic_data["referensi"]:
        st.caption(f"✓ {ref}")

    st.markdown("---")

    # Tombol Aksi Menuju Kuis
    col_k1, col_k2 = st.columns([2, 1])
    with col_k1:
        st.write("Sudah memahami materi ini? Uji pemahamanmu sekarang melalui kuis interaktif 10 soal!")
    with col_k2:
        if st.button(f"✏️ Kerjakan Kuis Topik {topic_data['nomor']}", use_container_width=True):
            st.session_state["selected_topic_quiz"] = chosen_topic_id
            st.session_state["nav_page"] = "Kuis"
            st.rerun()


# ==============================================================================
# HALAMAN 3: MODUL KUIS INTERAKTIF
# ==============================================================================
def render_kuis():
    """Menampilkan modul kuis interaktif 5 topik x 10 soal = 50 soal."""
    st.markdown("## ✏️ Kuis Evaluasi Pemahaman")
    st.write("Jawablah 10 pertanyaan pilihan ganda pada topik yang kamu pilih. Setiap jawaban benar bernilai 10 poin.")

    topic_keys = list(MATERI_PEMBELAJARAN.keys())
    topic_labels = [
        f"Topik {MATERI_PEMBELAJARAN[k]['nomor']}: {MATERI_PEMBELAJARAN[k]['judul'].split(':')[0]}"
        for k in topic_keys
    ]

    active_idx = topic_keys.index(st.session_state["selected_topic_quiz"]) if st.session_state["selected_topic_quiz"] in topic_keys else 0
    selected_label = st.radio(
        "Pilih Topik Kuis:",
        options=topic_labels,
        index=active_idx,
        horizontal=True
    )
    topic_id = topic_keys[topic_labels.index(selected_label)]
    st.session_state["selected_topic_quiz"] = topic_id

    soal_list = get_quiz_by_topic(topic_id)
    total_soal = len(soal_list)

    is_submitted = st.session_state["quiz_submitted"].get(topic_id, False)

    st.markdown("---")

    # JIKA KUIS SUDAH DISELESAIKAN: TAMPILKAN HASIL & PEMBAHASAN LENGKAP
    if is_submitted:
        user_answers = st.session_state["quiz_answers"].get(topic_id, {})
        hasil = calculate_topic_score(topic_id, user_answers)

        st.markdown(f"### 🎉 Hasil Kuis: {TOPIC_TITLES.get(topic_id, topic_id)}")

        # Kartu Skor Ringkas
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Nilai Akhir", f"{hasil['skor']} / 100")
        with c2:
            st.metric("Jawaban Benar", f"{hasil['benar']} Soal")
        with c3:
            st.metric("Jawaban Salah", f"{hasil['salah']} Soal")
        with c4:
            st.metric("Kategori", hasil["kategori"])

        # Kategori pemahaman badge
        badge_type = (
            "badge-success" if hasil["skor"] >= 76 else "badge-warning" if hasil["skor"] >= 51 else "badge-danger"
        )
        st.markdown(f"""
        <div style="margin: 1rem 0;">
            <b>Kategori Hasil:</b> <span class="badge {badge_type}">{hasil['kategori']}</span>
        </div>
        """, unsafe_allow_html=True)

        # Rekomendasi singkat berdasarkan nilai
        rec = get_recommendation_for_score(hasil["skor"])
        st.info(f"💡 **Saran Belajar:** {rec['pesan']}")

        # Pembahasan Soal
        st.markdown("#### 📖 Pembahasan Lengkap Setiap Soal")
        for idx, d in enumerate(hasil["detail"]):
            status_simbol = "✅ Benar" if d["is_correct"] else "❌ Kurang Tepat"
            with st.expander(f"Soal {idx+1}: {d['pertanyaan'][:70]}... — ({status_simbol})", expanded=(not d["is_correct"])):
                st.markdown(f"**Pertanyaan:** {d['pertanyaan']}")

                jawaban_user_idx = d["jawaban_pengguna"]
                jawaban_user_txt = d["pilihan"][jawaban_user_idx] if jawaban_user_idx is not None else "Tidak dijawab"
                jawaban_benar_txt = d["pilihan"][d["jawaban_benar"]]

                st.write(f"👉 **Jawabanmu:** {jawaban_user_txt}")
                st.write(f"🎯 **Jawaban Benar:** {jawaban_benar_txt}")
                st.markdown(f"💡 **Penjelasan Medis & Ilmiah:** {d['penjelasan']}")

        st.markdown("---")
        col_act1, col_act2 = st.columns(2)
        with col_act1:
            if st.button("🔄 Ulangi Kuis Topik Ini", use_container_width=True):
                st.session_state["quiz_submitted"][topic_id] = False
                st.session_state["quiz_answers"][topic_id] = {}
                st.session_state["quiz_current_q"][topic_id] = 0
                st.rerun()
        with col_act2:
            if st.button("📊 Lihat Dashboard Hasil Lengkap", use_container_width=True):
                st.session_state["nav_page"] = "Hasil Pembelajaran"
                st.rerun()

        return

    # JIKA KUIS SEDANG BERJALAN: TAMPILKAN SOAL SATU PER SATU
    curr_q_idx = st.session_state["quiz_current_q"].get(topic_id, 0)
    if curr_q_idx >= total_soal:
        curr_q_idx = total_soal - 1
        st.session_state["quiz_current_q"][topic_id] = curr_q_idx

    soal = soal_list[curr_q_idx]

    # Indikator Kemajuan
    st.markdown(f"#### Soal {curr_q_idx + 1} dari {total_soal}")
    progres_val = (curr_q_idx + 1) / total_soal
    st.progress(progres_val)

    # Kotak Soal
    st.markdown(f"""
    <div class="content-card">
        <h4 style="color: #0F172A; line-height: 1.5; margin-bottom: 1rem;">
            {curr_q_idx + 1}. {soal['pertanyaan']}
        </h4>
    </div>
    """, unsafe_allow_html=True)

    # Pilihan Jawaban
    existing_ans = st.session_state["quiz_answers"][topic_id].get(curr_q_idx, None)

    pilihan_terpilih = st.radio(
        "Pilih satu jawaban yang paling tepat:",
        options=list(range(len(soal["pilihan"]))),
        format_func=lambda i: soal["pilihan"][i],
        index=existing_ans,
        key=f"radio_{topic_id}_{curr_q_idx}"
    )

    # Simpan jawaban saat ini jika pengguna telah memilih
    if pilihan_terpilih is not None:
        st.session_state["quiz_answers"][topic_id][curr_q_idx] = pilihan_terpilih

    # Tombol Navigasi Antarsoal
    col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])

    with col_nav1:
        if curr_q_idx > 0:
            if st.button("⬅️ Soal Sebelumnya", use_container_width=True):
                st.session_state["quiz_current_q"][topic_id] -= 1
                st.rerun()

    with col_nav3:
        if curr_q_idx < total_soal - 1:
            if st.button("Soal Berikutnya ➡️", use_container_width=True):
                # Validasi: Pengguna harus menjawab sebelum melanjutkan
                if st.session_state["quiz_answers"][topic_id].get(curr_q_idx) is None:
                    st.warning("⚠️ Silakan pilih salah satu jawaban terlebih dahulu sebelum melanjutkan!")
                else:
                    st.session_state["quiz_current_q"][topic_id] += 1
                    st.rerun()
        else:
            if st.button("✅ Selesai & Kirim Jawaban", use_container_width=True):
                # Validasi: Soal terakhir juga harus dijawab
                if st.session_state["quiz_answers"][topic_id].get(curr_q_idx) is None:
                    st.warning("⚠️ Silakan pilih salah satu jawaban terlebih dahulu untuk menyelesaikan kuis!")
                else:
                    # Hitung dan simpan skor
                    hasil = calculate_topic_score(topic_id, st.session_state["quiz_answers"][topic_id])
                    st.session_state["quiz_scores"][topic_id] = hasil["skor"]
                    st.session_state["quiz_submitted"][topic_id] = True
                    st.success("Jawaban kuis berhasil dikirim! Menampilkan pembahasan...")
                    st.rerun()


# ==============================================================================
# HALAMAN 4: HASIL PEMBELAJARAN & PREDIKSI MACHINE LEARNING
# ==============================================================================
def render_hasil():
    """Menampilkan dashboard hasil belajar, grafik radar/bar, dan prediksi CART Decision Tree."""
    st.markdown("## 📊 Rapor & Hasil Pembelajaran Adaptif")
    st.write(
        "Halaman ini merangkum capaian evaluasimu dari seluruh topik pembelajaran, "
        "menganalisis profil pemahaman menggunakan algoritma Decision Tree (CART), "
        "dan memberikan rekomendasi belajar yang disesuaikan secara personal."
    )

    scores_dict = st.session_state["quiz_scores"]
    user_class = st.session_state["user_class"]

    # Jalankan Prediksi Decision Tree jika model tersedia
    ml_pred = None
    if st.session_state.get("ml_ready", False) and st.session_state.get("ml_classifier"):
        clf = st.session_state["ml_classifier"]
        fitur_input = {
            "kelas": user_class,
            "skor_pubertas": scores_dict.get("pubertas", 0),
            "skor_perubahan_tubuh": scores_dict.get("perubahan_tubuh", 0),
            "skor_kebersihan_menstruasi": scores_dict.get("kebersihan_menstruasi", 0),
            "skor_pencegahan_ims": scores_dict.get("pencegahan_ims", 0),
            "skor_pencegahan_kekerasan_seksual": scores_dict.get("pencegahan_kekerasan_seksual", 0),
        }
        ml_pred = clf.predict(fitur_input)

    # Analisis profil pembelajaran
    profil = analyze_learning_profile(scores_dict, ml_pred, user_class)

    # 1. KARTU RINGKASAN METRIK UTAMA
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">Kelas {user_class}</div>
            <div class="metric-label">Tingkat Pendidikan SMP</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{profil['rata_rata']}</div>
            <div class="metric-label">Rata-rata Skor Keseluruhan</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        top_name = profil["topik_tertinggi"]["judul"].split(":")[0] if profil["topik_tertinggi"] else "-"
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value" style="font-size: 1.3rem; color: #2E7D32;">{top_name}</div>
            <div class="metric-label">Topik Paling Dikuasai</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        low_name = profil["topik_terendah"]["judul"].split(":")[0] if profil["topik_terendah"] else "-"
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value" style="font-size: 1.3rem; color: #E65100;">{low_name}</div>
            <div class="metric-label">Topik Perlu Ditingkatkan</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. GRAFIK PERBANDINGAN NILAI LIMA TOPIK
    st.markdown("### 📈 Grafik Perbandingan Nilai 5 Topik")
    col_chart1, col_chart2 = st.columns([3, 2])

    with col_chart1:
        # Bar Chart Nilai per Topik
        chart_data = pd.DataFrame([
            {"Topik": t["judul"].split(":")[0], "Skor": t["skor"], "Status": t["status"]}
            for t in profil["detail_per_topik"]
        ])

        fig_bar = px.bar(
            chart_data,
            x="Topik",
            y="Skor",
            color="Skor",
            color_continuous_scale=["#EF5350", "#FFA726", "#66BB6A"],
            range_y=[0, 105],
            text="Skor",
            title="Nilai Kuis Setiap Topik Pembelajaran"
        )
        fig_bar.update_layout(
            font=dict(family="Plus Jakarta Sans", size=12),
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_chart2:
        # Radar Chart Profil Kompetensi
        categories = [t["judul"].split(":")[0] for t in profil["detail_per_topik"]]
        r_values = [t["skor"] for t in profil["detail_per_topik"]]
        # Tutup polygon
        categories_closed = categories + [categories[0]]
        r_values_closed = r_values + [r_values[0]]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=r_values_closed,
            theta=categories_closed,
            fill='toself',
            fillcolor='rgba(30, 136, 229, 0.25)',
            line=dict(color='#1E88E5', width=2),
            name="Profil Siswa"
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            showlegend=False,
            title="Radar Kompetensi",
            font=dict(family="Plus Jakarta Sans", size=11),
            margin=dict(l=30, r=30, t=40, b=30)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")

    # 3. KARTU HASIL PREDIKSI MACHINE LEARNING (DECISION TREE CART)
    st.markdown("### 🤖 Klasifikasi Tingkat Pemahaman (Machine Learning)")
    st.write(
        "Sistem ReproGuide menggunakan model **Decision Tree (CART)** yang dilatih dengan dataset simulasi "
        "untuk mengklasifikasikan pola pemahaman ke dalam tiga kategori: **Rendah**, **Sedang**, atau **Tinggi**."
    )

    if ml_pred:
        kategori_pred = ml_pred["kategori_prediksi"]
        prob = ml_pred.get("probabilitas", {})

        pred_badge_class = (
            "badge-success" if kategori_pred == "Tinggi" else "badge-warning" if kategori_pred == "Sedang" else "badge-danger"
        )

        st.markdown(f"""
        <div class="content-card" style="border-left: 6px solid #1E88E5;">
            <h4>Hasil Prediksi Model Decision Tree: <span class="badge {pred_badge_class}">{kategori_pred}</span></h4>
            <p style="color: #475569; margin-top: 0.5rem;">{profil['ml_info']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Probabilitas Prediksi
        st.markdown("##### 🎯 Tingkat Keyakinan Prediksi (Probabilitas):")
        cols_prob = st.columns(3)
        for idx, (cat_name, p_val) in enumerate(prob.items()):
            with cols_prob[idx]:
                st.metric(f"Peluang {cat_name}", f"{p_val}%")
                st.progress(p_val / 100.0)

        # Penjelasan Aturan & Visualisasi Model Sederhana
        with st.expander("🔍 Lihat Informasi Teknis Model & Aturan Decision Tree", expanded=False):
            clf = st.session_state["ml_classifier"]
            info = clf.get_model_info()

            st.write(f"**Algoritma:** {info['algoritma']}")
            st.write(f"**Kriteria Evaluasi:** {info['kriteria_pemisahan']}")
            st.write(f"**Akurasi pada Data Uji Simulasi:** {info['metrik'].get('accuracy', 0)}%")
            st.write(f"**Jumlah Data Pelatihan:** {info['metrik'].get('total_latih', 0)} baris | **Data Uji:** {info['metrik'].get('total_uji', 0)} baris")

            st.markdown("##### Bobot Kepentingan Fitur (Feature Importance):")
            fi = info.get("fitur_penting", {})
            if fi:
                df_fi = pd.DataFrame([
                    {"Fitur": k.replace("skor_", "").replace("_", " ").title(), "Kepentingan": round(v * 100, 1)}
                    for k, v in fi.items()
                ]).sort_values("Kepentingan", ascending=True)

                fig_fi = px.bar(
                    df_fi,
                    x="Kepentingan",
                    y="Fitur",
                    orientation="h",
                    title="Kontribusi Fitur dalam Pengambilan Keputusan",
                    color="Kepentingan",
                    color_continuous_scale="Blues"
                )
                fig_fi.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=260)
                st.plotly_chart(fig_fi, use_container_width=True)

            st.markdown("##### Representasi Logika Percabangan Pohon Keputusan (CART):")
            st.code(info.get("aturan_pohon", ""), language="text")

    # Catatan Akademis Wajib
    st.markdown("""
    <div class="disclaimer-box">
        <b>⚠️ Catatan Transparansi Akademis & Simulasi:</b><br>
        Model Machine Learning ini dilatih menggunakan <i>dataset_simulasi.csv</i> (data sintetis yang dibuat khusus untuk pengembangan prototipe MVP 1.0).
        Hasil klasifikasi merupakan rekomendasi panduan edukasi dan <b>bukan diagnosis klinis medis</b>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 4. REKOMENDASI PEMBELAJARAN PER TOPIK
    st.markdown("### 💡 Rekomendasi Pembelajaran Adaptif Per Topik")
    st.write(
        "Rekomendasi di bawah ini disusun otomatis berdasarkan capaian skor pada masing-masing topik kuis:"
    )

    for item in profil["detail_per_topik"]:
        badge_class = (
            "badge-success" if item["skor"] >= 76 else "badge-warning" if item["skor"] >= 51 else "badge-danger"
        )
        st.markdown(f"""
        <div class="content-card" style="border-left: 5px solid {item['warna']};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <h4 style="margin: 0; color: #0F172A;">{item['judul']}</h4>
                <span class="badge {badge_class}">Skor: {item['skor']} / 100 — {item['status']}</span>
            </div>
            <p style="margin: 0.5rem 0; color: #334155; line-height: 1.5;">{item['pesan']}</p>
            <div style="background-color: #F8FAFC; padding: 0.6rem 0.8rem; border-radius: 6px; font-size: 0.9rem; color: #475569;">
                <b>Langkah Disarankan:</b> {item['tindakan']} &bull; <i>{item['fokus']}</i>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# HALAMAN 5: TENTANG REPROGUIDE & DOKUMENTASI SISTEM
# ==============================================================================
def render_tentang():
    """Menampilkan informasi lengkap mengenai aplikasi ReproGuide, metodologi, dan tim pengembang."""
    st.markdown("## ℹ️ Tentang ReproGuide")
    st.caption("Adaptive Reproductive Health Education Platform MVP 1.0")

    col_t1, col_t2 = st.columns([3, 2])
    with col_t1:
        st.markdown("### 🎯 Visi & Tujuan")
        st.write(
            "**ReproGuide** adalah inovasi platform pendidikan kesehatan reproduksi yang dirancang khusus "
            "untuk memenuhi kebutuhan pelajar Sekolah Menengah Pertama (SMP kelas 7, 8, dan 9) di Indonesia. "
            "Kesehatan reproduksi sering kali dianggap sebagai topik yang tabu dibicarakan, "
            "sehingga banyak remaja memperoleh informasi yang salah dan tidak aman dari sumber yang tidak jelas."
        )

        st.write(
            "Melalui ReproGuide, materi disampaikan dengan bahasa Indonesia yang bersahabat, santun, tidak menghakimi, "
            "dan berlandaskan fakta medis yang sah. Aplikasi ini mengintegrasikan evaluasi interaktif dan "
            "teknologi Machine Learning untuk memetakan pemahaman dan memberikan panduan belajar secara personal."
        )

    with col_t2:
        st.markdown("""
        <div class="content-card">
            <h4>📌 Identitas Sistem</h4>
            <p><b>Nama Platform:</b> ReproGuide</p>
            <p><b>Nama Panjang:</b> Adaptive Reproductive Health Education Platform</p>
            <p><b>Versi:</b> 1.0 (Minimum Viable Product - MVP)</p>
            <p><b>Target Pengguna:</b> Siswa SMP Kelas 7, 8, dan 9</p>
            <p><b>Bahasa Antarmuka:</b> 100% Bahasa Indonesia</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Landasan Materi & Sumber Ilmiah
    st.markdown("### 🏛️ Landasan Pedoman Edukatif & Medis")
    st.write(
        "Seluruh materi dalam ReproGuide disaring secara teliti agar sesuai dengan psikologi dan perkembangan "
        "kognitif remaja, bersumber dari panduan resmi lembaga kesehatan terkemuka:"
    )

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown("""
        <div class="content-card">
            <h4>🇮🇩 Kemenkes RI</h4>
            <p style="font-size: 0.9rem; color: #475569;">
                Pedoman Pelayanan Kesehatan Peduli Remaja (PKPR) dan Buku Saku Kesehatan Reproduksi Remaja Indonesia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_s2:
        st.markdown("""
        <div class="content-card">
            <h4>🌐 WHO</h4>
            <p style="font-size: 0.9rem; color: #475569;">
                World Health Organization Guidelines on Adolescent Reproductive Health and Rights.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_s3:
        st.markdown("""
        <div class="content-card">
            <h4>🤝 UNICEF</h4>
            <p style="font-size: 0.9rem; color: #475569;">
                Panduan Manajemen Kebersihan Menstruasi dan Sanitasi Sekolah di Indonesia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Arsitektur Teknologi & Machine Learning
    st.markdown("### ⚙️ Arsitektur Teknologi & Algoritma")
    st.markdown("""
    - **Bahasa Pemrograman:** Python 3.9+
    - **Kerangka Antarmuka (Web Framework):** Streamlit
    - **Pengolahan & Manajemen Data:** Pandas
    - **Visualisasi Data:** Plotly Express & Plotly Graph Objects
    - **Model Machine Learning:** Scikit-learn `DecisionTreeClassifier` dengan algoritma **CART** (Classification and Regression Trees).
    - **Kriteria Pemisahan Node:** Gini Impurity
    - **Manajemen Sesi:** Streamlit `session_state` (tanpa ketergantungan database eksternal ataupun token API berbayar).
    """)

    st.markdown("---")

    # Batasan MVP 1.0
    st.markdown("### 🛡️ Batasan Pengembangan Versi MVP 1.0")
    st.write(
        "Sesuai dengan ruang lingkup demonstrasi prototipe MVP 1.0, beberapa batasan sistem berlaku:"
    )
    st.markdown("""
    1. **Data Simulasi Sintetis:** Dataset pelatihan (`dataset_simulasi.csv`) merupakan 300 baris data sintetis terstruktur untuk membuktikan fungsi model CART, bukan sampel rekam medis riil.
    2. **Penyimpanan Sesi (In-Memory):** Progres evaluasi disimpan selama sesi peramban aktif menggunakan `session_state`.
    3. **Privasi Siswa:** Aplikasi tidak meminta data pribadi seperti nama lengkap, NISN, atau alamat untuk menjaga kerahasiaan anak.
    4. **Saran Non-Klinis:** Rekomendasi belajar ditujukan untuk tujuan pengayaan edukasi dan literasi, bukan tindakan medis.
    """)


# ==============================================================================
# ROUTER APLIKASI
# ==============================================================================
def main():
    # Konfigurasi Halaman (Harus menjadi perintah Streamlit pertama)
    st.set_page_config(
        page_title="ReproGuide - Edukasi Kesehatan Reproduksi Adaptif",
        page_icon="🩺",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    init_session_state()
    render_sidebar()

    current_page = st.session_state["nav_page"]
    if current_page == "Beranda":
        render_beranda()
    elif current_page == "Materi Pembelajaran":
        render_materi()
    elif current_page == "Kuis":
        render_kuis()
    elif current_page == "Hasil Pembelajaran":
        render_hasil()
    elif current_page == "Tentang ReproGuide":
        render_tentang()
    else:
        render_beranda()


if __name__ == "__main__":
    main()
