# Re**X**plore 
### *A Web-Based Regular Expression Explorer*

> An interactive, student-friendly regex testing tool powered by **Python + Flask** — inspired by regex101.com, built for learners.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-Educational-purple?style=for-the-badge)

---

## 📸 Preview

```
ReXplore — Dark nebula theme with neuron animation background
Pattern input → Operation dropdown → Live result page
```

---

## Features

| Feature | Description |
|---|---|
|  **7 Python Operations** | `re.match`, `re.search`, `re.findall`, `re.finditer`, `re.sub`, `re.split`, `re.compile` |
|  **Match Highlighting** | Visual preview with matched text highlighted inline |
|  **Capture Groups** | Displays all capture groups per match |
|  **RegEx Notes Sidebar** | 12 collapsible reference sections to learn while you test |
|  **Quick Reference** | Click-to-insert common patterns |
|  **Neuron Background** | Animated canvas with floating node network |
|  **Python Backend** | Real `re` module — not JavaScript simulation |
|  **Responsive Layout** | Works on all screen sizes |

---

## 🗂️ Project Structure

```
ReXplore/
│
├── main.py                  ← Flask backend (routes + regex logic)
│
├── static/
│   ├── Rexplore.css         ← Styles for main page
│   └── result.css           ← Styles for result page
│
└── templates/
    ├── ReXplore.html        ← Main form page
    └── result.html          ← Results display page
```

---

## ⚙️ How It Works

```
User fills form (ReXplore.html)
        │
        ▼
POST /execute  ──►  main.py reads pattern + test_str + operation
        │
        ▼
Python re module runs the operation
        │
        ▼
Results passed to result.html via render_template()
        │
        ▼
Styled result page displayed to user
```

> Same concept as a basic Flask form app —  
> `ReXplore.html` = your Form.html  
> `result.html` = your result.html  
> `/execute` route = your `/Submit` route

---

##  Getting Started

### Prerequisites

```bash
Python 3.8+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/rexplore.git

# 2. Navigate into the project
cd rexplore

# 3. Install dependencies
pip install flask

# 4. Run the app
python main.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔧 Supported Operations

```python
re.findall(pattern, string)    # Returns list of all matches
re.search(pattern, string)     # Returns first match anywhere
re.match(pattern, string)      # Match only at beginning of string
re.finditer(pattern, string)   # Iterator of all match objects
re.sub(pattern, repl, string)  # Find and replace matches
re.split(pattern, string)      # Split string by pattern
re.compile(pattern)            # Compile pattern into regex object
```

---

## 📖 RegEx Quick Reference

| Pattern | Meaning |
|---|---|
| `\d` | Any digit (0–9) |
| `\w` | Word character (a-z, A-Z, 0-9, _) |
| `\s` | Whitespace |
| `.` | Any character except newline |
| `^` | Start of string |
| `$` | End of string |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n,m}` | Between n and m times |
| `(group)` | Capture group |
| `a\|b` | Alternation (a or b) |
| `[abc]` | Character class |
| `(?=...)` | Lookahead |

---

## Tech Stack

- **Backend** — Python 3, Flask, `re` module
- **Frontend** — HTML5, CSS3, Vanilla JavaScript
- **Fonts** — JetBrains Mono, Syne (Google Fonts)
- **Animation** — HTML5 Canvas (neuron network)
- **Templating** — Jinja2

---

## 📁 Key Files Explained

### `main.py`
Contains two Flask routes:
- `GET /` — Renders the main `ReXplore.html` form
- `POST /execute` — Reads form data, runs Python regex, renders `result.html`

### `ReXplore.html`
Main page with:
- Test string textarea
- Regex pattern input with `/` delimiters
- Operation dropdown (7 options)
- Replacement field (shown only for `re.sub`)
- Quick Reference grid
- RegEx Notes sidebar

### `result.html`
Result page with:
- Match preview with highlighted matches
- Individual match cards (index, value, groups)
- Operation-specific output (sub → replaced text, split → chips)
- Back to ReXplore button

---

##  Design

| Element | Value |
|---|---|
| Background | `#0a0a0f` — Deep space black |
| Primary Accent | `#7c5cfc` — Electric purple |
| Secondary Accent | `#fc5ca0` — Neon pink |
| Highlight | `#5cfcb8` — Cyber teal |
| Font | JetBrains Mono + Syne |
| Theme | Dark nebula + neuron network |

---

## 🛠️ Future Improvements

- [ ] Add regex flags support (`re.IGNORECASE`, `re.MULTILINE`)
- [ ] Add match count live counter
- [ ] Add regex explanation panel
- [ ] Export results as JSON / CSV
- [ ] Add saved patterns history
- [ ] Deploy to cloud (Render / Railway)

---

## ⚠️ Disclaimer

> This project is built **for educational purposes only** as part of a data science internship project at **Innomatics Research Labs**.
>
> - Font *JetBrains Mono* © JetBrains (SIL Open Font License)
> - Font *Syne* © Bonjour Monde (SIL Open Font License)
> - All third-party assets remain property of their respective owners
> - Background visuals and design patterns are used for learning demonstrations only

---

##  Author

**V. Chidvilas Naidu**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/chidvilas-kumkapalla-60703a1b3)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chidvilasnaidu)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](chidvilasnaidu99@gmail.com)

---

## 📄 License

This project is intended for **educational use only**.  
© 2026 ReXplore — All rights reserved.

---

<div align="center">

Made with ❤️ during Internship @ **Innomatics Research Labs**

*"Learning RegEx, one pattern at a time."*

