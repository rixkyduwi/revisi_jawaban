from flask import Flask, jsonify
app= Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.route('/api/upload_image/', methods=['POST'])
def index():
  return jsonify{
    "pesan":"gambar telah terupload"
  }

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug = True, port=4000)