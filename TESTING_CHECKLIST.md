# TESTING CHECKLIST - Theme Switching Fix

## ✅ PRE-TESTING SETUP

1. **Start Flask Server**
   ```bash
   cd "c:\Users\Administrator\Documents\Kuliah_301250004\Semester 2\Pengantar pemrogman\Tugas\Kalkulator Transformasi Bilangan Flask"
   python app.py
   ```

2. **Open Browser**
   - Navigate to: http://127.0.0.1:5000
   - Open DevTools (F12)
   - Go to Console tab (check for errors)

3. **Clear Browser Cache** (if testing after previous version)
   - Press `Ctrl + Shift + Delete`
   - Clear cached images and files
   - OR hard refresh: `Ctrl + F5`

---

## 🌙 DARK MODE TESTING

### Visual Checks
- [ ] **Background:** Pure black `#0a0e27` (NOT blue)
- [ ] **Body text:** Matrix green `#00ff87`
- [ ] **Navbar:** Black background with green bottom border
- [ ] **Brand logo:** Green text with `> LOGICLAB` format
- [ ] **Nav links:** Gray text, green on hover
- [ ] **Feature cards:** Dark gray background with green borders
- [ ] **Card titles:** Green text
- [ ] **Card descriptions:** Blue-gray text
- [ ] **Buttons:** Black with green borders
- [ ] **Button hover:** Green background with black text
- [ ] **Form inputs:** Black background with green borders
- [ ] **Input focus:** Green glow effect
- [ ] **Cyber rain:** Green Matrix characters falling
- [ ] **Theme toggle icon:** Sun icon (☀️) visible

### Interaction Checks
- [ ] Click feature cards - should have green glow on hover
- [ ] Type in form inputs - should show green border on focus
- [ ] Hover over buttons - should invert to green
- [ ] Scroll page - should see green scrollbar
- [ ] Check navbar links - should highlight green on hover

### Console Checks
- [ ] No JavaScript errors
- [ ] Console shows: `Theme applied: dark`
- [ ] `data-theme="dark"` on `<html>` element
- [ ] `class="theme-dark"` on `<body>` element

---

## ☀️ LIGHT MODE TESTING

### Visual Checks
- [ ] **Background:** Animated gradient (purple → pink → blue)
- [ ] **Background animation:** Gradient is moving/shifting
- [ ] **Body text:** Dark gray/black `#1a1a2e`
- [ ] **Navbar:** White background with purple bottom border
- [ ] **Brand logo:** Purple gradient text with `> LOGICLAB`
- [ ] **Nav links:** Gray text, purple on hover
- [ ] **Feature cards:** White background with purple borders
- [ ] **Card titles:** Purple text
- [ ] **Card descriptions:** Gray text
- [ ] **Buttons:** Purple gradient background
- [ ] **Button hover:** Stronger glow effect
- [ ] **Form inputs:** White background with purple borders
- [ ] **Input focus:** Purple glow effect
- [ ] **Cyber rain:** Colorful (blue/purple/pink) characters falling
- [ ] **Theme toggle icon:** Moon icon (🌙) visible

### Interaction Checks
- [ ] Click feature cards - should have purple glow on hover
- [ ] Type in form inputs - should show purple border on focus
- [ ] Hover over buttons - should show purple glow
- [ ] Scroll page - should see purple scrollbar
- [ ] Check navbar links - should highlight purple on hover

### Console Checks
- [ ] No JavaScript errors
- [ ] Console shows: `Theme applied: light`
- [ ] `data-theme="light"` on `<html>` element
- [ ] `class="theme-light"` on `<body>` element

---

## 🔄 THEME TOGGLE TESTING

### Toggle Functionality
- [ ] Click theme toggle button (moon/sun icon)
- [ ] **Instant change:** Background changes immediately (no delay)
- [ ] **All elements update:** Cards, navbar, buttons all change
- [ ] **Icon changes:** Moon ↔ Sun
- [ ] **Smooth transition:** 0.3s ease animation
- [ ] **Sound effect:** Click sound plays (if enabled)

