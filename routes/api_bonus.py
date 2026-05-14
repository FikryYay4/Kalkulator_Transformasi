import math
from flask import Blueprint, request, jsonify

api_bonus_bp = Blueprint('api_bonus', __name__)

@api_bonus_bp.route('/faktorial', methods=['POST'])
def bonus_faktorial():
    """
    Endpoint untuk menghitung faktorial sebuah bilangan (n!).
    """
    try:
        data = request.json
        n = int(data['n'])
        
        if n < 0:
            return jsonify({'error': 'Faktorial tidak terdefinisi untuk bilangan negatif!'}), 400
        if n > 170:
            # 170! adalah batas atas standar untuk tipe data float 64-bit sebelum infinity
            return jsonify({'error': 'Angka terlalu besar!'}), 400
        
        result = math.factorial(n)
        
        steps = []
        if n == 0 or n == 1:
            steps.append(f"{n}! = 1")
        else:
            terms = ' × '.join(str(i) for i in range(n, 0, -1))
            # Jika suku terlalu panjang, potong
            if len(terms) > 100:
                terms = f"{n} × {n-1} × ... × 2 × 1"
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


@api_bonus_bp.route('/fibonacci', methods=['POST'])
def bonus_fibonacci():
    """
    Endpoint untuk membuat deret Fibonacci hingga ke-N.
    """
    try:
        data = request.json
        n = int(data['n'])
        
        if n < 1:
            return jsonify({'error': 'N harus >= 1!'}), 400
        if n > 50:
            return jsonify({'error': 'N terlalu besar!'}), 400
        
        # Mencari deret fibonacci
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        # Potong sesuai panjang N yang diminta
        result = fib[:n]
        
        steps = [f"F(1) = 0"]
        if n >= 2:
            steps.append(f"F(2) = 1")
            
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
