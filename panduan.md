Panduan menjalankan aplikasi web
1. Pastikan Python latest version sudah terpasang
2. Pastikan Github sudah login dan editor sudah terpasang (vscode atau antigravity) 
3. Cara mengambil proyek dari Github
a. (Jika punya git) buka halaman repo di browser, lalu klik tombol hijau "<> Code" di sebelah kanan atas daftar file. 
   Pada tab HTTPS, klik ikon salin (dua kotak bertingkat) untuk menyalin URL repository. Buka terminal, lalu ketik 
   git clone <tempel_link_yang_sudah_disalin>
   cd nama-repo
b. (Download melalui ZIP) buka halaman repo di browser, lalu klik tombol hijau "<> Code" di sebelah kanan atas daftar file. 
   Di menu dropdown paling bawah, klik Download ZIP. Lalu ekstrak zip folder ke lokasi yang kamu inginkan.
4. Jalankan perintah berikut satu persatu di terminal:
   pip install -r requirements.txt
   streamlit run app.py
  
