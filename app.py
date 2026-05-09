from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)
app.secret_key = 'kalkulatorpro-secret-key-2026'


# ===== HELPER FUNCTIONS =====

def validate_base_number(num_str, base):
    """Validate if number string is valid for given base"""
    num_str = str(num_str).upper().strip()
    valid_chars = '0123456789ABCDEF'[:base]
    return all(c in valid_chars for c in num_str)


def convert_to_decimal(num_str, from_base):
    """Convert any base to decimal with detailed steps"""
    num_str = str(num_str).upper().strip()
    steps = []
    result = 0
    
    # Generate step-by-step calculation
    terms = []
    for i, digit in enumerate(num_str):
        position = len(num_str) - 1 - i
        digit_value = int(digit, from_base)
        term_value = digit_value * (from_base ** position)
        result += term_value
        
        if from_base == 16:
            digit_display = digit
        else:
            digit_display = digit
            
        terms.append(f"({digit_display} × {from_base}^{position})")
        steps.append(f"Posisi {position}: {digit_display} × {from_base}^{position} = {digit_value} × {from_base**position} = {term_value}")
    
    # Create formula like: (12356)₁₆ = (1 × 16⁴) + (2 × 16³) + ...
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    formula = f"({num_str}){base_subscript.get(from_base, f'_{from_base}')} = {' + '.join(terms)} = ({result}){base_subscript[10]}"
    
    return result, steps, formula


def convert_from_decimal(num, to_base):
    """Convert decimal to any base with detailed steps"""
    if num == 0:
        return '0', ['0 dalam basis apapun adalah 0'], f"(0)₁₀ = (0)_{to_base}"
    
    steps = []
    result = []
    original = num
    
    digits = '0123456789ABCDEF'
    
    while num > 0:
        remainder = num % to_base
        quotient = num // to_base
        result.append(digits[remainder])
        steps.append(f"{num} ÷ {to_base} = {quotient} sisa {remainder} → digit: {digits[remainder]}")
        num = quotient
    
    result.reverse()
    result_str = ''.join(result)
    
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    formula = f"({original})₁₀ = ({result_str}){base_subscript.get(to_base, f'_{to_base}')}"
    
    return result_str, steps, formula


def convert_base_to_base(num_str, from_base, to_base):
    """Convert from any base to any base"""
    # First convert to decimal
    decimal_val, steps1, formula1 = convert_to_decimal(num_str, from_base)
    
    # Then convert to target base
    if to_base == 10:
        return str(decimal_val), steps1, formula1
    
    result_str, steps2, formula2 = convert_from_decimal(decimal_val, to_base)
    
    # Combine steps
    all_steps = steps1 + ['', f'Hasil desimal: {decimal_val}', ''] + steps2
    
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    combined_formula = f"({num_str}){base_subscript.get(from_base, f'_{from_base}')} → ({decimal_val})₁₀ → ({result_str}){base_subscript.get(to_base, f'_{to_base}')}"
    
    return result_str, all_steps, combined_formula


def compare_numbers(num1_str, base1, num2_str, base2, operator):
    """Compare two numbers in any base"""
    # Convert both to decimal
    val1, _, _ = convert_to_decimal(num1_str, base1)
    val2, _, _ = convert_to_decimal(num2_str, base2)
    
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    
    if operator == '>':
        result = val1 > val2
        symbol = '>'
    elif operator == '<':
        result = val1 < val2
        symbol = '<'
    elif operator == '>=':
        result = val1 >= val2
        symbol = '≥'
    elif operator == '<=':
        result = val1 <= val2
        symbol = '≤'
    elif operator == '==':
        result = val1 == val2
        symbol = '='
    elif operator == '!=':
        result = val1 != val2
        symbol = '≠'
    else:
        result = False
        symbol = '?'
    
    steps = [
        f"Konversi ({num1_str}){base_subscript.get(base1, f'_{base1}')} ke desimal: {val1}",
        f"Konversi ({num2_str}){base_subscript.get(base2, f'_{base2}')} ke desimal: {val2}",
        f"Bandingkan: {val1} {symbol} {val2}",
        f"Hasil: {'BENAR (TRUE)' if result else 'SALAH (FALSE)'}"
    ]
    
    formula = f"({num1_str}){base_subscript.get(base1, f'_{base1}')} {symbol} ({num2_str}){base_subscript.get(base2, f'_{base2}')} = {val1} {symbol} {val2}"
    
    return result, steps, formula


def apply_logic_gate(gate, input1, input2=None):
    """Apply logic gate operation"""
    input1 = bool(int(input1))
    if input2 is not None:
        input2 = bool(int(input2))
    
    if gate == 'AND':
        result = input1 and input2
        formula = f"{int(input1)} AND {int(input2)} = {int(result)}"
    elif gate == 'OR':
        result = input1 or input2
        formula = f"{int(input1)} OR {int(input2)} = {int(result)}"
    elif gate == 'NOT':
        result = not input1
        formula = f"NOT {int(input1)} = {int(result)}"
    elif gate == 'XOR':
        result = input1 != input2
        formula = f"{int(input1)} XOR {int(input2)} = {int(result)}"
    elif gate == 'NAND':
        result = not (input1 and input2)
        formula = f"{int(input1)} NAND {int(input2)} = {int(result)}"
    elif gate == 'NOR':
        result = not (input1 or input2)
        formula = f"{int(input1)} NOR {int(input2)} = {int(result)}"
    else:
        result = False
        formula = "Unknown gate"
    
    return int(result), formula


