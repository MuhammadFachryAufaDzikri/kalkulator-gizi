"""Modul perhitungan BMI, BMR, dan kebutuhan kalori."""

AKTIVITAS = {
    "sedikit": 1.2,     # jarang olahraga
    "ringan": 1.375,    # olahraga 1-3x/minggu
    "sedang": 1.55,     # olahraga 3-5x/minggu
    "berat": 1.725,     # olahraga 6-7x/minggu
}

GENDER = ("laki-laki", "perempuan")


def hitung_bmi(berat_kg, tinggi_cm):
    return 0.0


def kategori_bmi(bmi):
    return ""


def hitung_bmr(berat_kg, tinggi_cm, usia, gender):
    return 0.0


def hitung_kalori_harian(bmr, aktivitas):
    return 0.0


def hitung_target_makro(kalori):
    return {"protein": 0.0, "karbo": 0.0, "lemak": 0.0}