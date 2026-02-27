import datetime
import webbrowser

def tampilkan_menu():
    """Menampilkan menu pilihan"""
    print("\n=== BROWSER SEDERHANA ===")
    print("1. Buka Website")
    print("2. Lihat History")
    print("3. Hapus History")
    print("4. Out")
    print("========================")

def buka_website():
    """Fungsi untuk 'membuka' website"""
    url = input("Masukkan URL website: ")
    
    # Memastikan URL memiliki protokol http:// atau https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    # Mendapatkan waktu sekarang
    waktu_sekarang = datetime.datetime.now()
    waktu_format = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
    
    # Menyimpan ke file history.txt
    with open("history.txt", "a") as file:
        file.write(f"{waktu_format} | {url}\n")
    
    # Membuka URL di browser
    print(f"🌐 Membuka {url} di browser...")
    webbrowser.open(url)
    
    print(f"✓ Berhasil membuka: {url}")
    print(f"✓ Tersimpan di history pada {waktu_format}")

def lihat_history():
    """Fungsi untuk melihat history browsing"""
    try:
        with open("history.txt", "r") as file:
            isi_history = file.readlines()
        
        if len(isi_history) == 0:
            print("\nHistory masih kosong!")
        else:
            print("\n=== HISTORY BROWSING ===")
            nomor = 1
            for baris in isi_history:
                print(f"{nomor}. {baris.strip()}")
                nomor = nomor + 1
            print(f"\nTotal: {len(isi_history)} website")
    
    except FileNotFoundError:
        print("\nHistory masih kosong!")

def hapus_history():
    """Fungsi untuk menghapus history"""
    try:
        with open("history.txt", "r") as file:
            isi_history = file.readlines()
        
        if len(isi_history) == 0:
            print("\nHistory masih kosong!")
            return
        
        # Tampilkan sub-menu hapus
        print("\n=== MENU HAPUS ===")
        print("1. Pilih history yang mau dihapus")
        print("2. Hapus SEMUA history")
        print("0. Batal")
        print("==================")
        
        pilihan_menu = input("\nPilih menu: ")
        
        try:
            nomor_menu = int(pilihan_menu)
            
            # Pilihan 0: Batal
            if nomor_menu == 0:
                konfirmasi_batal = input("Yakin nih mau dibatalin? (y/n): ")
                if konfirmasi_batal.lower() == "y":
                    print("✗ Penghapusan dibatalkan, kembali ke menu utama")
                else:
                    print("✓ Oke, balik lagi nih ke menu hapus. Pilih yang bener dong!")
                    # Panggil fungsi hapus_history lagi untuk kembali ke menu hapus
                    hapus_history()
            
            # Pilihan 1: Hapus history tertentu
            elif nomor_menu == 1:
                # Tampilkan history dengan nomor
                print("\n=== HISTORY BROWSING ===")
                nomor = 1
                for baris in isi_history:
                    print(f"{nomor}. {baris.strip()}")
                    nomor = nomor + 1
                print("========================")
                
                pilihan_nomor = input(f"\nMasukkan nomor history yang mau dihapus (1-{len(isi_history)}): ")
                
                try:
                    nomor_hapus = int(pilihan_nomor)
                    
                    # Cek apakah nomor valid
                    if nomor_hapus >= 1 and nomor_hapus <= len(isi_history):
                        # Tampilkan item yang akan dihapus
                        item_dihapus = isi_history[nomor_hapus - 1]
                        print(f"\nAnda akan menghapus:")
                        print(f"  {item_dihapus.strip()}")
                        
                        # Minta konfirmasi
                        konfirmasi = input("\nYakin nih mau dihapus? (y/n): ")
                        
                        if konfirmasi.lower() == "y":
                            # Hapus item dari list
                            isi_history.pop(nomor_hapus - 1)
                            
                            # Tulis kembali ke file
                            with open("history.txt", "w") as file:
                                for baris in isi_history:
                                    file.write(baris)
                            
                            print(f"✓ History nomor {nomor_hapus} berhasil dihapus!")
                        else:
                            print("✗ Penghapusan dibatalkan")
                    else:
                        print(f"✗ Pilih yang bener dong! Pilih 1-{len(isi_history)}")
                
                except ValueError:
                    print("✗ Input yang bener lah! Harus pake nomor")
            
            # Pilihan 2: Hapus semua history
            elif nomor_menu == 2:
                konfirmasi = input("Yakin mau hapus SEMUA history? (y/n): ")
                if konfirmasi.lower() == "y":
                    with open("history.txt", "w") as file:
                        file.write("")
                    print("✓ Semua history berhasil dihapus!")
                else:
                    print("✗ Penghapusan dibatalkan")
            
            else:
                print("✗ Pilih yang bener dong! Pilih 0, 1, atau 2")
        
        except ValueError:
            print("✗ Input yang bener lah! Harus pake nomor")
    
    except FileNotFoundError:
        print("\nHistory masih kosong!")

# Program Utama
def main():
    print("Selamat datang di Browser Sederhana!")
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            buka_website()
        elif pilihan == "2":
            lihat_history()
        elif pilihan == "3":
            hapus_history()
        elif pilihan == "4":
            print("\nTerima kasih! Sampai jumpa!")
            break
        else:
            print("\n✗ Pilih yang bener dong! Pilih 1-4")

# Menjalankan program
if __name__ == "__main__":
    main()
