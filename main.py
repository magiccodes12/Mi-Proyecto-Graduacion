from flask import Flask, render_template, request, redirect, url_for
import os
import http.server
import socketserver

app = Flask(__name__)

IMAGES = ["static/img/gallery/1.jpeg",
        "static/img/gallery/2.jpg",
        "static/img/gallery/3.jpg"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/donations.html')
def donations():
    return render_template('donations.html')

@app.route('/donar', methods=['POST'])
def donar():
    cantidad = request.form.get('cantidad') 

    print(f'Donacion recibida: ${cantidad}')
    return redirect(url_for('donations'))

@app.route('/recursos.html')
def us():
    return render_template('recursos.html')

@app.route('/index.html')
def inicio():
    return render_template('index.html')

@app.route('/3r.html')
def projects():
    return render_template('3r.html')

if __name__ == '__main__':
    app.run(debug=True)