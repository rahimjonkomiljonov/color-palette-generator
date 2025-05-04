

A Flask-based web application that extracts the dominant colors from an uploaded image and displays them in a table with their hex codes and percentages.

## Features
- Upload images in PNG, JPG, JPEG, or GIF format.
- Extracts the top 10 dominant colors using K-means clustering.
- Displays colors with their hex codes and percentage of occurrence in a clean, white table.
- Persistent image preview using localStorage.
- Responsive design with a consistent background image.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/color-palette-generator.git
   cd color-palette-generator
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.x installed, then run:
   ```bash
   pip install flask flask-wtf pillow scikit-learn numpy
   ```

4. **Directory Structure**:
   Ensure the following structure:
   ```
   color-palette-generator/
   ├── static/
   │   ├── images/
   │   │   └── pexels-pixabay-531756.jpg  # Background image
   │   └── uploads/                       # Folder for uploaded images
   ├── templates/
   │   └── index.html                     # HTML template
   ├── main.py                            # Flask application
   └── README.md                          # This file
   ```

## Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```
   The app will start at `http://127.0.0.1:5000`.

2. **Upload an Image**:
   - Open the URL in your browser.
   - Click "Choose File" to select an image.
   - Click "Extract Colors" to process the image.

3. **View Results**:
   - The dominant colors will be displayed in a table with their hex codes and percentages.

## Screenshots

![Color Palette Generator Interface](path/to/screenshot.png)
*Upload an image and extract its dominant colors.*

## Dependencies
- Flask: Web framework
- Flask-WTF: Form handling
- Pillow: Image processing
- scikit-learn: K-means clustering for color extraction
- NumPy: Array operations

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""

    
