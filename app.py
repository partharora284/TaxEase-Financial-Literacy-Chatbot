import streamlit as st
from groq import Groq

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="TaxEase – Financial Literacy Chatbot",
    page_icon="💰",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

    .hero {
        background: linear-gradient(135deg, #1a3c5e 0%, #2e6da4 100%);
        border-radius: 14px;
        padding: 28px 32px 20px;
        margin-bottom: 24px;
        text-align: center;
        color: white;
    }
    .hero h1 { font-size: 2rem; margin: 0 0 4px; }
    .hero p  { font-size: 1rem; opacity: .85; margin: 0; }

    .stButton > button {
        background: #eaf2fb;
        border: 1.5px solid #2e6da4;
        border-radius: 20px;
        color: #1a3c5e;
        font-size: .82rem;
        padding: 5px 14px;
        cursor: pointer;
        transition: all .2s;
        white-space: normal;
        text-align: left;
    }
    .stButton > button:hover {
        background: #2e6da4;
        color: white;
    }

    .bubble-user {
        background: #2e6da4;
        color: white;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 16px;
        margin: 6px 0 6px 15%;
        word-wrap: break-word;
    }
    .bubble-bot {
        background: #f0f4f9;
        color: #1a1a2e;
        border-radius: 18px 18px 18px 4px;
        padding: 12px 16px;
        margin: 6px 15% 6px 0;
        word-wrap: break-word;
    }
    .bubble-label {
        font-size: .72rem;
        color: #888;
        margin-bottom: 2px;
    }

    .disclaimer {
        font-size: .73rem;
        color: #888;
        text-align: center;
        margin-top: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ── System prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """
You are TaxEase, a friendly and patient financial literacy assistant specialised in
Indian income-tax and filing basics for complete beginners.

YOUR PERSONA
- Warm, encouraging, jargon-free
- Always explain acronyms (e.g. "TDS – Tax Deducted at Source") the first time you use them
- Use simple analogies and real-life examples
- Never make the user feel stupid for asking basic questions

SCOPE
- Indian personal income tax: slabs, ITR forms, deductions (80C, 80D, HRA, etc.)
- How to file on the Income Tax e-filing portal
- Key deadlines and penalties
- Understanding Form 16, Form 26AS, AIS
- Difference between old and new tax regimes
- Basic concepts: TDS, advance tax, self-assessment tax, refunds

PROMPT-ENGINEERING TECHNIQUES USED (for capstone demonstration)
1. Role + persona assignment        → warm, beginner-friendly expert
2. Scope restriction                → stay on tax topics only
3. Chain-of-thought for calculations → always show step-by-step working
4. Few-shot via system examples     → structured Q&A style
5. Output formatting instructions   → use markdown headers, bullets, and a summary box

BEHAVIOUR RULES
- If asked something outside tax/finance, politely say "That's outside my area –
  I can only help with taxes and basic financial literacy!"
- For tax calculations always show step-by-step working inside a code block
- End every answer that involves an action (filing, uploading, etc.) with a
  QUICK CHECKLIST summarising what the user needs to do
- Keep answers under 350 words unless the user explicitly asks for more detail
- Remind the user at the end of every answer: "I'm an educational assistant –
  please consult a chartered accountant for personalised advice."
"""

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    st.session_state.client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ── Hero header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>💰 TaxEase</h1>
    <p>Your friendly guide to Indian Income Tax – built for complete beginners</p>
</div>
""", unsafe_allow_html=True)

# ── Suggested questions ───────────────────────────────────────────────────────
SUGGESTIONS = [
    "What is income tax and who has to pay it?",
    "What is the difference between old and new tax regime?",
    "How do I file my ITR for the first time?",
    "What is Form 16 and where do I get it?",
    "What deductions can I claim under Section 80C?",
    "What happens if I miss the tax filing deadline?",
]

if not st.session_state.messages:
    st.markdown("#### 👋 Hi! What would you like to learn today?")
    cols = st.columns(2)
    for i, q in enumerate(SUGGESTIONS):
        if cols[i % 2].button(q, key=f"sugg_{i}"):
            st.session_state.messages.append({"role": "user", "content": q})
            st.rerun()

# ── Chat history display ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="bubble-label" style="text-align:right">You</div>'
                    f'<div class="bubble-user">{msg["content"]}</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bubble-label">🤖 TaxEase</div>'
                    f'<div class="bubble-bot">{msg["content"]}</div>',
                    unsafe_allow_html=True)

# ── Chat input + response ─────────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything about taxes…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking…"):
        # Build messages with system prompt prepended
        api_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

        response = st.session_state.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=api_messages,
            max_tokens=1024,
        )
        reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# ── Clear chat button ─────────────────────────────────────────────────────────
if st.session_state.messages:
    if st.button("🗑️ Clear conversation", key="clear"):
        st.session_state.messages = []
        st.rerun()

# ── Disclaimer ────────────────────────────────────────────────────────────────
st.markdown(
    '<p class="disclaimer">⚠️ TaxEase is an educational tool only. '
    'For personalised tax advice please consult a Chartered Accountant.</p>',
    unsafe_allow_html=True,
)
