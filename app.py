"""
Aplikasi Kalkulator Transformasi Bilangan Flask
-----------------------------------------------
Main entry point dari aplikasi Flask.
Menggunakan arsitektur modular dengan Blueprints agar lebih rapi dan mudah dikelola.
"""

from flask import Flask
from routes import register_blueprints

def create_app():
    """
    Factory function untuk membuat instance Flask app.
    Pendekatan ini direkomendasikan untuk aplikasi skala besar.
    """
    app = Flask(__name__)
    
    # Secret key untuk management session jika diperlukan
    app.secret_key = 'kalkulatorpro-secret-key-2026'

    # Mendaftarkan semua routes (view dan API) dari modul routes
    register_blueprints(app)
    
    return app

# Inisialisasi aplikasi
app = create_app()

if __name__ == '__main__':
    # Jalankan server
    app.run(debug=True, port=5000)
