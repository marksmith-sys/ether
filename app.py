from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Головна сторінка з формою оплати"""
    return render_template('index.html')

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    """Обслуговування зображень"""
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)