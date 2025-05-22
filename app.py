from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

perintah_terakhir = "tutup"

@app.route("/", methods=["GET", "POST"])
def index():
    global perintah_terakhir
    if request.method == "POST":
        jenis = request.form.get("jenis")
        if jenis == "organik":
            perintah_terakhir = "buka"
        else:
            perintah_terakhir = "tutup"
        print(f"Jenis sampah dipilih: {jenis} -> Perintah: {perintah_terakhir}")
    return render_template("index.html", perintah=perintah_terakhir)

@app.route("/perintah", methods=["GET"])
def get_perintah():
    return jsonify({"perintah": perintah_terakhir})

if _name_ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)