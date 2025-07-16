# Smart Kanji Learning App

<p align="center">
  <a href="https://smartkanjilearningapp-pzkdamtczvopp7ul5relxt.streamlit.app/" target="_blank"><img src="https://img.shields.io/badge/Live%20Demo-Streamlit-success?logo=streamlit" alt="Live demo badge"></a>
  <img src="https://img.shields.io/github/license/your-username/smart-kanji-learning-app" alt="License">
</p>

An interactive **Streamlit** web application that helps learners master Japanese kanji through adaptive quizzes, instant look‑ups, and rich visual explanations. Built for both beginners and advanced students, the app leverages open kanji datasets and a lightweight quiz engine to deliver a fun, bite‑sized study experience right in your browser.

---

## ✨ Key Features

| Category | Highlights |
|----------|------------|
| **Adaptive Quiz** | • Multiple‑choice or typing mode<br>• Dynamic difficulty based on your recent accuracy<br>• Instant feedback with mnemonic hints |
| **Kanji Lookup** | • Search by kanji, reading, or English meaning<br>• Displays radicals, stroke count, JLPT level, and frequency rank<br>• SVG stroke‑order animation when available |
| **Progress Tracking** | • Session‑based stats (accuracy %, streaks, items mastered)<br>• CSV export to keep personal records |
| **Audio Support** | • Auto‑generated ON/KUN readings via gTTS so you can hear correct pronunciation |
| **Responsive UI** | • Clean Streamlit components, emoji reactions, dark‑mode ready |

> **Live Demo:** <https://smartkanjilearningapp-pzkdamtczvopp7ul5relxt.streamlit.app/>

---

## 🚀 Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/your-username/smart-kanji-learning-app.git
cd smart-kanji-learning-app
```

2. **Create a virtual environment & install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run locally**

```bash
streamlit run app.py
```

4. Open <http://localhost:8501> in your browser and start drilling kanji!

---

## 🏗️ Project Structure

```
smart-kanji-learning-app/
├── app.py                # Streamlit UI entrypoint
├── kanji_helpers.py      # Quiz generation & kanji utilities
├── data/
│   └── kanjidic2.json    # Parsed KanjiDIC2 dataset (≈13k characters)
├── resources/
│   ├── radicals.csv
│   └── stroke_svgs/
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.10**
- **[Streamlit](https://streamlit.io/)** – instant web apps for data & ML
- **KanjiDIC2** – open kanji metadata
- **pandas**, **regex**, **random** – core quiz logic
- **gTTS / playsound** – optional text‑to‑speech (macOS/Linux only)

---

## 🌐 Deployment

The live demo is hosted on **Streamlit Community Cloud**. To deploy your fork:

1. Push the repo to GitHub.
2. Sign in to <https://share.streamlit.io/> and link your repo.
3. Set the main file to `app.py` and add required secrets (if any).
4. Click **Deploy** – Streamlit handles the rest!

---

## 🤝 Contributing

PRs are welcome! Feel free to open an issue for feature requests or bug reports. Please follow the conventional commit style and write concise, descriptive messages.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- The [KanjiDIC2](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project) project for the comprehensive kanji dataset.
- [Streamlit](https://streamlit.io/) for making web app deployment a breeze.
- All contributors and testers who provided feedback during development.

---

Happy kanji learning! よろしくお願いします 🙇‍♂️