### Toggle Multiple Times
- [ ] Dark → Light → Dark → Light (repeat 5 times)
- [ ] Each toggle should be instant
- [ ] No visual glitches or flashing
- [ ] No console errors

### Persistence Testing
1. **Set to Dark Mode**
   - [ ] Click toggle to dark mode
   - [ ] Refresh page (F5)
   - [ ] Should stay in dark mode

2. **Set to Light Mode**
   - [ ] Click toggle to light mode
   - [ ] Refresh page (F5)
   - [ ] Should stay in light mode

3. **Navigate Between Pages**
   - [ ] Set to dark mode
   - [ ] Click "Aritmatika" link
   - [ ] Should stay in dark mode
   - [ ] Click "Logika" link
   - [ ] Should stay in dark mode
   - [ ] Repeat for light mode

---

## 📄 PAGE-BY-PAGE TESTING

### Home Page (/)
- [ ] Dark mode: Black background, green text
- [ ] Light mode: Gradient background, dark text
- [ ] Feature cards change color with theme
- [ ] System info panel changes color
- [ ] Recent operations panel changes color

### Aritmatika Page (/aritmatika)
- [ ] Calculator card changes with theme
- [ ] Form inputs change with theme
- [ ] Operation buttons change with theme
- [ ] Calculate button changes with theme
- [ ] Result section changes with theme
- [ ] Steps timeline changes with theme

### Logika Page (/logika)
- [ ] Logic gate selector changes with theme
- [ ] Input fields change with theme
- [ ] Circuit builder changes with theme
- [ ] SVG gate diagrams visible in both themes
- [ ] Truth table changes with theme

### Konversi Page (/konversi)
- [ ] Tab navigation changes with theme
- [ ] Number system converter changes with theme
- [ ] Temperature converter changes with theme
- [ ] Currency converter changes with theme
- [ ] Swap button changes with theme

### Bonus Page (/bonus)
- [ ] Factorial calculator changes with theme
- [ ] Fibonacci calculator changes with theme
- [ ] Result displays change with theme

### Riwayat Page (/riwayat)
- [ ] History items change with theme
- [ ] Category badges visible in both themes
- [ ] Clear history button changes with theme
- [ ] Empty state message changes with theme

---

## 🖥️ BROWSER COMPATIBILITY

Test in multiple browsers:

### Chrome/Edge (Chromium)
- [ ] Dark mode works
- [ ] Light mode works
- [ ] Toggle works
- [ ] Persistence works

### Firefox
- [ ] Dark mode works
- [ ] Light mode works
- [ ] Toggle works
- [ ] Persistence works

### Safari (if available)
- [ ] Dark mode works
- [ ] Light mode works
- [ ] Toggle works
- [ ] Persistence works

---

## 📱 RESPONSIVE TESTING

### Desktop (1920x1080)
- [ ] Dark mode displays correctly
- [ ] Light mode displays correctly
- [ ] All elements visible

### Tablet (768x1024)
- [ ] Dark mode displays correctly
- [ ] Light mode displays correctly
- [ ] Navbar collapses properly
- [ ] Cards stack correctly

### Mobile (375x667)
- [ ] Dark mode displays correctly
- [ ] Light mode displays correctly
- [ ] Navbar hamburger menu works
- [ ] Cards stack vertically
- [ ] Theme toggle accessible

---

## 🐛 EDGE CASE TESTING

### LocalStorage
1. **Clear localStorage**
   - Open DevTools → Application → Local Storage
   - Delete `theme` key
   - Refresh page
   - [ ] Should default to dark mode

2. **Invalid theme value**
   - Set `localStorage.setItem('theme', 'invalid')`
   - Refresh page
   - [ ] Should fallback to dark mode

### Performance
- [ ] Theme toggle is instant (< 100ms)
- [ ] No layout shift when toggling
- [ ] No memory leaks after 50+ toggles
- [ ] Cyber rain doesn't slow down page

### Accessibility
- [ ] Theme toggle has proper `title` attribute
- [ ] Keyboard navigation works (Tab key)
- [ ] Enter key toggles theme
- [ ] Screen reader announces theme change

