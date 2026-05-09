# 🔐 LOGICLAB - Cyber Calculator Terminal

![Version](https://img.shields.io/badge/version-2.0-00ff87?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.8+-00d9ff?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/flask-3.0+-b026ff?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/license-MIT-ff0055?style=for-the-badge)

> **Terminal kalkulator cybersecurity dengan operasi aritmatika, logika digital, dan transformasi bilangan**

Aplikasi web kalkulator canggih dengan tema cybersecurity/hacker aesthetic, dilengkapi dengan sound effects, scan animations, dan matrix rain effect. Dibangun untuk tugas kuliah Teknik Informatika Semester 2.

---

## ✨ Features

### 🔢 Operasi Aritmatika
- ➕ Penjumlahan, Pengurangan, Perkalian, Pembagian
- 🔺 Pangkat, Akar Kuadrat
- 📐 Modulus, Floor Division
- 📊 Langkah-langkah penyelesaian detail

### 🔌 Operasi Logika Digital
- **Logic Gates**: AND, OR, NOT, XOR, NAND, NOR
- **Truth Tables**: Tabel kebenaran otomatis
- **Multi-Base Comparison**: Bandingkan bilangan dari basis berbeda (Binary, Octal, Decimal, Hexadecimal)
- **Circuit Simulator**: Bangun dan evaluasi rangkaian gerbang logika kompleks

### 🔄 Konversi Bilangan
- **Basis Bilangan**: Binary ↔ Octal ↔ Decimal ↔ Hexadecimal
- **Langkah Detail**: Format matematis seperti `(12356)₁₆ = (1 × 16⁴) + (2 × 16³) + (3 × 16²) + (5 × 16¹) + (6 × 16⁰) = (74582)₁₀`
- **Notasi Subscript**: Tampilan profesional dengan subscript basis

### 🌡️ Konversi Suhu
- Celsius, Fahrenheit, Kelvin, Réaumur
- Konversi multi-arah dengan langkah detail

### 💱 Konversi Mata Uang
- IDR, USD, EUR, SGD, MYR
- Kurs statis untuk demonstrasi

### 🎁 Fitur Bonus
- 🔢 Faktorial (n!)
- 📈 Deret Fibonacci

### 🎨 Cybersecurity Theme
- **Matrix Rain Effect**: Efek hujan kode ala Matrix
- **Terminal Aesthetic**: Desain terminal hacker
- **Scan Animations**: Animasi scan cybersecurity
- **Sound Effects**: Efek suara keyboard dan UI
- **Neon Glow**: Efek cahaya neon hijau
- **Dark Mode**: Tema gelap dengan grid cyber

### 📜 Riwayat Perhitungan
- Simpan semua operasi dalam localStorage
- Filter berdasarkan kategori
- Timestamp setiap operasi

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git (untuk version control)

### Installation

1. **Clone repository**
```bash
git clone <repository-url>
cd "Kalkulator Transformasi Bilangan Flask"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run aplikasi**
```bash
python app.py
```

4. **Buka browser**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
Kalkulator Transformasi Bilangan Flask/
│
├── app.py                      # Flask application & API endpoints
├── requirements.txt            # Python dependencies
├── PRD.md                      # Product Requirements Document
├── README.md                   # Documentation
├── .gitignore                  # Git ignore rules
│
├── static/
│   ├── css/
│   │   ├── style.css          # Base styles
│   │   └── cyber-theme.css    # Cybersecurity theme
│   └── js/
│       ├── main.js            # Core JavaScript
│       └── cyber-sound.js     # Sound effects system
│
└── templates/
    ├── base.html              # Base template
    ├── index.html             # Homepage
    ├── aritmatika.html        # Arithmetic operations
    ├── logika.html            # Logic operations
    ├── konversi.html          # Conversion systems
    ├── bonus.html             # Bonus features
    └── riwayat.html           # History page
```

---

## 🎯 API Endpoints

### Aritmatika
```http
POST /api/aritmatika
Content-Type: application/json

{
  "num1": 10,
  "num2": 5,
  "operation": "+"
}
```

### Logic Gates
```http
POST /api/logika/gate
Content-Type: application/json

{
  "gate": "AND",
  "input1": 1,
  "input2": 0
}
```

### Multi-Base Comparison
```http
POST /api/logika/compare
Content-Type: application/json

{
  "num1": "1010",
  "base1": 2,
  "num2": "A",
  "base2": 16,
  "operator": ">"
}
```

### Circuit Simulator
```http
POST /api/logika/circuit
Content-Type: application/json

{
  "gates": [
    {"gate": "AND", "input1": "1", "input2": "0"},
    {"gate": "OR", "input1": "G1", "input2": "1"}
  ]
}
```

### Number Conversion
```http
POST /api/konversi/bilangan
Content-Type: application/json

{
  "number": "12356",
  "from_base": 16,
  "to_base": 10
}
```

### Temperature Conversion
```http
POST /api/konversi/suhu
Content-Type: application/json

{
  "value": 100,
  "from_unit": "C",
  "to_unit": "F"
}
```

### Currency Conversion
```http
POST /api/konversi/mata-uang
Content-Type: application/json

{
  "amount": 1000000,
  "from_currency": "IDR",
  "to_currency": "USD"
}
```

---

## 🎨 Theme Customization

### Color Palette
```css
--cyber-green: #00ff87      /* Primary accent */
--cyber-blue: #00d9ff       /* Secondary accent */
--cyber-purple: #b026ff     /* Tertiary accent */
--cyber-red: #ff0055        /* Error/danger */
--cyber-yellow: #ffea00     /* Warning */
--matrix-bg: #0a0e27        /* Background */
--terminal-bg: #000000      /* Terminal black */
```

### Fonts
- **Display**: Orbitron (Headers, titles)
- **Body**: Rajdhani (Regular text)
- **Monospace**: Share Tech Mono (Code, terminal)

---

## 🔊 Sound Effects

Sound effects menggunakan Web Audio API untuk:
- **Keyboard clicks**: Saat mengetik
- **Button hovers**: Saat hover tombol
- **Button clicks**: Saat klik tombol
- **Success**: Operasi berhasil
- **Error**: Terjadi kesalahan
- **Scan**: Efek scan cybersecurity
- **Processing**: Saat memproses data

Toggle sound dengan tombol speaker di navbar.

---

## 🎮 Usage Examples

### 1. Konversi Hexadecimal ke Decimal
```
Input: 12356 (base 16)
Output: 74582 (base 10)

Langkah:
(12356)₁₆ = (1 × 16⁴) + (2 × 16³) + (3 × 16²) + (5 × 16¹) + (6 × 16⁰)
         = (1 × 65536) + (2 × 4096) + (3 × 256) + (5 × 16) + (6 × 1)
         = 65536 + 8192 + 768 + 80 + 6
         = (74582)₁₀
```

### 2. Logic Circuit
```
Gate 1: AND(1, 0) = 0
Gate 2: OR(G1, 1) = 1
Gate 3: NOT(G2) = 0
Final Output: 0
```

### 3. Multi-Base Comparison
```
Compare: (1010)₂ > (A)₁₆
Step 1: (1010)₂ = 10 (decimal)
Step 2: (A)₁₆ = 10 (decimal)
Result: 10 > 10 = FALSE
```

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] Semua operasi aritmatika berjalan
- [ ] Logic gates menghasilkan output benar
- [ ] Truth tables akurat
- [ ] Multi-base comparison valid
- [ ] Circuit simulator evaluasi benar
- [ ] Number conversion akurat
- [ ] Temperature conversion benar
- [ ] Currency conversion sesuai rate
- [ ] History tersimpan di localStorage
- [ ] Dark mode berfungsi
- [ ] Sound effects aktif
- [ ] Responsive di mobile
- [ ] Matrix rain effect smooth

