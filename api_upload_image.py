from flask import Flask
import jsonify
app= Flask(__name__)
app.config['']
app.routes('/api/upload_image/' method=['POST'])
def index():
  imagename=
  return jsonify{
    "pesan":"gambar telah terupload"
  }
