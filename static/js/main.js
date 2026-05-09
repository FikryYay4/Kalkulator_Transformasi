// ===== THEME TOGGLE =====
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('themeToggle');
    const icon = document.getElementById('themeIcon');
    const html = document.documentElement;

    // Load saved theme
    const saved = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', saved);
    updateIcon(saved);

    if (toggle) {
        toggle.addEventListener('click', function() {
            const current = html.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateIcon(next);
        });
    }

    function updateIcon(theme) {
        if (icon) {
            icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        }
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
