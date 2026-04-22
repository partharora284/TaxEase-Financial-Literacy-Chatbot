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
| AI / LLM | [Anthropic Claude API](https://docs.anthropic.com) (`claude-opus-4-5`) |
| Language | Python 3.10+ |
| Hosting | Streamlit Community Cloud |

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

### 3. Set your Anthropic API key
Create a `.env` file or export the variable:
```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxx
```
Or on Windows:
```cmd
set ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxx
```

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
   ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxx"
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
| **Jargon expansion (few-shot style)** | System instructs the model to always expand acronyms on first use |
| **Length constraint** | Answers capped at 350 words unless explicitly asked for more |

---

## 📁 Project Structure

```
taxease-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚠️ Disclaimer

TaxEase is an **educational tool only**. It does not constitute professional financial or legal advice. For personalised tax planning, please consult a qualified Chartered Accountant.

---

## 📜 License

MIT License — free to use, modify, and distribute.
