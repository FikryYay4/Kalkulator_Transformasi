// ===== CYBER SOUND EFFECTS =====
// Using Web Audio API for keyboard and UI sounds

class CyberSound {
    constructor() {
        this.audioContext = null;
        this.enabled = localStorage.getItem('soundEnabled') !== 'false';
        this.init();
    }

    init() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        } catch (e) {
            console.warn('Web Audio API not supported');
        }
    }

    playTone(frequency, duration, type = 'sine') {
        if (!this.enabled || !this.audioContext) return;

        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        oscillator.frequency.value = frequency;
        oscillator.type = type;

        gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + duration);

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + duration);
    }

    // Keyboard click sound
    keyPress() {
        this.playTone(800, 0.05, 'square');
    }

    // Button hover sound
    hover() {
        this.playTone(600, 0.03, 'sine');
    }

    // Button click sound
    click() {
        this.playTone(1000, 0.08, 'square');
    }

    // Success sound
    success() {
        this.playTone(880, 0.1, 'sine');
        setTimeout(() => this.playTone(1100, 0.15, 'sine'), 100);
    }

    // Error sound
    error() {
        this.playTone(200, 0.2, 'sawtooth');
    }

    // Scan sound
    scan() {
        if (!this.enabled || !this.audioContext) return;

        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(400, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(1200, this.audioContext.currentTime + 0.5);

        gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.5);

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + 0.5);
    }

    // Processing sound
    processing() {
        for (let i = 0; i < 3; i++) {
            setTimeout(() => this.playTone(600 + (i * 100), 0.05, 'square'), i * 100);
        }
    }

    toggle() {
        this.enabled = !this.enabled;
        localStorage.setItem('soundEnabled', this.enabled);
        if (this.enabled) {
            this.success();
        }
        return this.enabled;
    }
}

// Global sound instance
const cyberSound = new CyberSound();

// Add sound effects to inputs and buttons
document.addEventListener('DOMContentLoaded', function() {
    // Keyboard sounds for inputs
    document.querySelectorAll('input, textarea').forEach(input => {
        input.addEventListener('keydown', () => cyberSound.keyPress());
    });

    // Hover sounds for buttons
    document.querySelectorAll('button, .btn, .op-btn, .feature-card').forEach(btn => {
        btn.addEventListener('mouseenter', () => cyberSound.hover());
    });

    // Click sounds for buttons
    document.querySelectorAll('button, .btn, .op-btn').forEach(btn => {
        btn.addEventListener('click', () => cyberSound.click());
    });

    // Add sound toggle button to navbar
    const soundToggle = document.createElement('button');
    soundToggle.className = 'theme-toggle ms-2';
    soundToggle.innerHTML = '<i class="bi bi-volume-up-fill"></i>';
    soundToggle.title = 'Toggle Sound Effects';
    soundToggle.addEventListener('click', function() {
        const enabled = cyberSound.toggle();
        this.innerHTML = enabled ? 
            '<i class="bi bi-volume-up-fill"></i>' : 
            '<i class="bi bi-volume-mute-fill"></i>';
    });

    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle && themeToggle.parentElement) {
        themeToggle.parentElement.appendChild(soundToggle);
    }

    // Update initial state
    if (!cyberSound.enabled) {
        soundToggle.innerHTML = '<i class="bi bi-volume-mute-fill"></i>';
    }
});

// Export for use in other scripts
window.cyberSound = cyberSound;
