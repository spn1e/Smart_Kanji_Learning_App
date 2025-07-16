# Smart Kanji OCR & Quiz App

<p align="center">
  <a href="https://smartkanjilearningapp-pzkdamtczvopp7ul5relxt.streamlit.app/" target="_blank"><img src="https://img.shields.io/badge/Live%20Demo-Streamlit-success?logo=streamlit" alt="Live demo badge"></a>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
</p>

A lightweight **Streamlit** web application that helps you learn Japanese kanji in three quick steps:

1. **Upload** an image containing Japanese text.
2. **See** the extracted kanji plus ON/KUN readings (powered by SudachiPy).
3. **Answer** a multiple‑choice question to test your memory of one random reading.

That’s it—no heavy databases, no sign‑ups, just fast OCR and an instant mini‑quiz inside your browser.

---

## ✨ Current Features

| Category | Details |
|----------|---------|
| **Image OCR** | Japanese Tesseract model (`tesseract‑ocr‑jpn`) extracts kanji from any PNG/JPG |
| **Reading Lookup** | SudachiPy tokeniser returns the standard reading for every token |
| **Quick Quiz** | One multiple‑choice question per session, with instant feedback |
| **Clean UI** | Pure Streamlit components, mobile‑friendly layout |

> **Live Demo:** <https://smartkanjilearningapp-pzkdamtczvopp7ul5relxt.streamlit.app/>

---

## 🚀 Quick Start (local)

```bash
# 1. Clone
git clone https://github.com/your-username/smart-kanji-app.git
cd smart-kanji-app

# 2. Create venv & install
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Make sure Tesseract with Japanese data is available
#    Ubuntu / Debian example:
sudo apt-get install tesseract-ocr tesseract-ocr-jpn

# 4. Run
streamlit run app.py
```

Open <http://localhost:8501> and start practising kanji!

---

## 🏗️ Project Layout

```
smart-kanji-app/
├── app.py             # Streamlit UI
├── kanji_helpers.py   # OCR, reading helper & quiz generator
├── requirements.txt   # Python deps
├── apt.txt            # Extra system packages for Streamlit Cloud
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Streamlit** – turn Python scripts into shareable web apps
- **Tesseract OCR** + Japanese language pack
- **OpenCV & Pillow** – image handling
- **SudachiPy** – tokenisation & reading extraction

---

## 🌐 1‑Click Deployment (Streamlit Community Cloud)

1. Fork or push the repo to GitHub.
2. Go to <https://share.streamlit.io/>.
3. Create a new app, point **“Main file”** to `app.py`, and leave the rest to Streamlit.
4. Add `apt.txt` so the build installs `tesseract-ocr` and `tesseract-ocr-jpn`.

---

## 🤝 Contributing

Bug reports and pull requests are welcome!  
If you add new quiz modes, progress tracking, or audio, please update this README accordingly.

---

## 📄 License

This project is licensed under the **MIT License** – see `LICENSE` for details.

---

## 🙏 Acknowledgements

- Google’s **Tesseract OCR** project
- **SudachiPy** team for the tokenizer
- The **Streamlit** community

*Happy kanji learning! よろしくお願いします 🌸*
