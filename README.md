# 🔥 Roast Me (AI-Powered Humor App)

A fun and interactive web app that generates witty, humorous roasts based on user input using **Google Gemini AI** and **Streamlit**.

---

## 🚀 Live Demo

👉 *(https://roastmeee.streamlit.app)*

---

## 🧠 Features

* 🎭 Generate funny, non-offensive roasts using AI
* 🎚️ Adjustable roast levels:

  * Mild 😌
  * Savage 😈
  * Unhinged 💀
* ⚡ Fast responses powered by Gemini
* 🎨 Clean and modern UI with animations
* 🔐 Secure API key handling using environment variables and secrets

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit
* **AI Model:** Google Gemini API
* **Backend Logic:** Python
* **Deployment:** Streamlit Community Cloud

---

## 📦 Installation (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/roastme.git
cd roastme
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open: `http://localhost:8501`

---

## ☁️ Deployment

This app is deployed using **Streamlit Community Cloud**.

### Steps:

1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Add secret in dashboard:

```toml
GEMINI_API_KEY = "your_api_key"
```

4. Deploy 🚀

---

## 🔐 Environment Variables

| Variable       | Description         |
| -------------- | ------------------- |
| GEMINI_API_KEY | Your Gemini API key |

---


## 💡 Future Improvements

* 📜 Roast history tracking
* 📋 Copy/share roast button
* 🎤 Voice input
* 🌐 Multi-language support
* 🎭 Custom roast personalities

---

## ⚠️ Disclaimer

This app is intended for **entertainment purposes only**.
All roasts are generated to be humorous and non-offensive.

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
