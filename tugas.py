import math

# --- 1. Definisi Fungsi (Functions) ---

def hitung_silinder(r, t):
    keliling = 2 * math.pi * r
    # Luas permukaan silinder: 2 * luas alas + luas selimut
    luas_permukaan = 2 * math.pi * r * (r + t)
    volume = math.pi * (r**2) * t
    return keliling, luas_permukaan, volume

def hitung_kerucut(r, t):
    # Mencari garis pelukis (s) menggunakan pythagoras
    s = math.sqrt(r**2 + t**2)
    keliling_alas = 2 * math.pi * r
    # Luas permukaan kerucut: luas alas + luas selimut
    luas_permukaan = math.pi * r * (r + s)
    volume = (1/3) * math.pi * (r**2) * t
    return keliling_alas, luas_permukaan, volume

# --- 2. Input Data ---

print("=== Program Perhitungan Menara ===")
print("\n--- Data Silinder ---")
r_silinder = float(input("Masukkan jari-jari silinder: "))
t_silinder = float(input("Masukkan tinggi silinder: "))

print("\n--- Data Kerucut ---")
r_kerucut = float(input("Masukkan jari-jari kerucut: "))
t_kerucut = float(input("Masukkan tinggi kerucut: "))

# --- 3. Eksekusi Fungsi ---

k_sil, l_sil, v_sil = hitung_silinder(r_silinder, t_silinder)
k_ker, l_ker, v_ker = hitung_kerucut(r_kerucut, t_kerucut)

# --- 4. Output Hasil ---

print("\n" + "="*30)
print("HASIL PERHITUNGAN")
print("="*30)

print(f"Silinder:")
print(f"- Keliling Alas  : {k_sil:.2f}")
print(f"- Luas Permukaan : {l_sil:.2f}")
print(f"- Volume         : {v_sil:.2f}")

print(f"\nKerucut:")
print(f"- Keliling Alas  : {k_ker:.2f}")
print(f"- Luas Permukaan : {l_ker:.2f}")
print(f"- Volume         : {v_ker:.2f}")