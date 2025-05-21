from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variabel global untuk menyimpan perintah terakhir
perintah_terakhir = "tutup"

@app.route("/", methods=["GET", "POST"])
def index():
    global perintah_terakhir
    if request.method == "POST":
        aksi = request.form.get("aksi")
        if aksi in ["buka", "tutup"]:
            perintah_terakhir = aksi
            print(f"Perintah diubah menjadi: {aksi}")
    return render_template("index.html", perintah=perintah_terakhir)

@app.route("/perintah", methods=["GET"])
def get_perintah():
    return jsonify({"perintah": perintah_terakhir})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
