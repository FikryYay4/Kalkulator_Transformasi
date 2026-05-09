# 🚀 Installation Guide - LogicLab

Panduan lengkap instalasi dan setup LogicLab Cyber Calculator Terminal.

---

## 📋 Prerequisites

Sebelum memulai, pastikan sistem Anda memiliki:

### Required
- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (included with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Recommended
- **Virtual Environment** - Untuk isolasi dependencies
- **Modern Browser** - Chrome 90+, Firefox 88+, atau Edge 90+
- **Code Editor** - VS Code, PyCharm, atau editor favorit Anda

### System Requirements
- **OS**: Windows 10/11, macOS 10.14+, atau Linux
- **RAM**: Minimal 2GB (4GB recommended)
- **Storage**: 100MB free space
- **Internet**: Untuk download dependencies

---

## 🔧 Installation Steps

### Method 1: Quick Start (Recommended)

#### Windows
```cmd
# 1. Clone repository
git clone <repository-url>
cd "Kalkulator Transformasi Bilangan Flask"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run application
python app.py

# 4. Open browser
start http://localhost:5000
```

#### macOS/Linux
```bash
# 1. Clone repository
git clone <repository-url>
cd "Kalkulator Transformasi Bilangan Flask"

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Run application
python3 app.py

# 4. Open browser
open http://localhost:5000  # macOS
xdg-open http://localhost:5000  # Linux
```

### Method 2: With Virtual Environment (Best Practice)

#### Windows
```cmd
# 1. Clone repository
git clone <repository-url>
cd "Kalkulator Transformasi Bilangan Flask"

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
python app.py
```

#### macOS/Linux
```bash
# 1. Clone repository
git clone <repository-url>
cd "Kalkulator Transformasi Bilangan Flask"

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
python app.py
```

---

## 📦 Dependencies

File `requirements.txt` berisi:

```txt
Flask==3.0.0
Werkzeug==3.0.1
```

### Installing Individual Packages

Jika ingin install manual:

```bash
pip install Flask==3.0.0
pip install Werkzeug==3.0.1
```

---

## ⚙️ Configuration

### Port Configuration

Default port adalah `5000`. Untuk mengubah:

**Edit `app.py`:**
```python
if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Change to your preferred port
```

### Debug Mode

**Production:**
```python
app.run(debug=False, port=5000)
```

**Development:**
```python
app.run(debug=True, port=5000)
```

### Host Configuration

**Local only (default):**
```python
app.run(debug=True, host='127.0.0.1', port=5000)
```

**Network accessible:**
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🧪 Verification

### 1. Check Python Version
```bash
python --version
# Should show: Python 3.8.x or higher
```

### 2. Check Flask Installation
```bash
python -c "import flask; print(flask.__version__)"
# Should show: 3.0.0 or higher
```

### 3. Test Application
```bash
python app.py
```

Expected output:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

### 4. Test in Browser

Open `http://localhost:5000` dan verify:
- ✅ Homepage loads dengan tema cyber
- ✅ Matrix rain effect aktif (dark theme)
- ✅ Sound effects berfungsi (klik tombol sound)
- ✅ Navigation ke semua halaman
- ✅ Operasi aritmatika berjalan
- ✅ Logic gates berfungsi
- ✅ Konversi bilangan akurat
- ✅ History tersimpan

---

## 🐛 Troubleshooting

### Problem: "Python not found"

**Solution:**
```bash
# Windows: Add Python to PATH
# Or use full path
C:\Python39\python.exe app.py

# macOS/Linux: Use python3
python3 app.py
```

### Problem: "pip not found"

**Solution:**
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### Problem: "Port 5000 already in use"

**Solution 1: Kill process**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

**Solution 2: Change port**
```python
# Edit app.py
app.run(debug=True, port=8080)
```

### Problem: "Module not found"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Or install individually
pip install Flask Werkzeug
```

### Problem: "Permission denied"

**Solution:**
```bash
# Windows: Run as Administrator
# macOS/Linux: Use sudo
sudo pip install -r requirements.txt
```

### Problem: "Virtual environment not activating"

**Solution:**
```bash
# Windows PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

# Windows CMD
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

### Problem: "Sound effects not working"

**Cause:** Browser tidak support Web Audio API atau user belum interact

**Solution:**
- Klik tombol sound toggle di navbar
- Refresh halaman
- Gunakan browser modern (Chrome/Firefox/Edge)

### Problem: "Matrix rain effect laggy"

**Solution:**
- Disable matrix rain di `base.html` (comment out `createMatrixRain()`)
- Reduce canvas resolution
- Use more powerful device

---

## 🔄 Updating

### Pull Latest Changes
```bash
git pull origin master
pip install -r requirements.txt --upgrade
```

### Check for Updates
```bash
git fetch
git status
```

---

## 🗑️ Uninstallation

### Remove Virtual Environment
```bash
# Deactivate first
deactivate

# Remove directory
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

### Remove Application
```bash
cd ..
rm -rf "Kalkulator Transformasi Bilangan Flask"  # macOS/Linux
rmdir /s "Kalkulator Transformasi Bilangan Flask"  # Windows
```

---

## 📚 Next Steps

After successful installation:

1. **Read Documentation**: Check `README.md` untuk features
2. **Explore Features**: Test semua operasi
3. **Customize Theme**: Edit `cyber-theme.css`
4. **Check API**: Review API endpoints di `app.py`
5. **Report Issues**: Create issue jika ada bug

---

## 💡 Tips

### Development Tips
- Use virtual environment untuk isolasi
- Enable debug mode saat development
- Check console untuk errors
- Use browser DevTools untuk debugging

### Performance Tips
- Disable matrix rain jika laggy
- Clear localStorage jika history terlalu banyak
- Use modern browser untuk best performance
- Close unused tabs

### Security Tips
- Jangan expose ke internet tanpa proper security
- Change secret key di production
- Disable debug mode di production
- Use HTTPS jika deploy

---

## 🆘 Getting Help

Jika masih ada masalah:

1. **Check Documentation**: README.md, PRD.md
2. **Review Code**: Check comments di source code
3. **Test Browser**: Try different browser
4. **Check Console**: Browser console dan terminal output
5. **Search Issues**: Google error message

---

## ✅ Installation Checklist

- [ ] Python 3.8+ installed
- [ ] pip working
- [ ] Git installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] Application runs
- [ ] Browser opens localhost:5000
- [ ] All features working
- [ ] Sound effects active
- [ ] Theme switching works
- [ ] History saving

---

<div align="center">

### 🔐 LOGICLAB

**Installation Complete!** Start calculating with style.

[Documentation](README.md) • [Changelog](CHANGELOG.md) • [PRD](PRD.md)

</div>
