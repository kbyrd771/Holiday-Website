from flask import Flask, render_template, request
from postmarker.core import PostmarkClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)