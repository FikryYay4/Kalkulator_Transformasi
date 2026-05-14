// ===== THEME TOGGLE =====
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('themeToggle');
    const icon = document.getElementById('themeIcon');
    const html = document.documentElement;

    // Load saved theme or default to dark
    const saved = localStorage.getItem('theme') || 'dark';
    applyTheme(saved);

    if (toggle) {
        toggle.addEventListener('click', function() {
            const current = html.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            localStorage.setItem('theme', next);
            
            // Play sound effect if available
            if (window.cyberSound) {
                window.cyberSound.click();
            }
        });
    }

    function applyTheme(theme) {
        // Set attribute
        html.setAttribute('data-theme', theme);
        html.className = 'theme-' + theme;
        
        // Update icon
        if (icon) {
            icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        }
        
        // Force immediate visual update by adding/removing class
        document.body.classList.remove('theme-light', 'theme-dark');
        document.body.classList.add('theme-' + theme);
        
        console.log('Theme toggle:', theme);
        
        // Apply inline styles with !important using cssText
        if (theme === 'dark') {
            document.body.style.cssText = 'background: #0a0e27 !important; background-color: #0a0e27 !important; color: #00ff87 !important;';
        } else {
            document.body.style.cssText = 'background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe) !important; background-size: 400% 400% !important; animation: gradientShift 15s ease infinite !important; color: #1a1a2e !important;';
        }
        
        // Force update navbar
        const navbar = document.querySelector('.navbar-custom');
        if (navbar) {
            if (theme === 'dark') {
                navbar.style.cssText = 'background: rgba(10, 14, 39, 0.98) !important; background-color: rgba(10, 14, 39, 0.98) !important; border-bottom: 2px solid #00ff87 !important; box-shadow: 0 0 20px rgba(0,255,135,0.3) !important;';
            } else {
                navbar.style.cssText = 'background: rgba(255, 255, 255, 0.98) !important; background-color: rgba(255, 255, 255, 0.98) !important; border-bottom: 3px solid rgba(102, 102, 241, 0.5) !important; box-shadow: 0 4px 30px rgba(102,102,241,0.4) !important;';
            }
        }
        
        // Force update all cards
        const cards = document.querySelectorAll('.feature-card, .calc-card');
        cards.forEach(card => {
            if (theme === 'dark') {
                card.style.cssText = 'background: rgba(15, 20, 25, 0.95) !important; background-color: rgba(15, 20, 25, 0.95) !important; border: 2px solid rgba(0, 255, 135, 0.3) !important; border-color: rgba(0, 255, 135, 0.3) !important; box-shadow: 0 8px 32px rgba(0,0,0,0.8) !important;';
            } else {
                card.style.cssText = 'background: rgba(255, 255, 255, 0.95) !important; background-color: rgba(255, 255, 255, 0.95) !important; border: 2px solid rgba(102, 102, 241, 0.4) !important; border-color: rgba(102, 102, 241, 0.4) !important; box-shadow: 0 8px 32px rgba(102,102,241,0.3) !important;';
            }
        });
        
        // Force update all form controls
        const formControls = document.querySelectorAll('.form-control-custom, .form-select-custom, select, input[type="text"], input[type="number"]');
        formControls.forEach(control => {
            if (theme === 'dark') {
                control.style.cssText = 'background: rgba(0, 0, 0, 0.7) !important; background-color: rgba(0, 0, 0, 0.7) !important; border: 2px solid rgba(0, 255, 135, 0.4) !important; border-color: rgba(0, 255, 135, 0.4) !important; color: #00ff87 !important;';
            } else {
                control.style.cssText = 'background: rgba(255, 255, 255, 0.95) !important; background-color: rgba(255, 255, 255, 0.95) !important; border: 2px solid rgba(102, 102, 241, 0.4) !important; border-color: rgba(102, 102, 241, 0.4) !important; color: #1a1a2e !important;';
            }
        });
        
        console.log('Theme applied:', theme);
    }
});

// ===== HISTORY MANAGEMENT (localStorage) =====
function saveHistory(category, formula, result, steps) {
    const history = JSON.parse(localStorage.getItem('calculationHistory') || '[]');
    const now = new Date();
    const timestamp = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' });

    history.unshift({
        category: category,
        formula: formula,
        result: String(result),
        steps: steps || [],
        timestamp: timestamp,
        date: now.toLocaleDateString('id-ID')
    });

    // Keep max 100 entries
    if (history.length > 100) history.length = 100;
    localStorage.setItem('calculationHistory', JSON.stringify(history));
}

function clearCategoryHistory(category) {
    if (!confirm('Hapus riwayat ' + category + '?')) return;
    const history = JSON.parse(localStorage.getItem('calculationHistory') || '[]');
    const filtered = history.filter(h => h.category !== category);
    localStorage.setItem('calculationHistory', JSON.stringify(filtered));

    // Re-render sidebar if function exists on page
    if (typeof renderSideHistory === 'function') renderSideHistory();
    if (typeof renderSH === 'function') renderSH();
}

// ===== SMOOTH SCROLL FOR RESULTS =====
function scrollToResult() {
    const el = document.getElementById('resultSection');
    if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

// ===== INPUT VALIDATION HELPER =====
function validateNumber(value, fieldName) {
    if (value === '' || value === null || value === undefined) {
        return { valid: false, error: 'Masukkan ' + fieldName + '!' };
    }
    const num = parseFloat(value);
    if (isNaN(num)) {
        return { valid: false, error: fieldName + ' harus berupa angka!' };
    }
    return { valid: true, value: num };
}
