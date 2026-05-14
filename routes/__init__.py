"""
Export semua blueprint agar dapat didaftarkan di app.py
"""

from .views import views_bp
from .api_aritmatika import api_aritmatika_bp
from .api_logika import api_logika_bp
from .api_konversi import api_konversi_bp
from .api_bonus import api_bonus_bp

def register_blueprints(app):
    """
    Fungsi untuk mendaftarkan semua blueprint ke dalam instance Flask app.
    
    Args:
        app (Flask): Instance aplikasi Flask utama.
    """
    app.register_blueprint(views_bp)
    app.register_blueprint(api_aritmatika_bp, url_prefix='/api/aritmatika')
    app.register_blueprint(api_logika_bp, url_prefix='/api/logika')
    app.register_blueprint(api_konversi_bp, url_prefix='/api/konversi')
    app.register_blueprint(api_bonus_bp, url_prefix='/api/bonus')
