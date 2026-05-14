import math
from flask import Blueprint, request, jsonify

api_aritmatika_bp = Blueprint('api_aritmatika', __name__)

@api_aritmatika_bp.route('/', methods=['POST'])
def hitung_aritmatika():
    """
    Endpoint API untuk operasi aritmatika.
    Menerima JSON dengan format:
    { "num1": 10, "num2": 5, "operation": "+" }
    """
    try:
        data = request.json
        num1 = float(data['num1'])
        num2 = float(data.get('num2', 0))
        operation = data['operation']
        
        steps = []
        
        # Mengecek operasi yang diminta
        if operation == '+':
            result = num1 + num2
            formula = f"{num1} + {num2}"
            steps.append(f"Penjumlahan: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            formula = f"{num1} - {num2}"
            steps.append(f"Pengurangan: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            formula = f"{num1} × {num2}"
            steps.append(f"Perkalian: {num1} × {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Tidak bisa dibagi dengan nol!'}), 400
            result = num1 / num2
            formula = f"{num1} ÷ {num2}"
            steps.append(f"Pembagian: {num1} ÷ {num2} = {result}")
        elif operation == '**':
            result = num1 ** num2
            formula = f"{num1}^{num2}"
            steps.append(f"Pangkat: {num1}^{num2} = {result}")
        elif operation == 'sqrt':
            if num1 < 0:
                return jsonify({'error': 'Tidak bisa akar dari bilangan negatif!'}), 400
            result = math.sqrt(num1)
            formula = f"√{num1}"
            steps.append(f"Akar kuadrat: √{num1} = {result}")
        elif operation == '%':
            result = num1 % num2
            formula = f"{num1} mod {num2}"
            steps.append(f"Modulus: {num1} mod {num2} = {result}")
        elif operation == '//':
            result = num1 // num2
            formula = f"{num1} // {num2}"
            steps.append(f"Floor division: {num1} // {num2} = {result}")
        else:
            return jsonify({'error': 'Operasi tidak valid!'}), 400
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400
