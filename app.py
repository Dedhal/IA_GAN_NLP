from flask import Flask, send_file
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)

generator = tf.keras.models.load_model('dog_generator.h5')

def generate_image():
    z_dim = 100 
    z = np.random.normal(0, 1, (1, z_dim))
    fake_image = generator.predict(z)
    fake_image = ((fake_image + 1) / 2 * 255).astype(np.uint8)
    fake_image = cv2.cvtColor(fake_image[0], cv2.COLOR_RGB2BGR)
    cv2.imwrite('generated_image.jpg', fake_image)
    return 'generated_image.jpg'

@app.route('/')
def home():
    image_path = generate_image()
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
