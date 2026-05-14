"""
Modul Conversion Utils
----------------------
Modul ini berisi fungsi-fungsi pembantu untuk mengelola logika transformasi atau konversi bilangan.
Dibuat modular agar mudah di-maintain dan di-testing secara terpisah.
"""

def validate_base_number(num_str, base):
    """
    Memvalidasi apakah string angka sesuai dengan basis yang diberikan.
    
    Args:
        num_str (str): String angka yang akan divalidasi.
        base (int): Basis bilangan (2, 8, 10, atau 16).
        
    Returns:
        bool: True jika valid, False jika tidak valid.
    """
    num_str = str(num_str).upper().strip()
    valid_chars = '0123456789ABCDEF'[:base]
    return all(c in valid_chars for c in num_str)


def convert_to_decimal(num_str, from_base):
    """
    Mengonversi bilangan dari basis apa pun ke desimal beserta langkah penyelesaiannya.
    
    Args:
        num_str (str): String angka yang akan dikonversi.
        from_base (int): Basis asal bilangan tersebut.
        
    Returns:
        tuple: (hasil_desimal, daftar_langkah, string_rumus)
    """
    num_str = str(num_str).upper().strip()
    steps = []
    result = 0
    
    # Membuat perhitungan langkah demi langkah
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
    
    # Membuat string rumus contoh: (12356)₁₆ = (1 × 16⁴) + (2 × 16³) + ...
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    formula = f"({num_str}){base_subscript.get(from_base, f'_{from_base}')} = {' + '.join(terms)} = ({result}){base_subscript[10]}"
    
    return result, steps, formula


def convert_from_decimal(num, to_base):
    """
    Mengonversi bilangan desimal ke basis tujuan beserta langkah penyelesaiannya.
    
    Args:
        num (int): Nilai desimal yang akan dikonversi.
        to_base (int): Basis tujuan konversi.
        
    Returns:
        tuple: (hasil_string, daftar_langkah, string_rumus)
    """
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
    """
    Mengonversi bilangan dari basis asal ke basis tujuan mana pun.
    Fungsi ini melakukan konversi ke desimal terlebih dahulu sebagai perantara.
    
    Args:
        num_str (str): String angka asal.
        from_base (int): Basis asal angka tersebut.
        to_base (int): Basis tujuan konversi.
        
    Returns:
        tuple: (hasil_string, daftar_langkah_gabungan, rumus_gabungan)
    """
    # 1. Konversi ke desimal sebagai jembatan
    decimal_val, steps1, formula1 = convert_to_decimal(num_str, from_base)
    
    # Jika tujuan akhirnya desimal, langsung return
    if to_base == 10:
        return str(decimal_val), steps1, formula1
    
    # 2. Konversi dari desimal ke basis tujuan
    result_str, steps2, formula2 = convert_from_decimal(decimal_val, to_base)
    
    # Gabungkan langkah penyelesaian
    all_steps = steps1 + ['', f'Hasil desimal perantara: {decimal_val}', ''] + steps2
    
    base_subscript = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
    combined_formula = f"({num_str}){base_subscript.get(from_base, f'_{from_base}')} → ({decimal_val})₁₀ → ({result_str}){base_subscript.get(to_base, f'_{to_base}')}"
    
    return result_str, all_steps, combined_formula
