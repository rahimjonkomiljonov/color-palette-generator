from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from PIL import Image
from collections import Counter
import colorsys
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yfjt8tyf64j9h0huugjgfdr354s'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

class UploadImageForm(FlaskForm):
    image = FileField('Upload Image')
    submit = SubmitField('Extract Colors')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_top_colors(image_path, num_colors=10):
    # Open and resize image
    img = Image.open(image_path).convert('RGB')
    img = img.resize((300, 300))  # Increased size for better detail
    pixels = np.array(img.getdata())

    # Reshape pixels for K-means clustering
    pixels_2d = pixels.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(pixels_2d)
    cluster_labels = kmeans.predict(pixels_2d)
    centers = kmeans.cluster_centers_.astype(int)

    # Calculate counts for each cluster
    cluster_counts = np.bincount(cluster_labels, minlength=num_colors)

    # Convert cluster centers to hex and calculate percentages
    color_data = []
    total_pixels = len(pixels)
    for i, center in enumerate(centers):
        r, g, b = center
        hex_code = f'#{r:02x}{g:02x}{b:02x}'.lower()
        percentage = cluster_counts[i] / total_pixels if total_pixels > 0 else 0
        color_data.append((hex_code, percentage))

    # Sort by percentage in descending order
    color_data.sort(key=lambda x: x[1], reverse=True)
    return color_data[:num_colors]

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadImageForm()
    color_data = None
    if form.validate_on_submit():
        file = form.image.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            color_data = extract_top_colors(file_path)
        else:
            return "Invalid file type. Please upload a PNG, JPG, JPEG, or GIF."
    return render_template('index.html', form=form, color_data=color_data)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, port=5001)