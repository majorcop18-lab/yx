def rekomendasi_kopi(umur):
    """
    Memberikan rekomendasi kopi berdasarkan kelompok umur.
    
    Args:
        umur (int): Umur pengguna.
        
    Returns:
        tuple: (Rekomendasi kopi, Saran tambahan)
    """
    
    if umur < 18:
        # Kelompok Anak/Remaja
        kopi_rekomendasi = "Minuman non-kopi (misalnya, cokelat panas, teh herbal)"
        saran_tambahan = "Hindari konsumsi kafein berlebihan. Jika ingin mencoba kopi, pilih yang kadar kafeinnya sangat rendah atau tanpa kafein (decaf)."
    
    elif 18 <= umur <= 25:
        # Kelompok Dewasa Muda (Mencoba Hal Baru)
        kopi_rekomendasi = "Kopi kekinian (misalnya, Cold Brew, V60 single origin dengan rasa fruity, Cappuccino manis)"
        saran_tambahan = "Usia ini sering bereksperimen. Cobalah berbagai biji kopi dari berbagai daerah (single origin) untuk menemukan profil rasa favoritmu (asam, pahit, manis)."
    
    elif 26 <= umur <= 45:
        # Kelompok Dewasa (Keseimbangan & Klasik)
        kopi_rekomendasi = "Espresso-based klasik (misalnya, Latte, Americano) atau Kopi Tubruk/Filter Kopi medium-to-dark roast."
        saran_tambahan = "Fokus pada konsistensi dan kualitas. Coba nikmati kopi tanpa banyak tambahan gula atau susu untuk menghargai rasa kopi yang sebenarnya. Perhatikan waktu konsumsi kafein."
        
    elif 46 <= umur <= 65:
        # Kelompok Dewasa Lanjut (Kenyamanan & Kesehatan)
        kopi_rekomendasi = "Kopi Decaf (Tanpa Kafein) atau kopi dengan kadar kafein rendah (misalnya, kopi robusta dark roast yang cenderung kurang asam di perut)."
        saran_tambahan = "Pertimbangkan faktor kesehatan, seperti sensitivitas lambung dan tekanan darah. Minum dalam jumlah sedang."
        
    else: # umur > 65
        # Kelompok Lansia
        kopi_rekomendasi = "Sangat disarankan Kopi Decaf atau teh. Jika mengonsumsi kopi berkafein, lakukan konsultasi dengan dokter."
        saran_tambahan = "Hidrasi sangat penting. Batasi kafein dan pastikan kopi yang dikonsumsi tidak mengganggu tidur atau pencernaan."
        
    return kopi_rekomendasi, saran_tambahan

# --- Program Utama ---
def main():
    print("--- 💡 Program Rekomendasi Kopi Berdasarkan Umur ---")
    
    while True:
        try:
            # Meminta input umur dari pengguna
            umur_input = input("Masukkan umur Anda (dalam angka): ")
            umur = int(umur_input)
            
            if
