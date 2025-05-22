from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

perintah_terakhir = "tutup"
jenis_terakhir = "tidak ada"
riwayat = []  # List untuk menyimpan riwayat data (jenis, perintah)

@app.route("/", methods=["GET", "POST"])
def index():
    global perintah_terakhir, jenis_terakhir, riwayat
    if request.method == "POST":
        jenis = request.form.get("jenis")
        if jenis == "organik":
            perintah_terakhir = "buka"
        else:
            perintah_terakhir = "tutup"
        jenis_terakhir = jenis
        riwayat.append({"jenis": jenis, "perintah": perintah_terakhir})

    return render_template("index.html", perintah=perintah_terakhir, riwayat=riwayat)

@app.route("/perintah", methods=["GET"])
def get_perintah():
    # Kirim juga jenis sampah supaya ESP32 tahu
    return jsonify({"perintah": perintah_terakhir, "jenis": jenis_terakhir})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