def evaluate_circuit(gates_data):
    """Evaluate a circuit of logic gates"""
    steps = []
    results = {}
    
    for i, gate_info in enumerate(gates_data):
        gate = gate_info['gate']
        input1_ref = gate_info['input1']
        input2_ref = gate_info.get('input2', None)
        
        # Resolve input1
        if input1_ref.startswith('G'):
            gate_num = int(input1_ref[1:])
            input1 = results.get(f'G{gate_num}', 0)
        else:
            input1 = int(input1_ref)
        
        # Resolve input2
        if input2_ref and input2_ref.startswith('G'):
            gate_num = int(input2_ref[1:])
            input2 = results.get(f'G{gate_num}', 0)
        elif input2_ref:
            input2 = int(input2_ref)
        else:
            input2 = None
        
        # Apply gate
        result, formula = apply_logic_gate(gate, input1, input2)
        gate_id = f'G{i+1}'
        results[gate_id] = result
        
        steps.append(f"{gate_id}: {formula} = {result}")
    
    final_result = results[f'G{len(gates_data)}'] if gates_data else 0
    
    return final_result, steps


# ===== ROUTES =====

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aritmatika')
def aritmatika():
    return render_template('aritmatika.html')


@app.route('/logika')
def logika():
    return render_template('logika.html')


@app.route('/konversi')
def konversi():
    return render_template('konversi.html')


@app.route('/bonus')
def bonus():
    return render_template('bonus.html')


@app.route('/riwayat')
def riwayat():
    return render_template('riwayat.html')


# ===== API ENDPOINTS =====

@app.route('/api/aritmatika', methods=['POST'])
def api_aritmatika():
    try:
        data = request.json
        num1 = float(data['num1'])
        num2 = float(data.get('num2', 0))
        operation = data['operation']
        
        steps = []
        
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


@app.route('/api/konversi/bilangan', methods=['POST'])
def api_konversi_bilangan():
    try:
        data = request.json
        number = data['number'].strip()
        from_base = int(data['from_base'])
        to_base = int(data['to_base'])
        
        # Validate base
        if from_base not in [2, 8, 10, 16] or to_base not in [2, 8, 10, 16]:
            return jsonify({'error': 'Basis harus 2, 8, 10, atau 16!'}), 400
        
        # Validate number for base
        if not validate_base_number(number, from_base):
            return jsonify({'error': f'Angka tidak valid untuk basis {from_base}!'}), 400
        
        # Convert
        result, steps, formula = convert_base_to_base(number, from_base, to_base)
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/logika/gate', methods=['POST'])
def api_logika_gate():
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


@app.route('/api/logika/compare', methods=['POST'])
def api_logika_compare():
    try:
        data = request.json
        num1 = data['num1'].strip()
        base1 = int(data['base1'])
        num2 = data['num2'].strip()
        base2 = int(data['base2'])
        operator = data['operator']
        
        # Validate
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


@app.route('/api/logika/circuit', methods=['POST'])
def api_logika_circuit():
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


@app.route('/api/konversi/suhu', methods=['POST'])
def api_konversi_suhu():
    try:
        data = request.json
        value = float(data['value'])
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        
        # Convert to Celsius first
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
        
        # Convert from Celsius to target
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


@app.route('/api/konversi/mata-uang', methods=['POST'])
def api_konversi_mata_uang():
    try:
        data = request.json
        amount = float(data['amount'])
        from_currency = data['from_currency']
        to_currency = data['to_currency']
        
        # Static exchange rates (IDR base)
        rates = {
            'IDR': 1,
            'USD': 15750,
            'EUR': 17200,
            'SGD': 11800,
            'MYR': 3500
        }
        
        # Convert to IDR first
        idr_amount = amount * rates[from_currency]
        
        # Convert to target currency
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


@app.route('/api/bonus/faktorial', methods=['POST'])
def api_bonus_faktorial():
    try:
        data = request.json
        n = int(data['n'])
        
        if n < 0:
            return jsonify({'error': 'Faktorial tidak terdefinisi untuk bilangan negatif!'}), 400
        if n > 170:
            return jsonify({'error': 'Angka terlalu besar!'}), 400
        
        result = math.factorial(n)
        
        steps = []
        if n == 0 or n == 1:
            steps.append(f"{n}! = 1")
        else:
            terms = ' × '.join(str(i) for i in range(n, 0, -1))
            steps.append(f"{n}! = {terms}")
            steps.append(f"Hasil: {result}")
        
        formula = f"{n}!"
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/bonus/fibonacci', methods=['POST'])
def api_bonus_fibonacci():
    try:
        data = request.json
        n = int(data['n'])
        
        if n < 1:
            return jsonify({'error': 'N harus >= 1!'}), 400
        if n > 50:
            return jsonify({'error': 'N terlalu besar!'}), 400
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        result = fib[:n]
        
        steps = [f"F(1) = 0", f"F(2) = 1"]
        for i in range(2, n):
            steps.append(f"F({i+1}) = F({i}) + F({i-1}) = {fib[i-1]} + {fib[i-2]} = {fib[i]}")
        
        formula = f"Fibonacci({n})"
        
        return jsonify({
            'result': result,
            'formula': formula,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
