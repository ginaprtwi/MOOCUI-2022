# Fungsi untuk menghitung total belanjaan
def hitung_total_belanjaan(nama_berkas):
    try:
        # Membuka berkas receipt
        with open(nama_berkas, 'r') as file:
            total_harga = 0
            for line in file:
                # Memisahkan nama barang dan harga
                parts = line.strip().split()
                if len(parts) == 2:
                    harga = int(parts[1])
                    total_harga += harga
            
            # Menghitung total setelah diskon
            diskon = total_harga * 0.10
            total_setelah_diskon = total_harga - diskon
            
            # Menampilkan hasil
            print(f"Total harga pada receipt: {total_harga}")
            print(f"Total harga setelah diskon Hari Guru Nasional: {total_setelah_diskon}")
    
    except FileNotFoundError:
        print(f"Berkas {nama_berkas} tidak ditemukan :(")

# Program utama
if __name__ == "__main__":
    # Meminta input nama berkas receipt
    nama_berkas = input("Masukkan nama berkas receipt: ")
    hitung_total_belanjaan(nama_berkas)