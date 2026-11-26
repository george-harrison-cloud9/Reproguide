"""
Modul Kuis ReproGuide
Menyediakan bank soal lengkap (5 topik x 10 soal = 50 soal pilihan ganda),
sistem penilaian, dan fungsi pendukung evaluasi pembelajaran.
"""

BANK_SOAL = {
    # ----------------------------------------------------
    # TOPIK 1: PUBERTAS (10 SOAL)
    # ----------------------------------------------------
    "pubertas": [
        {
            "id": 1,
            "pertanyaan": "Apa pengertian yang paling tepat mengenai masa pubertas?",
            "pilihan": [
                "A. Tahap transisi alami dari masa anak-anak menuju kedewasaan dan kematangan reproduksi",
                "B. Penyakit musiman yang dialami semua anak berusia belasan tahun",
                "C. Proses berhentinya pertumbuhan fisik dan mental pada manusia",
                "D. Masa di mana seseorang tidak lagi memerlukan bimbingan orang tua"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Pubertas adalah tahap perkembangan alami ketika organ reproduksi mulai matang dan tubuh bertumbuh dari masa anak-anak menuju kedewasaan."
        },
        {
            "id": 2,
            "pertanyaan": "Berapakah rentang usia umum dimulainya masa pubertas pada anak perempuan?",
            "pilihan": [
                "A. 5 hingga 8 tahun",
                "B. 9 hingga 14 tahun",
                "C. 16 hingga 20 tahun",
                "D. 21 hingga 25 tahun"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Pada anak perempuan, masa pubertas umumnya dimulai pada rentang usia 9 hingga 14 tahun, dipengaruhi oleh faktor keturunan dan nutrisi."
        },
        {
            "id": 3,
            "pertanyaan": "Berapakah rentang usia umum dimulainya masa pubertas pada anak laki-laki?",
            "pilihan": [
                "A. 6 hingga 8 tahun",
                "B. 10 hingga 15 tahun",
                "C. 18 hingga 22 tahun",
                "D. 23 hingga 27 tahun"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Pada anak laki-laki, masa pubertas umumnya dimulai sedikit lebih lambat dari perempuan, yaitu pada usia 10 hingga 15 tahun."
        },
        {
            "id": 4,
            "pertanyaan": "Hormon utama yang memicu perubahan fisik pada anak laki-laki saat pubertas adalah...",
            "pilihan": [
                "A. Insulin",
                "B. Melatonin",
                "C. Testosteron",
                "D. Tiroksin"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Testosteron diproduksi oleh testis dan merupakan hormon utama yang memicu perubahan fisik pada remaja laki-laki, seperti suara membesar dan pertumbuhan otot."
        },
        {
            "id": 5,
            "pertanyaan": "Hormon utama yang memicu perkembangan fisik dan siklus menstruasi pada remaja perempuan adalah...",
            "pilihan": [
                "A. Estrogen dan Progesteron",
                "B. Adrenalin dan Dopamin",
                "C. Glukagon dan Kortisol",
                "D. Oksitosin dan Serotonin"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Estrogen dan progesteron diproduksi oleh ovarium dan berperan penting dalam pembentukan payudara serta pengaturan siklus haid perempuan."
        },
        {
            "id": 6,
            "pertanyaan": "Mengapa setiap remaja mengalami awal pubertas pada usia yang berbeda-beda?",
            "pilihan": [
                "A. Karena beberapa anak tidak memiliki hormon pertumbuhan",
                "B. Karena dipengaruhi faktor genetik (keturunan), asupan gizi, dan kondisi kesehatan",
                "C. Karena ada anak yang lupa mengalami pubertas",
                "D. Karena hanya ditentukan oleh jenis olahraga yang disukai"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Perbedaan waktu mulainya pubertas sangat normal karena setiap orang memiliki latar belakang genetik, pola makan, dan kondisi tubuh yang unik."
        },
        {
            "id": 7,
            "pertanyaan": "Bagian otak yang bertugas memberikan sinyal pertama untuk memulai proses pubertas adalah...",
            "pilihan": [
                "A. Kelenjar Hipofisis (Pituitari)",
                "B. Saraf sensorik mata",
                "C. Batang telinga",
                "D. Sumsum tulang belakang"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Kelenjar hipofisis di dasar otak mengeluarkan hormon sinyal (LH dan FSH) yang memicu kelenjar reproduksi mulai aktif berproduksi."
        },
        {
            "id": 8,
            "pertanyaan": "Perubahan emosi berupa perasaan yang cepat berubah (mood swing) saat pubertas disebabkan oleh...",
            "pilihan": [
                "A. Penyakit mental berbahaya",
                "B. Kurangnya minum air es",
                "C. Pengaruh lonjakan dan penyesuaian hormon dalam tubuh",
                "D. Hukuman atas perbuatan masa kecil"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Perubahan kadar hormon yang cepat selama pubertas dapat memengaruhi sistem saraf dan suasana hati, yang merupakan hal wajar dalam masa penyesuaian diri."
        },
        {
            "id": 9,
            "pertanyaan": "Sikap terbaik yang perlu diambil saat menghadapi perubahan fisik pada diri sendiri saat pubertas adalah...",
            "pilihan": [
                "A. Mengurung diri di kamar karena merasa malu",
                "B. Membanding-bandingkan bentuk tubuh dengan teman di media sosial",
                "C. Menerima diri dengan bersyukur dan merawat kebersihan tubuh secara teratur",
                "D. Mencoba berbagai obat keras tanpa resep dokter"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Menerima perubahan diri dengan rasa syukur, menjaga kebersihan, dan menerapkan pola hidup sehat adalah sikap bijak menghadapi pubertas."
        },
        {
            "id": 10,
            "pertanyaan": "Jika kamu merasa cemas atau bingung dengan perubahan tubuhmu, kepada siapa sebaiknya kamu bertanya?",
            "pilihan": [
                "A. Orang asing yang baru dikenal di internet",
                "B. Orang tua, guru BK, atau tenaga medis profesional yang tepercaya",
                "C. Akun anonim di media sosial tanpa identitas jelas",
                "D. Menyimpannya sendiri sampai menjadi beban pikiran"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Orang tua, guru BK, dan tenaga medis di puskesmas/klinik adalah pihak paling aman dan tepercaya untuk memberikan penjelasan kesehatan reproduksi."
        }
    ],

    # ----------------------------------------------------
    # TOPIK 2: PERUBAHAN TUBUH DAN REPRODUKSI (10 SOAL)
    # ----------------------------------------------------
    "perubahan_tubuh": [
        {
            "id": 1,
            "pertanyaan": "Apa yang dimaksud dengan ciri-ciri kelamin primer?",
            "pilihan": [
                "A. Perubahan warna rambut dan gaya berpakaian",
                "B. Perubahan yang berkaitan langsung dengan fungsi organ reproduksi",
                "C. Tinggi badan yang bertambah drastis",
                "D. Nilai pelajaran di sekolah yang meningkat"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Ciri kelamin primer adalah pematangan organ internal yang langsung berfungsi untuk proses reproduksi (pembentukan sperma atau sel telur)."
        },
        {
            "id": 2,
            "pertanyaan": "Berikut ini yang merupakan ciri kelamin primer pada remaja laki-laki adalah...",
            "pilihan": [
                "A. Testis mulai memproduksi sperma (ditandai dengan mimpi basah)",
                "B. Tumbuh kumis dan jenggot di wajah",
                "C. Suara menjadi lebih rendah dan berat",
                "D. Jakun mulai terlihat menonjol di leher"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Mulai diproduksinya sel sperma oleh testis adalah ciri primer, sedangkan suara membesar dan kumis adalah ciri kelamin sekunder."
        },
        {
            "id": 3,
            "pertanyaan": "Berikut ini yang merupakan ciri kelamin primer pada remaja perempuan adalah...",
            "pilihan": [
                "A. Pinggul mulai membesar",
                "B. Kulit menjadi lebih halus",
                "C. Terjadinya menstruasi pertama (menarche) akibat ovulasi",
                "D. Tumbuh rambut halus di sekitar ketiak"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Menarche (menstruasi pertama) menandakan bahwa ovarium telah mulai mematangkan dan melepaskan sel telur, yang merupakan ciri kelamin primer."
        },
        {
            "id": 4,
            "pertanyaan": "Mengapa suara remaja laki-laki menjadi lebih berat dan dalam saat pubertas?",
            "pilihan": [
                "A. Karena pita suara dan laring (kotak suara) membesar di bawah pengaruh hormon testosteron",
                "B. Karena saluran pernapasan menyempit",
                "C. Karena terlalu sering bernyanyi lagu bernada rendah",
                "D. Karena batuk yang tidak kunjung sembuh"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Laring membesar dan pita suara menebal di bawah pengaruh testosteron, menghasilkan getaran suara yang lebih rendah (suara lebih berat) dan menonjolnya jakun."
        },
        {
            "id": 5,
            "pertanyaan": "Apakah mimpi basah pada remaja laki-laki merupakan tanda penyakit atau kelainan?",
            "pilihan": [
                "A. Ya, itu adalah tanda adanya infeksi organ dalam",
                "B. Tidak, mimpi basah adalah proses biologis alami dan sehat pengeluaran kelebihan sperma",
                "C. Ya, karena hanya terjadi pada orang yang kurang tidur",
                "D. Ya, dan harus segera diobati dengan antibiotik keras"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Mimpi basah adalah mekanisme biologis alami tubuh laki-laki untuk mengeluarkan tumpukan cairan sperma yang diproduksi secara teratur saat tidur."
        },
        {
            "id": 6,
            "pertanyaan": "Manakah di bawah ini yang merupakan ciri kelamin sekunder pada perempuan?",
            "pilihan": [
                "A. Menarche (haid pertama)",
                "B. Pelepasan sel telur oleh ovarium",
                "C. Payudara mulai membesar dan pinggul melebar",
                "D. Pembentukan dinding rahim"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Pembesaran payudara dan pelebaran pinggul merupakan ciri fisik luar (sekunder) yang dipicu oleh hormon estrogen."
        },
        {
            "id": 7,
            "pertanyaan": "Apa penyebab munculnya jerawat dan bau badan yang lebih menyengat pada masa pubertas?",
            "pilihan": [
                "A. Aktivitas kelenjar minyak (sebasea) dan kelenjar keringat (apokrin) meningkat pesat",
                "B. Terlalu banyak membaca buku pelajaran",
                "C. Kurang makan sayur dan buah semangka",
                "D. Udara di dalam kamar yang terlalu dingin"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Hormon pubertas merangsang kelenjar minyak dan keringat untuk berproduksi lebih aktif. Keringat yang bercampur bakteri kulit memicu bau badan dan pori-pori tersumbat memicu jerawat."
        },
        {
            "id": 8,
            "pertanyaan": "Organ reproduksi perempuan yang bertugas menghasilkan sel telur (ovum) adalah...",
            "pilihan": [
                "A. Uretra",
                "B. Ovarium (indung telur)",
                "C. Vagina",
                "D. Serviks"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Ovarium adalah sepasang kelenjar di panggul yang memproduksi serta melepaskan sel telur setiap bulannya."
        },
        {
            "id": 9,
            "pertanyaan": "Organ reproduksi laki-laki yang bertugas memproduksi sel sperma dan hormon testosteron adalah...",
            "pilihan": [
                "A. Testis",
                "B. Kantung kemih",
                "C. Ginjal",
                "D. Hati"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Testis yang berada di dalam kantung skrotum berfungsi memproduksi sel sperma dan menyekresikan hormon testosteron."
        },
        {
            "id": 10,
            "pertanyaan": "Sikap 'body positivity' yang tepat terhadap perbedaan laju pertumbuhan tubuh antarteman adalah...",
            "pilihan": [
                "A. Menertawakan teman yang tubuhnya paling pendek di kelas",
                "B. Menghargai keberagaman bentuk tubuh dan tidak melakukan ejekan fisik (body shaming)",
                "C. Memaksa teman yang kurus untuk makan obat penambah berat badan",
                "D. Membuat lelucon tentang jakun atau tinggi badan teman"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Menghargai keragaman fisik dan menjauhi perundungan fisik (body shaming) menciptakan lingkungan pertemanan yang aman dan suportif bagi semua orang."
        }
    ],

    # ----------------------------------------------------
    # TOPIK 3: KEBERSIHAN DAN MENSTRUASI (10 SOAL)
    # ----------------------------------------------------
    "kebersihan_menstruasi": [
        {
            "id": 1,
            "pertanyaan": "Secara biologis, apakah yang menyebabkan keluarnya darah menstruasi?",
            "pilihan": [
                "A. Luka sobekan pada organ dalam akibat infeksi berat",
                "B. Luruhnya dinding bagian dalam rahim (endometrium) karena sel telur tidak dibuahi",
                "C. Pembuangan racun darah kotor sisa pencernaan makanan",
                "D. Reaksi alergi terhadap makanan pedas atau asam"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Jika sel telur tidak dibuahi oleh sperma, kadar hormon menurun sehingga lapisan dinding rahim yang dipersiapkan untuk kehamilan meluruh dan keluar sebagai darah haid."
        },
        {
            "id": 2,
            "pertanyaan": "Berapakah rentang panjang siklus menstruasi normal pada umumnya?",
            "pilihan": [
                "A. 5 hingga 10 hari",
                "B. 21 hingga 35 hari",
                "C. 50 hingga 75 hari",
                "D. 90 hingga 120 hari"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Panjang siklus menstruasi normal berkisar antara 21 sampai 35 hari, dihitung dari hari pertama haid hingga hari pertama haid siklus berikutnya."
        },
        {
            "id": 3,
            "pertanyaan": "Berapa jam sekali pembalut sebaiknya diganti untuk menjaga kebersihan dan mencegah kuman berkembang biak?",
            "pilihan": [
                "A. Setiap 4 hingga 5 jam sekali, atau lebih sering saat deras",
                "B. Cukup satu kali sehari pada malam hari",
                "C. Setiap 24 jam sekali saja",
                "D. Hanya diganti jika pembalut sudah benar-benar penuh meluap"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Pembalut wajib diganti tiap 4–5 jam sekali untuk menghindari kelembapan tinggi yang dapat menjadi sarang kuman dan bakteri penyebab iritasi."
        },
        {
            "id": 4,
            "pertanyaan": "Bagaimanakah arah membilas area kewanitaan yang benar setelah buang air atau mandi?",
            "pilihan": [
                "A. Dari arah belakang ke depan menuju vagina",
                "B. Dari arah depan ke belakang menuju anus",
                "C. Bolak-balik secara acak",
                "D. Tidak perlu dibilas dengan air sama sekali"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Membilas dari arah depan ke belakang mencegah bakteri dari anus (seperti E. coli) terbawa masuk ke saluran kemih atau vagina."
        },
        {
            "id": 5,
            "pertanyaan": "Mengapa tidak dianjurkan menggunakan sabun antiseptik wangi di dalam area intim wanita secara berlebihan?",
            "pilihan": [
                "A. Karena sabun wangi terlalu murah",
                "B. Karena dapat merusak keseimbangan pH alami dan membunuh bakteri baik pelindung",
                "C. Karena dapat mengubah warna kulit menjadi biru",
                "D. Karena membuat pakaian dalam menjadi kaku"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Area vagina memiliki flora normal (bakteri baik seperti Lactobacillus) yang menjaga keasaman alami. Sabun wangi keras dapat merusak keseimbangan ini sehingga memicu infeksi jamur."
        },
        {
            "id": 6,
            "pertanyaan": "Bahan pakaian dalam apakah yang paling direkomendasikan untuk kesehatan organ reproduksi?",
            "pilihan": [
                "A. Bahan sintetis plastik kedap udara",
                "B. Bahan katun yang mudah menyerap keringat dan memiliki sirkulasi udara baik",
                "C. Bahan nilon tebal yang tidak elastis",
                "D. Bahan wol tebal yang memerangkap panas"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Bahan katun menyerap keringat dengan baik, menjaga area reproduksi tetap kering, serta mencegah pertumbuhan jamur akibat kelembapan tinggi."
        },
        {
            "id": 7,
            "pertanyaan": "Bagaimana cara membuang pembalut bekas yang higienis dan bertanggung jawab?",
            "pilihan": [
                "A. Dibuang langsung ke dalam lubang kloset toilet",
                "B. Dibungkus rapat dengan kertas/plastik bekas lalu dibuang ke tempat sampah tertutup",
                "C. Dibuang sembarangan di sudut kamar mandi sekolah",
                "D. Dihanyutkan ke saluran air got dekat rumah"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Pembalut yang dibungkus rapi dan dibuang ke tempat sampah tertutup mencegah penyebaran kuman serta mencegah tersumbatnya saluran toilet."
        },
        {
            "id": 8,
            "pertanyaan": "Bagi laki-laki, mengapa penting membersihkan lipatan kulit organ kemaluan dengan air bersih setiap hari?",
            "pilihan": [
                "A. Agar terhindar dari penumpukan kotoran, keringat, dan bakteri (smegma) yang memicu bau dan infeksi",
                "B. Supaya kulit kemaluan menjadi lebih gelap",
                "C. Agar tidak perlu mandi selama beberapa hari berikutnya",
                "D. Karena disuruh oleh teman sebaya"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Pembersihan menyeluruh pada organ kemaluan laki-laki mencegah penumpukan sel kulit mati dan sekresi lemak (smegma) yang dapat menjadi sarang kuman."
        },
        {
            "id": 9,
            "pertanyaan": "Apakah mitos yang menyatakan bahwa perempuan saat menstruasi dilarang keramas atau mencuci rambut itu benar?",
            "pilihan": [
                "A. Benar, karena keramas saat haid dapat menyumbat pori-pori kepala",
                "B. Salah, keramas dan mandi saat haid justru sangat penting untuk menjaga kebersihan dan kenyamanan tubuh",
                "C. Benar, karena darah haid bisa naik ke kepala jika rambut basah",
                "D. Benar, sesuai aturan medis internasional"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Itu adalah mitos yang keliru. Menjaga kebersihan diri, termasuk keramas dan mandi teratur, sangat dianjurkan saat menstruasi agar tubuh tetap bersih dan bugar."
        },
        {
            "id": 10,
            "pertanyaan": "Kapan sebaiknya pakaian dalam diganti setiap harinya?",
            "pilihan": [
                "A. Cukup seminggu sekali",
                "B. Tiga hari sekali saat akhir pekan",
                "C. Minimal 2 kali sehari (setelah mandi) atau setiap kali terasa lembap/kotor",
                "D. Hanya diganti saat bepergian ke luar rumah"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Mengganti pakaian dalam minimal 2 kali sehari menjaga area intim tetap kering, segar, dan bebas dari kelembapan berlebih yang disukai jamur kulit."
        }
    ],

    # ----------------------------------------------------
    # TOPIK 4: PENCEGAHAN IMS (10 SOAL)
    # ----------------------------------------------------
    "pencegahan_ims": [
        {
            "id": 1,
            "pertanyaan": "Apakah kepanjangan dari singkatan IMS dalam konteks kesehatan reproduksi?",
            "pilihan": [
                "A. Infeksi Menular Seksual",
                "B. Ikatan Medis Siswa",
                "C. Imunisasi Menyeluruh Sekolah",
                "D. Informasi Makanan Sehat"
            ],
            "jawaban_benar": 0,
            "penjelasan": "IMS adalah singkatan dari Infeksi Menular Seksual, yaitu penyakit infeksi yang ditularkan terutama melalui kontak hubungan seksual berisiko."
        },
        {
            "id": 2,
            "pertanyaan": "Manakah di bawah ini yang merupakan contoh penyakit Infeksi Menular Seksual yang disebabkan oleh bakteri?",
            "pilihan": [
                "A. Cacar air dan influenza",
                "B. Sifilis (Raja Singa) dan Gonore (Kencing Nanah)",
                "C. Demam berdarah dan malaria",
                "D. Asma dan diabetes melitus"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Sifilis (Treponema pallidum) dan Gonore (Neisseria gonorrhoeae) adalah infeksi menular seksual yang disebabkan oleh bakteri patogen."
        },
        {
            "id": 3,
            "pertanyaan": "HIV adalah virus yang menyerang sistem apa di dalam tubuh manusia?",
            "pilihan": [
                "A. Sistem pencernaan lambung",
                "B. Sistem kekebalan tubuh (sel darah putih CD4)",
                "C. Sistem kerangka dan persendian",
                "D. Sistem penglihatan mata"
            ],
            "jawaban_benar": 1,
            "penjelasan": "HIV (Human Immunodeficiency Virus) merusak sel darah putih yang bertugas melawan kuman, sehingga daya tahan tubuh penderita perlahan-lahan menurun."
        },
        {
            "id": 4,
            "pertanyaan": "Apakah perbedaan antara infeksi HIV dan kondisi AIDS?",
            "pilihan": [
                "A. HIV adalah obat penyembuh untuk penderita AIDS",
                "B. HIV adalah virus penyebabnya, sedangkan AIDS adalah kumpulan gejala penyakit akibat penurunan daya tahan tubuh tahap lanjut",
                "C. HIV hanya menyerang orang tua, sedangkan AIDS hanya menyerang anak-anak",
                "D. Tidak ada perbedaan, keduanya adalah jenis bakteri yang sama"
            ],
            "jawaban_benar": 1,
            "penjelasan": "HIV adalah nama virusnya. Jika infeksi HIV tidak ditangani dengan obat antiretroviral (ARV), kondisi ini berkembang menjadi tahap akhir yang disebut AIDS."
        },
        {
            "id": 5,
            "pertanyaan": "Jalur manakah di bawah ini yang BUKAN merupakan cara penularan virus HIV?",
            "pilihan": [
                "A. Bersalaman, berpelukan, atau mengobrol bersama",
                "B. Hubungan seksual berisiko tanpa pengaman",
                "C. Pemakaian jarum suntik secara bergantian",
                "D. Penularan dari ibu terinfeksi HIV ke janin tanpa penanganan medis"
            ],
            "jawaban_benar": 0,
            "penjelasan": "HIV TIDAK menular melalui kontak sosial biasa seperti bersalaman, berpelukan, batuk, bersin, atau menggunakan peralatan makan bersama."
        },
        {
            "id": 6,
            "pertanyaan": "Apakah gigitan nyamuk dapat menularkan virus HIV dari satu orang ke orang lain?",
            "pilihan": [
                "A. Ya, karena nyamuk menghisap darah manusia",
                "B. Tidak, virus HIV tidak dapat hidup atau berkembang biak di dalam tubuh nyamuk",
                "C. Ya, terutama pada musim hujan lebat",
                "D. Ya, jika nyamuknya berukuran sangat besar"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Secara ilmiah terbukti nyamuk tidak dapat menularkan HIV. Virus tersebut cepat hancur di sistem pencernaan nyamuk dan nyamuk tidak menyuntikkan darah orang lain."
        },
        {
            "id": 7,
            "pertanyaan": "Bagi pelajar tingkat SMP, langkah pencegahan IMS yang paling efektif dan bijak adalah...",
            "pilihan": [
                "A. Tidak melakukan aktivitas seksual berisiko (Abstinence) dan fokus pada pendidikan masa depan",
                "B. Minum obat antibiotik sembarangan setiap minggu",
                "C. Menghindari berbicara dengan teman sekolah",
                "D. Menggunakan lotion pelembap kulit setiap malam"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Abstinensia (menunda aktivitas seksual sampai dewasa dan menikah) adalah cara 100% efektif bagi remaja untuk mencegah IMS dan kehamilan di usia dini."
        },
        {
            "id": 8,
            "pertanyaan": "Selain hubungan seksual berisiko, perilaku apa lagi yang sangat berisiko menularkan IMS dan HIV?",
            "pilihan": [
                "A. Berolahraga lari maraton bersama teman",
                "B. Penggunaan jarum suntik tato atau narkoba suntik secara bergantian dan tidak steril",
                "C. Membaca buku bersama di perpustakaan sekolah",
                "D. Minum air putih yang dimasak hingga mendidih"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Jarum suntik yang tercemar darah penderita menjadi media langsung masuknya virus HIV atau hepatitis B/C ke pembuluh darah orang lain."
        },
        {
            "id": 9,
            "pertanyaan": "Bagaimanakah sikap yang tepat terhadap Orang dengan HIV/AIDS (ODHA) di lingkungan sosial?",
            "pilihan": [
                "A. Menjauhi, mengucilkan, dan menyebarkan berita buruk tentang mereka",
                "B. Memperlakukan mereka dengan rasa empati, tidak mendiskriminasi, dan memberi dukungan moral",
                "C. Mengusir mereka dari lingkungan tempat tinggal",
                "D. Memaksa mereka memakai masker khusus di tempat umum"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Stigma dan diskriminasi harus dihapus. Mengetahui bahwa HIV tidak menular lewat interaksi harian mengajarkan kita untuk bersikap manusiawi dan suportif terhadap ODHA."
        },
        {
            "id": 10,
            "pertanyaan": "Jika seseorang mengalami luka yang tidak biasa, ruam, atau nyeri di area intim, tindakan yang tepat adalah...",
            "pilihan": [
                "A. Membeli obat keras di warung tanpa resep dokter",
                "B. Menyembunyikan gejala karena takut dimarahi",
                "C. Berkonsultasi secara terbuka dengan dokter di puskesmas atau fasilitas kesehatan resmi",
                "D. Mengoleskan pasta gigi atau zat kimia berbahaya pada luka"
            ],
            "jawaban_benar": 2,
            "penjelasan": "Memeriksakan diri ke dokter di puskesmas memastikan diagnosis yang tepat dan penanganan dini secara medis tanpa menimbulkan komplikasi lebih berat."
        }
    ],

    # ----------------------------------------------------
    # TOPIK 5: PENCEGAHAN KEKERASAN SEKSUAL (10 SOAL)
    # ----------------------------------------------------
    "pencegahan_kekerasan_seksual": [
        {
            "id": 1,
            "pertanyaan": "Prinsip utama tentang kepemilikan tubuh yang harus dipahami setiap anak adalah...",
            "pilihan": [
                "A. Tubuh kita adalah milik orang lain yang lebih tua",
                "B. Tubuh kita adalah hak milik pribadi kita sendiri dan kita berhak menjaganya dari perlakuan tidak sopan",
                "C. Tubuh kita bebas disentuh oleh siapa saja asalkan diberi uang jajan",
                "D. Tubuh anak-anak tidak memerlukan perlindungan khusus"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Setiap individu memiliki hak otonomi tubuh (bodily integrity), yaitu hak untuk merasa aman dan menolak perlakuan yang melanggar batas kenyamanan fisiknya."
        },
        {
            "id": 2,
            "pertanyaan": "Area tubuh mana sajakah yang tergolong sebagai area pribadi yang tidak boleh dilihat atau disentuh sembarangan?",
            "pilihan": [
                "A. Rambut, telapak tangan, dan ujung kuku",
                "B. Bibir, dada/payudara, organ kemaluan, dan pantat/bokong",
                "C. Pundak dan siku tangan",
                "D. Lutut dan tumit kaki"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Area yang umumnya tertutup pakaian renang atau pakaian dalam (bibir, dada, area kelamin, pantat) adalah area pribadi yang dilindungi hukum dan norma kesopanan."
        },
        {
            "id": 3,
            "pertanyaan": "Manakah di bawah ini yang merupakan contoh dari 'sentuhan aman'?",
            "pilihan": [
                "A. Sentuhan di area dada yang disertai ancaman",
                "B. Jabat tangan ramah saat menyapa teman atau tepukan penyemangat di pundak oleh guru di depan kelas",
                "C. Sentuhan pada organ pribadi di tempat yang sepi dan tersembunyi",
                "D. Memaksa memegang bagian tubuh pribadi orang lain"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Sentuhan aman adalah sentuhan yang wajar, terbuka, menghormati kesopanan, dan membuat seseorang merasa nyaman serta dihargai."
        },
        {
            "id": 4,
            "pertanyaan": "Apakah yang dimaksud dengan 'sentuhan membingungkan atau mencurigakan'?",
            "pilihan": [
                "A. Sentuhan yang membuat kita merasa tidak nyaman, takut, risih, atau disertai bisikan agar merahasiakannya",
                "B. Sentuhan saat seorang dokter memeriksa paru-paru dengan stetoskop di hadapan orang tua",
                "C. Sentuhan hangat saat ibu memeluk kita saat sedih",
                "D. Sentuhan ketika bersalaman dengan kakek di hari raya"
            ],
            "jawaban_benar": 0,
            "penjelasan": "Jika sebuah sentuhan memunculkan rasa janggal, risih, atau pelaku meminta merahasiakannya dengan ancaman/rayuan, itu adalah tanda bahaya kekerasan seksual."
        },
        {
            "id": 5,
            "pertanyaan": "Apakah tiga langkah utama perlindungan diri jika ada orang yang mencoba melanggar batas tubuhmu?",
            "pilihan": [
                "A. Diam saja, menangis di tempat, dan menyalahkan diri sendiri",
                "B. TOLAK (Katakan Tidak dengan tegas), LARI (Pergi ke tempat aman), dan LAPOR (Ceritakan kepada orang dewasa tepercaya)",
                "C. Mengambil foto pelaku lalu mengunggahnya ke media sosial tanpa melapor ke keluarga",
                "D. Meminta uang damai kepada pelaku"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Langkah TOLAK - LARI - LAPOR (Katakan Tidak, Jauhi Bahaya, Laporkan ke Pihak Berwenang/Keluarga) adalah panduan standar pencegahan kekerasan bagi anak dan remaja."
        },
        {
            "id": 6,
            "pertanyaan": "Kapan seseorang diperbolehkan memeriksa atau melihat area pribadi tubuhmu?",
            "pilihan": [
                "A. Siapa saja di tempat umum asal meminta izin secara sopan",
                "B. Dokter atau tenaga medis resmi untuk keperluan pemeriksaan kesehatan, DENGAN DAMPINGAN orang tua atau wali sah",
                "C. Teman sebaya saat bermain petak umpet di ruang kosong",
                "D. Orang dewasa tak dikenal yang menawarkan hadiah mainan"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Pemeriksaan area pribadi hanya boleh dilakukan untuk tindakan medis yang sah dan wajib selalu didampingi oleh orang tua atau wali demi keselamatan."
        },
        {
            "id": 7,
            "pertanyaan": "Apakah yang dimaksud dengan 'victim blaming' (menyalahkan korban)?",
            "pilihan": [
                "A. Menghukum pelaku kejahatan dengan hukuman yang seberat-beratnya",
                "B. Sikap keliru yang menyalahkan pakaian, sikap, atau keberadaan korban atas terjadinya kekerasan seksual",
                "C. Tindakan memberikan bantuan medis dan psikologis kepada korban",
                "D. Upaya mencari saksi mata yang melihat suatu kejadian kejahatan"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Victim blaming adalah tindakan keliru yang melukai korban secara emosional. Pelaku kekerasan adalah satu-satunya pihak yang bertanggung jawab atas kejahatan tersebut."
        },
        {
            "id": 8,
            "pertanyaan": "Jika ada orang di media sosial yang meminta foto bagian tubuh pribadimu dengan iming-iming pulsa atau uang, sikap yang benar adalah...",
            "pilihan": [
                "A. Mengirimkan foto karena tergiur dengan hadiah pulsa",
                "B. Menolak tegas, memblokir akun tersebut, dan segera memberitahukan kejadian ini kepada orang tua atau guru",
                "C. Mengirimkan foto teman lain sebagai pengganti",
                "D. Melanjutkan percakapan rahasia di aplikasi lain"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Ini adalah modus kejahatan daring (cyber sexual grooming). Jangan pernah mengirimkan foto pribadi. Segera tolak, blokir, dan laporkan kepada orang tua."
        },
        {
            "id": 9,
            "pertanyaan": "Jika seorang teman bercerita bahwa ia pernah mengalami perlakuan tidak sopan atau kekerasan, sikap empati yang tepat adalah...",
            "pilihan": [
                "A. Menyebarkan rahasia teman itu ke seluruh kelas agar menjadi bahan gosip",
                "B. Mendengarkan ceritanya dengan tenang tanpa menghakimi, dan mendampinginya melapor ke guru BK atau orang tua",
                "C. Menertawakannya dan mengatakan bahwa itu salahnya sendiri",
                "D. Meminta teman tersebut tidak menceritakan pada siapa pun selamanya"
            ],
            "jawaban_benar": 1,
            "penjelasan": "Mendengarkan dengan penuh empati, meyakinkan bahwa itu bukan kesalahannya, serta membantunya mencari pertolongan orang dewasa adalah wujud kepedulian yang sejati."
        },
        {
            "id": 10,
            "pertanyaan": "Undang-Undang di Indonesia yang secara khusus melindungi masyarakat dari tindak pidana kekerasan seksual adalah...",
            "pilihan": [
                "A. UU No. 12 Tahun 2022 tentang Tindak Pidana Kekerasan Seksual (UU TPKS)",
                "B. Undang-Undang Lalu Lintas dan Angkutan Jalan",
                "C. Undang-Undang Kepabeanan dan Cukai",
                "D. Undang-Undang Hak Paten Industri"
            ],
            "jawaban_benar": 0,
            "penjelasan": "UU TPKS No. 12 Tahun 2022 adalah instrumen hukum penting di Indonesia yang memberikan perlindungan menyeluruh bagi korban, pencegahan, dan sanksi tegas bagi pelaku."
        }
    ]
}


def get_quiz_by_topic(topic_id):
    """Mengembalikan daftar 10 pertanyaan kuis untuk topik tertentu."""
    return BANK_SOAL.get(topic_id, [])


def get_quiz_length(topic_id):
    """Mengembalikan jumlah soal untuk topik tertentu."""
    return len(BANK_SOAL.get(topic_id, []))


def calculate_topic_score(topic_id, user_answers):
    """
    Menghitung skor kuis berdasarkan jawaban pengguna.
    user_answers: dict {question_index: selected_option_index}
    Returns: dict dengan 'skor', 'benar', 'salah', 'total', 'persentase', 'kategori', 'detail'
    """
    soal_list = BANK_SOAL.get(topic_id, [])
    if not soal_list:
        return {
            "skor": 0,
            "benar": 0,
            "salah": 0,
            "total": 0,
            "persentase": 0.0,
            "kategori": "Perlu Belajar Lagi",
            "detail": []
        }

    benar_count = 0
    detail = []

    for idx, soal in enumerate(soal_list):
        ans = user_answers.get(idx)
        jawaban_benar_idx = soal["jawaban_benar"]
        is_correct = (ans == jawaban_benar_idx)
        if is_correct:
            benar_count += 1

        detail.append({
            "soal_id": soal["id"],
            "pertanyaan": soal["pertanyaan"],
            "pilihan": soal["pilihan"],
            "jawaban_pengguna": ans,
            "jawaban_benar": jawaban_benar_idx,
            "is_correct": is_correct,
            "penjelasan": soal["penjelasan"]
        })

    total_soal = len(soal_list)
    salah_count = total_soal - benar_count
    skor = benar_count * 10
    persentase = (skor / (total_soal * 10)) * 100.0

    # Kategori pemahaman kuis:
    # 0 - 50: Perlu Belajar Lagi
    # 51 - 75: Cukup Memahami
    # 76 - 100: Sudah Memahami
    if skor <= 50:
        kategori = "Perlu Belajar Lagi"
    elif skor <= 75:
        kategori = "Cukup Memahami"
    else:
        kategori = "Sudah Memahami"

    return {
        "skor": skor,
        "benar": benar_count,
        "salah": salah_count,
        "total": total_soal,
        "persentase": persentase,
        "kategori": kategori,
        "detail": detail
    }
