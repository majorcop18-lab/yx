from flask import Flask, render_template, request

app = Flask(__name__)

def berikan_saran_kopi(usia, kadar_gula):
    """
    Memberikan saran kopi berdasarkan usia dan kadar gula darah.
    """
    saran_utama = ""
    saran_alternatif = []

    # --- Logika Saran Berdasarkan Usia ---
    if usia < 18:
        # Untuk usia di bawah 18, utamakan minuman tanpa kafein kuat
        saran_utama = "Minuman Non-Kopi atau Kopi Rendah Kafein (misalnya, **Cokelat Panas**, **Teh Herbal**, atau **Decaf Latte**)."
    elif 18 <= usia <= 35:
        # Usia produktif
        saran_utama = "Kopi dengan *Body* dan *Flavor* Kuat (misalnya, **Espresso**, **Cappuccino**, atau **Pour-Over** dengan biji *Arabica*)."
    elif 36 <= usia <= 55:
        # Usia yang mungkin lebih memilih keseimbangan
        saran_utama = "Kopi Klasik yang Seimbang (misalnya, **Latte** standar, **Americano**, atau **Cold Brew**)."
    else: # usia > 55
        # Utamakan yang lebih lembut di lambung dan mudah dicerna
        saran_utama = "Kopi dengan Keasaman Rendah (**Decaf Americano** atau **Kopi Susu Almond** ringan)."

    # --- Logika Penyesuaian Berdasarkan Kadar Gula ---
    if kadar_gula.lower() == 'tinggi' or kadar_gula.lower() == 'diabetes':
        # Saran untuk kadar gula tinggi
        if "decaf" not in saran_utama.lower() and "non-kopi" not in saran_utama.lower():
             # Jika saran utama bukan decaf/non-kopi, berikan alternatif.
            saran_alternatif.append("**Kopi Hitam Polos** (tanpa gula/pemanis)."
                                    " Hindari sirup dan krim manis.")
            saran_alternatif.append("**Stevia atau Erythritol** sebagai pemanis jika diperlukan, **bukan gula pasir**.")
            saran_alternatif.append("Utamakan minuman dengan susu rendah lemak atau non-dairy **tanpa tambahan gula**.")
        else:
             # Jika saran utama sudah rendah risiko
            saran_alternatif.append("Tetap pastikan minuman **bebas gula tambahan** dan gunakan pemanis alternatif yang aman.")

    elif kadar_gula.lower() == 'rendah' or kadar_gula.lower() == 'normal':
        # Untuk gula normal/rendah, berikan opsi eksplorasi
        saran_alternatif.append("Anda bebas mencoba varian kopi dengan sedikit tambahan rasa (misalnya, **Vanilla Latte** atau **Kopi Gula Aren**).")
        saran_alternatif.append("Untuk energi, coba **Affogato** atau **Mocha**.")

    return saran_utama, saran_alternatif

@app.route('/', methods=['GET', 'POST'])
def index():
    saran_kopi = None
    saran_alternatif = None
    usia_input = None
    kadar_gula_input = None

    if request.method == 'POST':
        try:
            # Ambil input dari form
            usia_input = int(request.form.get('usia'))
            kadar_gula_input = request.form.get('kadar_gula') # Nilainya 'Normal/Rendah' atau 'Tinggi/Diabetes'

            # Panggil fungsi untuk mendapatkan saran
            saran_kopi, saran_alternatif = berikan_saran_kopi(usia_input, kadar_gula_input)
        except ValueError:
            saran_kopi = "⚠️ **Input Usia Tidak Valid.** Mohon masukkan angka."
            saran_alternatif = []
        except Exception as e:
            saran_kopi = f"⚠️ **Terjadi Kesalahan:** {e}"
            saran_alternatif = []

    # Render template dengan hasil saran (atau tanpa hasil jika GET request)
    return render_template('index.html', 
                           saran_kopi=saran_kopi, 
                           saran_alternatif=saran_alternatif,
                           usia=usia_input,
                           kadar_gula=kadar_gula_input)

if __name__ == '__main__':
    # Pastikan Anda membuat folder 'templates' di direktori yang sama
    app.run(debug=True)
