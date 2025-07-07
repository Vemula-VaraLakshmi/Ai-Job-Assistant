# 🧠 AI Job Application Assistant

A smart and user-friendly web app that generates **personalized cover letters** by analyzing a user's resume (PDF) and a job description — powered by LLMs via [OpenRouter](https://openrouter.ai/).

This project was created to simplify the job application process using AI, combining Flask backend, OpenRouter LLMs (like GPT-4/Mixtral), PDF parsing, and a clean modern UI with Bootstrap or Tailwind CSS.

---

## 🚀 Features

- 📄 Upload your **PDF resume**
- 🧾 Paste any job description
- ⚡ Instantly generates a **tailored, professional cover letter**
- 🧠 Uses powerful **LLMs** like GPT-4, Mixtral (via OpenRouter)
- 🎨 Clean, responsive frontend UI (Bootstrap/Tailwind)
- 🔐 Secrets and API keys securely managed using `.env`

---

## 🏗️ Project Structure

```
ai-job-assistant/
│
├── backend/                  # Flask backend
│   ├── app.py                # Core backend script
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Contains API key (not pushed to GitHub)
│
├── frontend/                 # Static frontend (HTML/CSS/JS)
│   └── index.html
│
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

| Layer       | Technology                |
|-------------|---------------------------|
| Frontend    | HTML, CSS, Bootstrap or Tailwind |
| Backend     | Python, Flask             |
| AI Engine   | OpenRouter (LLM Proxy)    |
| PDF Parsing | PyMuPDF (`fitz`)          |
| Secrets     | `python-dotenv` & `.env`  |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-job-assistant.git
cd ai-job-assistant/backend
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you're using Python 3.7+

### 3️⃣ Add Your API Key in a `.env` File

In the `backend/` folder, create a file named `.env` and add your OpenRouter API key:

```
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

🔗 Get a free key from [https://openrouter.ai/keys](https://openrouter.ai/keys)

### 4️⃣ Run the Flask Server

```bash
python app.py
```

It will run locally at:  
📡 `http://127.0.0.1:5000`

---

## 🖥️ Using the App

1. Open `frontend/index.html` in your browser
2. Paste a **job description**
3. Upload your **resume in PDF format**
4. Click **"Generate Cover Letter"**
5. Watch the AI craft a tailored, professional cover letter just for you ✨

---

## 💡 Supported LLMs via OpenRouter

You can easily switch between supported models:

- `mistralai/mixtral-8x7b-instruct` (free & fast)
- `openai/gpt-3.5-turbo`
- `openai/gpt-4` *(may require credits)*
- `meta-llama/llama-3-8b-instruct`
- `anthropic/claude-3-haiku`

🔍 View all models here: [https://openrouter.ai/models](https://openrouter.ai/models)

---

## 🌍 Deployment Guide

### Backend (Flask)
- Use [Render](https://render.com/) or [Railway](https://railway.app/)
- Set `OPENROUTER_API_KEY` in environment variables
- Start command: `python app.py`

### Frontend
- Use **GitHub Pages** for static `index.html`
- Or deploy with **Vercel** / **Netlify**

---

## 📸 Screenshots

_Add screenshots here if available_  
Drag and drop image files directly into this section on GitHub to show the UI.

---

## 🙋‍♀️ Author

👩‍💻 Developed by **Vemula Vara Lakshmi** (Varsha)  
💡 Passionate about using AI to solve real-world problems.

---

## 📜 License

This project is open-source under the **MIT License** — feel free to use, improve, and share it!

---

## ⭐ Support

If you find this project helpful:
- 🌟 Star this repo
- 🍴 Fork and build on top of it
- 🧵 Share your feedback and improvements

Happy coding!
