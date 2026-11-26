"""
Modul Machine Learning ReproGuide
Mengimplementasikan klasifikasi tingkat pemahaman menggunakan Scikit-learn
DecisionTreeClassifier (Algoritma CART - Classification and Regression Trees).
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from modules.data_loader import KOLOM_FITUR, KOLOM_TARGET, load_dataset


class ReproGuideClassifier:
    """
    Kelas pembungkus untuk melatih, mengevaluasi, dan melakukan inferensi
    menggunakan model Decision Tree CART.
    """

    def __init__(self, criterion="gini", max_depth=4, random_state=42):
        self.criterion = criterion
        self.max_depth = max_depth
        self.random_state = random_state
        self.model = DecisionTreeClassifier(
            criterion=self.criterion,
            max_depth=self.max_depth,
            random_state=self.random_state
        )
        self.is_trained = False
        self.feature_names = KOLOM_FITUR
        self.target_name = KOLOM_TARGET
        self.class_names = ["Rendah", "Sedang", "Tinggi"]
        self.metrics = {}
        self.feature_importances_ = None
        self.tree_rules_text = ""

    def train(self, df=None, test_size=0.2):
        """
        Melatih model Decision Tree menggunakan dataset simulasi.
        """
        if df is None:
            df = load_dataset()

        X = df[self.feature_names]
        y = df[self.target_name]

        # Pembagian data latih (train) dan data uji (test)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state, stratify=y
        )

        # Pelatihan model CART
        self.model.fit(X_train, y_train)
        self.is_trained = True

        # Evaluasi pada data uji
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        cm = confusion_matrix(y_test, y_pred, labels=self.class_names)

        # Feature importances
        self.feature_importances_ = dict(
            zip(self.feature_names, self.model.feature_importances_)
        )

        # Ringkasan aturan pohon keputusan dalam format teks
        self.tree_rules_text = export_text(
            self.model,
            feature_names=[
                "Kelas", "Skor_Pub", "Skor_PerubTubuh",
                "Skor_Kebersihan", "Skor_IMS", "Skor_Kekerasan"
            ]
        )

        self.metrics = {
            "accuracy": round(acc * 100, 2),
            "total_latih": len(X_train),
            "total_uji": len(X_test),
            "confusion_matrix": cm,
            "classification_report": report
        }

        return self.metrics

    def predict(self, user_features):
        """
        Melakukan prediksi kategori pemahaman untuk pengguna tunggal.
        user_features: dict atau list berisi:
        [kelas, skor_pubertas, skor_perubahan_tubuh, skor_kebersihan_menstruasi, skor_pencegahan_ims, skor_pencegahan_kekerasan_seksual]
        """
        if not self.is_trained:
            self.train()

        if isinstance(user_features, dict):
            input_row = [
                user_features.get("kelas", 7),
                user_features.get("skor_pubertas", 0),
                user_features.get("skor_perubahan_tubuh", 0),
                user_features.get("skor_kebersihan_menstruasi", 0),
                user_features.get("skor_pencegahan_ims", 0),
                user_features.get("skor_pencegahan_kekerasan_seksual", 0),
            ]
        else:
            input_row = list(user_features)

        X_input = pd.DataFrame([input_row], columns=self.feature_names)
        prediction = self.model.predict(X_input)[0]

        # Probabilitas masing-masing kelas
        probabilities = {}
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(X_input)[0]
            for cls, prob in zip(self.model.classes_, probs):
                probabilities[cls] = round(prob * 100, 1)

        return {
            "kategori_prediksi": prediction,
            "probabilitas": probabilities,
            "input_digunakan": dict(zip(self.feature_names, input_row))
        }

    def get_model_info(self):
        """Mengembalikan informasi ringkas mengenai konfigurasi model."""
        return {
            "algoritma": "DecisionTreeClassifier (CART)",
            "kriteria_pemisahan": "Gini Impurity",
            "kedalaman_maksimal": self.max_depth,
            "random_state": self.random_state,
            "status_pelatihan": "Sudah Dilatih" if self.is_trained else "Belum Dilatih",
            "metrik": self.metrics,
            "fitur_penting": self.feature_importances_,
            "aturan_pohon": self.tree_rules_text
        }
