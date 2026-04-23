# 💰 TaxEase – Financial Literacy Chatbot

> A Streamlit-powered, AI-driven chatbot that helps complete beginners understand Indian Income Tax concepts and filing procedures.

---

## 🎯 Purpose

Many first-time taxpayers in India find income tax confusing — cryptic forms, unfamiliar acronyms, and overlapping rules. **TaxEase** breaks it all down using plain language, real-life analogies, and step-by-step guidance. It is designed for:

- Salaried individuals filing their first ITR
- Students or freshers who just started earning
- Anyone who wants to understand deductions, TDS, and the new vs old tax regime

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io) |
| AI / LLM | [Groq API](https://console.groq.com) – `llama-3.1-8b-instant` (Free tier) |
| Language | Python 3.10+ |
| Hosting | Streamlit Community Cloud (Free) |

---

## ✨ Features

- 💬 **Multi-turn conversational chat** — remembers context within a session
- 🧠 **Expert system prompt** — scoped to Indian personal income tax
- 📌 **Suggested starter questions** — onboards new users instantly
- 🔢 **Step-by-step tax calculations** — shown in formatted code blocks
- ✅ **Quick checklists** — every action-oriented answer ends with what to do next
- 🗑️ **Clear conversation** — reset and start fresh at any time
- ⚠️ **Disclaimer** — always reminds users to consult a CA for personalised advice

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/taxease-chatbot.git
cd taxease-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Groq API key
Create a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "gsk_your-key-here"
```
Get your free key at [console.groq.com](https://console.groq.com) — no credit card required.

### 4. Run the app
```bash
streamlit run app.py
```
The app opens at **http://localhost:8501**

---

## ☁️ Deploy on Streamlit Community Cloud (Free)

1. Push the code to a **public GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo, branch (`main`), and file (`app.py`)
4. In **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "gsk_your-key-here"
   ```
5. Click **Deploy** — your live URL will be ready in ~2 minutes!

---

## 🧠 Prompt Engineering Techniques Demonstrated

| Technique | Where Applied |
|---|---|
| **Role + Persona assignment** | System prompt opens with "You are TaxEase…" defining voice and expertise |
| **Scope restriction** | Explicit rules to stay on tax topics; politely refuse out-of-scope questions |
| **Chain-of-thought reasoning** | All tax calculations require step-by-step working in a code block |
| **Output formatting instructions** | Markdown headers, bullets, and ✅ Quick Checklist at end of action items |
| **Jargon expansion** | System instructs the model to always expand acronyms on first use |
| **Length constraint** | Answers capped at 350 words unless explicitly asked for more |

---

## 🗂️ Application Architecture

```
User types a question
        ↓
Streamlit captures input (st.chat_input)
        ↓
Message added to session_state (conversation memory)
        ↓
Full history + System Prompt sent to Groq API
        ↓
LLM (LLaMA 3.1) generates a response
        ↓
Reply stored in session_state + displayed as chat bubble
        ↓
st.rerun() refreshes the UI
```

---

## 📁 Project Structure

```
taxease-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies (streamlit, groq)
└── README.md           # This file
```

---

## 📦 Dependencies

```
streamlit>=1.35.0
groq>=0.9.0
```

---

## 🌐 Live Demo

🔗 [taxease-financial-literacy-chatbot.streamlit.app](https://taxease-financial-literacy-chatbot.streamlit.app)

---

## ⚠️ Disclaimer

TaxEase is an **educational tool only**. It does not constitute professional financial or legal advice. For personalised tax planning, please consult a qualified Chartered Accountant.

---

## 📜 License

MIT License — free to use, modify, and distribute.
