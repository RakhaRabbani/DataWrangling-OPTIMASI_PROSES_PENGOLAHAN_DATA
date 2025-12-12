from multiprocessing import Pool

def hitung(n):
    return n * n * n

if __name__ == "__main__":
    # Menggunakan Pool untuk paralelisasi
    with Pool() as p:
        hasil = p.map(hitung, range(1_000_000))
    
    print("Selesai!")