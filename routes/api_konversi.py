from flask import Blueprint, request, jsonify
from utils import validate_base_number, convert_base_to_base

api_konversi_bp = Blueprint('api_konversi', __name__)

@api_konversi_bp.route('/bilangan', methods=['POST'])
def konversi_bilangan():
    """
    Endpoint untuk konversi basis bilangan.
    """
    try:
        data = request.json
        number = data['number'].strip()
        from_base = int(data['from_base'])
        to_base = int(data['to_base'])
        
        # Validasi batas basis yang diperbolehkan
        if from_base not in [2, 8, 10, 16] or to_base not in [2, 8, 10, 16]:
            return jsonify({'error': 'Basis harus 2, 8, 10, atau 16!'}), 400
        
        # Validasi string angka untuk basis asal
        if not validate_base_number(number, from_base):
            return jsonify({'error': f'Angka tidak valid untuk basis {from_base}!'}), 400
        
        # Eksekusi konversi
        result, steps, formula = convert_base_to_base(number, from_base, to_base)
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_konversi_bp.route('/suhu', methods=['POST'])
def konversi_suhu():
    """
    Endpoint untuk konversi antar satuan suhu (C, F, K, R).
    """
    try:
        data = request.json
        value = float(data['value'])
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        
        # 1. Konversi ke Celcius terlebih dahulu
        if from_unit == 'C':
            celsius = value
        elif from_unit == 'F':
            celsius = (value - 32) * 5/9
        elif from_unit == 'K':
            celsius = value - 273.15
        elif from_unit == 'R':
            celsius = value * 5/4
        else:
            return jsonify({'error': 'Unit tidak valid!'}), 400
        
        # 2. Konversi dari Celcius ke satuan tujuan
        if to_unit == 'C':
            result = celsius
        elif to_unit == 'F':
            result = (celsius * 9/5) + 32
        elif to_unit == 'K':
            result = celsius + 273.15
        elif to_unit == 'R':
            result = celsius * 4/5
        else:
            return jsonify({'error': 'Unit tidak valid!'}), 400
        
        steps = [
            f"Nilai awal: {value}°{from_unit}",
            f"Konversi ke Celsius: {celsius}°C" if from_unit != 'C' else "Sudah dalam Celsius",
            f"Konversi ke {to_unit}: {result}°{to_unit}" if to_unit != 'C' else "Hasil akhir"
        ]
        
        formula = f"{value}°{from_unit} = {result}°{to_unit}"
        
        return jsonify({
            'result': round(result, 2),
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_konversi_bp.route('/mata-uang', methods=['POST'])
def konversi_mata_uang():
    """
    Endpoint untuk konversi mata uang menggunakan kurs statis.
    """
    try:
        data = request.json
        amount = float(data['amount'])
        from_currency = data['from_currency']
        to_currency = data['to_currency']
        
        # Kurs statis dengan basis IDR (berdasarkan PRD)
        rates = {
            'IDR': 1,
            'USD': 15750,
            'EUR': 17200,
            'SGD': 11800,
            'MYR': 3500
        }
        
        # Validasi mata uang
        if from_currency not in rates or to_currency not in rates:
            return jsonify({'error': 'Mata uang tidak didukung!'}), 400
            
        # Konversi ke IDR terlebih dahulu
        idr_amount = amount * rates[from_currency]
        
        # Konversi ke mata uang tujuan
        result = idr_amount / rates[to_currency]
        
        steps = [
            f"Jumlah awal: {amount:,.2f} {from_currency}",
            f"Konversi ke IDR: {idr_amount:,.2f} IDR" if from_currency != 'IDR' else "Sudah dalam IDR",
            f"Konversi ke {to_currency}: {result:,.2f} {to_currency}" if to_currency != 'IDR' else "Hasil akhir",
            f"Rate: 1 {to_currency} = {rates[to_currency]:,.0f} IDR"
        ]
        
        formula = f"{amount:,.2f} {from_currency} = {result:,.2f} {to_currency}"
        
        return jsonify({
            'result': round(result, 2),
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400
