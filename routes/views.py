from flask import Blueprint, render_template

# Blueprint untuk halaman-halaman utama HTML
views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    """Halaman Utama"""
    return render_template('index.html')

@views_bp.route('/aritmatika')
def aritmatika():
    """Halaman Kalkulator Aritmatika"""
    return render_template('aritmatika.html')

@views_bp.route('/logika')
def logika():
    """Halaman Kalkulator Logika"""
    return render_template('logika.html')

@views_bp.route('/konversi')
def konversi():
    """Halaman Konversi Bilangan & Satuan"""
    return render_template('konversi.html')

@views_bp.route('/bonus')
def bonus():
    """Halaman Fitur Bonus (Faktorial & Fibonacci)"""
    return render_template('bonus.html')

@views_bp.route('/riwayat')
def riwayat():
    """Halaman Riwayat Perhitungan"""
    return render_template('riwayat.html')
