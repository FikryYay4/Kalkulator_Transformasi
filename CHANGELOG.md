# Changelog

All notable changes to LogicLab Cyber Calculator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-05-09

### Added
- 🎨 **Cybersecurity Theme**: Matrix-inspired dark theme dengan neon green accents
- 🔊 **Sound Effects System**: Web Audio API untuk keyboard clicks, button sounds, dan UI feedback
- 🎬 **Scan Animations**: Cybersecurity-style scan lines dan hologram effects
- 🌧️ **Matrix Rain Effect**: Falling code animation di background (optional)
- 🔌 **Enhanced Logic Gates**: 
  - Multi-base comparison (Binary, Octal, Decimal, Hexadecimal)
  - Circuit builder untuk rangkaian gerbang logika kompleks
  - Truth tables otomatis untuk setiap gerbang
- 📐 **Detailed Conversion Steps**: 
  - Format matematis lengkap seperti `(12356)₁₆ = (1 × 16⁴) + (2 × 16³) + ... = (74582)₁₀`
  - Subscript notation untuk basis bilangan
  - Step-by-step explanation untuk setiap konversi
- 🎯 **Quick Access Terminal**: Shortcut panel di homepage
- 📊 **System Info Panel**: Status dan informasi sistem
- 🔐 **Security Indicators**: Visual indicators untuk secure connection
- 📱 **Improved Mobile Responsive**: Better touch targets dan layout
- 🎨 **Custom Fonts**: Orbitron, Rajdhani, Share Tech Mono untuk terminal aesthetic
- ⚡ **Performance Optimizations**: Lazy loading dan efficient animations

### Changed
- 🎨 **Complete UI Redesign**: From modern clean to cybersecurity terminal
- 🏷️ **Rebranding**: KalkulatorPro → LogicLab
- 🎨 **Color Scheme**: Purple gradients → Cyber green/blue/purple
- 📝 **Typography**: Inter → Orbitron/Rajdhani/Share Tech Mono
- 🔘 **Button Styles**: Rounded modern → Terminal cyber buttons
- 📊 **Result Display**: Card-based → Terminal output style
- 🎯 **Navigation**: Standard navbar → Cyber terminal navbar

### Enhanced
- 🔢 **Number Conversion**: Added detailed mathematical notation
- 🔌 **Logic Operations**: Extended to support multi-base inputs
- 📜 **History System**: Better categorization dan filtering
- 🎨 **Animations**: Smoother transitions dan cyber effects
- 📱 **Accessibility**: Better contrast ratios dan keyboard navigation

### Fixed
- 🐛 Input validation untuk semua basis bilangan
- 🐛 Error handling yang lebih robust
- 🐛 Mobile touch event conflicts
- 🐛 Theme persistence di localStorage
- 🐛 History overflow pada mobile devices

### Technical
- 📦 **Git Integration**: Version control setup dengan proper .gitignore
- 📝 **Documentation**: Comprehensive README.md dan CHANGELOG.md
- 🏗️ **Code Structure**: Modular CSS dan JavaScript
- 🎨 **CSS Architecture**: Separate cyber-theme.css untuk maintainability
- 🔊 **Audio System**: Dedicated cyber-sound.js module
- 🧪 **Testing**: Manual testing checklist

## [1.0.0] - 2026-04-XX

### Added
- ➕ Basic arithmetic operations (add, subtract, multiply, divide)
- 🔺 Advanced math (power, square root, modulus, floor division)
- 🔌 Logic gates (AND, OR, NOT, XOR, NAND, NOR)
- 🔄 Number base conversion (Binary, Octal, Decimal, Hexadecimal)
- 🌡️ Temperature conversion (Celsius, Fahrenheit, Kelvin, Réaumur)
- 💱 Currency conversion (IDR, USD, EUR, SGD, MYR)
- 🎁 Bonus features (Factorial, Fibonacci)
- 📜 History system dengan localStorage
- 🌓 Dark/Light mode toggle
- 📱 Responsive design dengan Bootstrap 5
- 🎨 Modern gradient UI
- 📊 Step-by-step explanations

### Technical
- ⚙️ Flask 3.0+ backend
- 🎨 Bootstrap 5.3 frontend
- 📝 Jinja2 templating
- 💾 LocalStorage untuk history
- 🎨 CSS custom properties untuk theming

---

## Future Roadmap

### Version 2.1.0 (Planned)
- [ ] Scientific calculator mode
- [ ] Graph plotter untuk fungsi matematika
- [ ] Binary arithmetic operations (ADD, SUB dengan carry)
- [ ] Bitwise operations (AND, OR, XOR, NOT, shift)
- [ ] More logic gate types (XNOR, Buffer, Tri-state)
- [ ] Custom color theme builder

### Version 2.2.0 (Planned)
- [ ] Export hasil ke PDF
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication system
- [ ] Real-time currency API integration
- [ ] Calculation sharing via URL
- [ ] Keyboard shortcuts

### Version 3.0.0 (Future)
- [ ] Multi-language support (EN, ID)
- [ ] API documentation dengan Swagger
- [ ] Mobile app (React Native/Flutter)
- [ ] Collaborative calculations
- [ ] Cloud sync
- [ ] Advanced analytics

---

## Contributors

- **LogicLab Team** - Initial work and cybersecurity theme
- **Teknik Informatika Semester 2** - Educational project

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
