from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/klasifikasi', methods=['GET'])
def klasifikasi():
    jenis_sampah = random.choice(["organik", "anorganik", "B3"])
    return jsonify({"jenis": jenis_sampah})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
