from flask import Flask, render_template, request

app = Flask(__name__)

# Halaman utama
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        aksi = request.form.get("aksi")
        if aksi == "buka":
            # Kirim perintah buka ke ESP32 di sini
            print("Perintah: Buka")
        elif aksi == "tutup":
            # Kirim perintah tutup ke ESP32 di sini
            print("Perintah: Tutup")
    return render_template("index.html")
