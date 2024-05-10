from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import qrcode

app = Flask(__name__)


def encode_image_to_qr(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Convert image to QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(image_path)
    qr.make(fit=True)

    # Create QR code image
    qr_image = qr.make_image(fill_color="white", back_color="#0b1f52")

    return qr_image

def decode_qr_to_image(qr_image):
    # Decode QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(qr_image)
    qr.make(fit=True)

    # Extract data from QR code
    image_path = qr.data_list[0].data.decode("utf-8")

    # Read original image
    original_image = cv2.imread(image_path)

    return original_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file_path = 'uploads/' + filename
            file.save(file_path)
            qr_image = encode_image_to_qr(file_path)
            qr_image.save("static/encrypted_qr.png")
            return render_template('encrypt.html', qr_image="static/encrypted_qr.png")
        else:
            error_message = "Error: Please select an image."
            return render_template('error_encrypt.html', error_message=error_message)

@app.route('/decrypt')
def decrypt():
    qr_image_path = "uploads/image.png"
    qr_image_enc = "static/encrypted_qr.png"
    if qr_image_enc:
        original_image = decode_qr_to_image(qr_image_path)
        cv2.imwrite("static/decrypted_image.png", original_image)
        return render_template('decrypt.html', decrypted_image="static/decrypted_image.png")
    else:
        return "Error: Please provide encrypted QR code."

if __name__ == '__main__':
    app.run(debug=True)