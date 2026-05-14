"""
Modul Logic Utils
-----------------
Modul ini menangani operasi logika dan simulasi rangkaian gerbang logika.
Tujuannya adalah memisahkan kompleksitas evaluasi logika dari kode routing.
"""

from utils.conversion_utils import convert_to_decimal

def compare_numbers(num1_str, base1, num2_str, base2, operator):
    """
    Membandingkan dua buah angka dalam basis yang berbeda (atau sama).
    
    Args:
        num1_str (str): Angka pertama.
        base1 (int): Basis angka pertama.
        num2_str (str): Angka kedua.
        base2 (int): Basis angka kedua.
        operator (str): Operator perbandingan (>, <, >=, <=, ==, !=).
        
    Returns:
        tuple: (hasil_boolean, daftar_langkah, rumus)
    """
    # Mengubah kedua angka ke desimal terlebih dahulu untuk kemudahan perbandingan
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
    """
    Mengaplikasikan operasi gerbang logika pada 1 atau 2 input.
    
    Args:
        gate (str): Jenis gerbang logika (AND, OR, NOT, XOR, NAND, NOR).
        input1 (int/str): Input pertama (biasanya 0 atau 1).
        input2 (int/str, optional): Input kedua (0 atau 1).
        
    Returns:
        tuple: (hasil_integer_0_atau_1, rumus)
    """
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
    """
    Mengevaluasi keseluruhan rangkaian gerbang logika yang saling terhubung.
    
    Args:
        gates_data (list): Daftar dictionary yang mendeskripsikan setiap gerbang
                           serta dari mana inputnya berasal (misal 'G1' atau '1').
                           
    Returns:
        tuple: (hasil_akhir_rangkaian, daftar_langkah)
    """
    steps = []
    results = {}
    
    for i, gate_info in enumerate(gates_data):
        gate = gate_info['gate']
        input1_ref = gate_info['input1']
        input2_ref = gate_info.get('input2', None)
        
        # Menyelesaikan asal usul input1 (bisa dari input langsung atau dari gerbang sebelumnya)
        if input1_ref.startswith('G'):
            gate_num = int(input1_ref[1:])
            input1 = results.get(f'G{gate_num}', 0)
        else:
            input1 = int(input1_ref)
        
        # Menyelesaikan asal usul input2
        if input2_ref and input2_ref.startswith('G'):
            gate_num = int(input2_ref[1:])
            input2 = results.get(f'G{gate_num}', 0)
        elif input2_ref:
            input2 = int(input2_ref)
        else:
            input2 = None
        
        # Menerapkan evaluasi gerbang logika
        result, formula = apply_logic_gate(gate, input1, input2)
        gate_id = f'G{i+1}'
        results[gate_id] = result
        
        steps.append(f"{gate_id}: {formula} = {result}")
    
    # Hasil akhir adalah output dari gerbang yang terakhir dieksekusi
    final_result = results[f'G{len(gates_data)}'] if gates_data else 0
    
    return final_result, steps