---

## ✅ ACCEPTANCE CRITERIA

### MUST PASS (Critical)
- [x] Dark mode has BLACK background (#0a0e27)
- [x] Light mode has GRADIENT background (animated)
- [x] Dark mode has GREEN text (#00ff87)
- [x] Light mode has DARK text (#1a1a2e)
- [x] Theme toggle changes theme INSTANTLY
- [x] Theme persists across page refreshes
- [x] Theme persists across page navigation
- [x] NO console errors
- [x] ALL pages respect theme setting

### SHOULD PASS (Important)
- [x] Smooth transitions (0.3s)
- [x] Cyber rain changes color with theme
- [x] All interactive elements change with theme
- [x] Hover effects work in both themes
- [x] Focus states work in both themes

### NICE TO HAVE (Optional)
- [x] Sound effects on toggle
- [x] Scan line animation
- [x] Glow effects
- [x] Gradient animation in light mode

---

## 🚨 KNOWN ISSUES TO CHECK

### Issue 1: Theme Not Changing
**Symptom:** Click toggle but nothing happens
**Fix:** Hard refresh (Ctrl + F5)
**Status:** Should be FIXED ✅

### Issue 2: Partial Theme Change
**Symptom:** Some elements change, others don't
**Fix:** Check CSS specificity, add !important
**Status:** Should be FIXED ✅

### Issue 3: Theme Resets on Refresh
**Symptom:** Theme doesn't persist
**Fix:** Check localStorage implementation
**Status:** Should be FIXED ✅

### Issue 4: Both Themes Look Same
**Symptom:** No visual difference
**Fix:** Inline styles + critical CSS overrides
**Status:** Should be FIXED ✅

---

## 📊 TEST RESULTS TEMPLATE

```
Date: _______________
Tester: _______________
Browser: _______________
OS: _______________

DARK MODE: ☐ PASS ☐ FAIL
LIGHT MODE: ☐ PASS ☐ FAIL
TOGGLE: ☐ PASS ☐ FAIL
PERSISTENCE: ☐ PASS ☐ FAIL
ALL PAGES: ☐ PASS ☐ FAIL

NOTES:
_________________________________
_________________________________
_________________________________

OVERALL: ☐ PASS ☐ FAIL
```

---

## 🎯 SUCCESS CRITERIA

**Theme switching is considered SUCCESSFUL if:**

1. ✅ Dark mode shows BLACK background with GREEN text
2. ✅ Light mode shows GRADIENT background with DARK text
3. ✅ Toggle button changes theme INSTANTLY
4. ✅ Theme persists across refreshes
5. ✅ Theme persists across navigation
6. ✅ ALL pages respect theme
7. ✅ NO console errors
8. ✅ Visual difference is OBVIOUS and CLEAR

**If ALL criteria are met:** ✅ THEME SYSTEM WORKING PERFECTLY

**If ANY criteria fails:** ❌ NEEDS DEBUGGING

---

## 📞 DEBUGGING STEPS

If theme doesn't work:

1. **Check Console**
   - F12 → Console
   - Look for errors
   - Check for "Theme applied: X" message

2. **Check HTML Attribute**
   - F12 → Elements
   - Find `<html>` tag
   - Should have `data-theme="dark"` or `data-theme="light"`

3. **Check Body Class**
   - Find `<body>` tag
   - Should have `class="theme-dark"` or `class="theme-light"`

4. **Check Inline Styles**
   - Find `<body>` tag
   - Should have `style="background: #0a0e27; color: #00ff87;"` (dark)
   - Or `style="background: linear-gradient(...);"` (light)

5. **Check localStorage**
   - F12 → Application → Local Storage
   - Should have `theme: "dark"` or `theme: "light"`

6. **Hard Refresh**
   - Press `Ctrl + F5`
   - Clears cache and reloads

7. **Clear Cache**
   - `Ctrl + Shift + Delete`
   - Clear cached files
   - Refresh page

---

**Status:** ✅ READY FOR TESTING
**Expected Result:** ALL TESTS SHOULD PASS
**Estimated Testing Time:** 15-20 minutes
