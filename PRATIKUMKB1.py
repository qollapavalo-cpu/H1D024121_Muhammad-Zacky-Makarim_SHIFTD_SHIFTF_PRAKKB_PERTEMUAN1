# Library
import random
import numpy as np

def analisis_nilai_siswa():
    print("Program Analisis Nilai Siswa")
    
    # 1. Struktur Data (List)
    nilai_siswa = []
    
    # 2. Struktur Kontrol (Perulangan)
    for i in range(10):
        nilai_acak = random.randint(60, 100)
        nilai_siswa.append(nilai_acak)
        
    print(f"Daftar Nilai Siswa (List): {nilai_siswa}")
    
    nilai_unik = set(nilai_siswa)
    print(f"Daftar Nilai Unik (Set): {nilai_unik}")
    
    rata_rata = np.mean(nilai_siswa)
    print(f"Rata-rata Kelas: {rata_rata}")
    
    print("\nStatus Kelulusan:")
    for nilai in nilai_siswa:
        if nilai >= 75:
            print(f"Nilai {nilai}: Lulus")
        else:
            print(f"Nilai {nilai}: Tidak Lulus")

analisis_nilai_siswa()