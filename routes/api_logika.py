from flask import Blueprint, request, jsonify
from utils import validate_base_number, compare_numbers, apply_logic_gate, evaluate_circuit

api_logika_bp = Blueprint('api_logika', __name__)

@api_logika_bp.route('/gate', methods=['POST'])
def logika_gate():
    """
    Endpoint untuk operasi gerbang logika sederhana (1 atau 2 input).
    """
    try:
        data = request.json
        gate = data['gate']
        input1 = int(data['input1'])
        input2 = int(data.get('input2', 0))
        
        result, formula = apply_logic_gate(gate, input1, input2)
        
        steps = [
            f"Gerbang: {gate}",
            f"Input 1: {input1}",
            f"Input 2: {input2}" if gate != 'NOT' else "Input 2: (tidak digunakan)",
            f"Output: {result}"
        ]
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_logika_bp.route('/compare', methods=['POST'])
def logika_compare():
    """
    Endpoint untuk membandingkan dua bilangan (bisa beda basis).
    """
    try:
        data = request.json
        num1 = data['num1'].strip()
        base1 = int(data['base1'])
        num2 = data['num2'].strip()
        base2 = int(data['base2'])
        operator = data['operator']
        
        # Validasi bilangan sesuai basisnya
        if not validate_base_number(num1, base1):
            return jsonify({'error': f'Angka 1 tidak valid untuk basis {base1}!'}), 400
        if not validate_base_number(num2, base2):
            return jsonify({'error': f'Angka 2 tidak valid untuk basis {base2}!'}), 400
        
        result, steps, formula = compare_numbers(num1, base1, num2, base2, operator)
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_logika_bp.route('/circuit', methods=['POST'])
def logika_circuit():
    """
    Endpoint untuk mensimulasikan rangkaian gerbang logika yang kompleks.
    """
    try:
        data = request.json
        gates = data['gates']
        
        if not gates:
            return jsonify({'error': 'Tambahkan minimal 1 gerbang!'}), 400
        
        result, steps = evaluate_circuit(gates)
        
        formula = f"Rangkaian {len(gates)} gerbang"
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400