---

## 📱 Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 90+     | ✅ Full Support |
| Edge    | 90+     | ✅ Full Support |
| Firefox | 88+     | ✅ Full Support |
| Safari  | 14+     | ⚠️ Partial (no Web Audio) |

---

## 🐛 Known Issues

1. **Matrix rain effect**: Dapat berat pada device low-end (optional, bisa dimatikan)
2. **Sound effects**: Tidak support di Safari iOS
3. **Web Audio API**: Memerlukan user interaction pertama kali

---

## 🔮 Future Enhancements

- [ ] Scientific calculator mode
- [ ] Graph plotter untuk fungsi matematika
- [ ] Export hasil ke PDF
- [ ] Database untuk persistent storage
- [ ] User authentication
- [ ] Real-time currency API
- [ ] More logic gate types (XNOR, etc)
- [ ] Binary arithmetic operations
- [ ] Bitwise operations
- [ ] Custom color themes

---

## 📚 Technologies Used

### Backend
- **Flask 3.0+**: Web framework
- **Python 3.8+**: Programming language

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling dengan custom properties
- **JavaScript ES6+**: Interactivity
- **Bootstrap 5.3**: UI framework
- **Bootstrap Icons**: Icon library

### APIs
- **Web Audio API**: Sound effects
- **Canvas API**: Matrix rain effect
- **LocalStorage API**: History persistence

---

## 👨‍💻 Development

### Setup Development Environment
```bash
# Clone repository
git clone <repo-url>
cd "Kalkulator Transformasi Bilangan Flask"

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run in debug mode
python app.py
```

### Git Workflow
```bash
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "feat: add new feature"

# View log
git log --oneline
```

### Commit Message Convention
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Testing
- `chore:` Maintenance

---

## 📄 License

MIT License - feel free to use for educational purposes.

---

## 👥 Credits

**Developed by**: LogicLab Team  
**Course**: Pengantar Pemrograman  
**Semester**: 2  
**Year**: 2026  
**Institution**: Teknik Informatika

---

## 🙏 Acknowledgments

- **Matrix Theme**: Inspired by The Matrix movie
- **Cybersecurity Aesthetic**: Inspired by hacker terminals
- **Sound Design**: Web Audio API examples
- **UI/UX**: Modern terminal interfaces

---

## 📞 Support

Jika ada pertanyaan atau issues:
1. Check documentation di PRD.md
2. Review code comments
3. Test di browser berbeda
4. Check console untuk errors

---

## 🎓 Educational Purpose

Aplikasi ini dibuat untuk tujuan edukasi dalam mata kuliah Pengantar Pemrograman. Mendemonstrasikan:
- Flask web development
- RESTful API design
- Frontend-backend integration
- Modern UI/UX design
- Git version control
- Project documentation

---

<div align="center">

### 🔐 LOGICLAB - Where Logic Meets Cybersecurity

**[SYSTEM INITIALIZED]** • **[SECURE CONNECTION]** • **[READY FOR OPERATIONS]**

Made with 💚 and ⚡ by LogicLab Team

</div>
