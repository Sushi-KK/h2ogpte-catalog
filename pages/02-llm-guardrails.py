

# Define the content for llm_guardrails.py in the same format
import streamlit as st

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="LLM Armour – h2oGPT with Guardrails", layout="wide")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            display: none !important;
        }
        .block-container {
            padding-top: 2rem;
            max-width: 1100px;
            margin: auto;
        }
        .section-title {
            font-size: 1.6rem;
            font-weight: 600;
            color: #4F8BF9;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
        }
        .back-link {
            font-size: 0.9rem;
            color: #3366cc;
            text-decoration: none;
        }
        .back-link:hover {
            text-decoration: underline;
        }
        .tag-block {
            background-color: #f1f3f6;
            padding: 0.8rem 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            font-size: 0.95rem;
        }
        th, td {
            text-align: left;
            padding: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Navigation
# -----------------------------
st.markdown('<a href="/" target="_self" class="back-link">⬅️ Back to Catalog</a>', unsafe_allow_html=True)

# -----------------------------
# Title & Meta
# -----------------------------
st.title("🛡️ LLM Armour – h2oGPT with Guardrails")
st.markdown("""
<div class="tag-block">
<strong>Use Case Category:</strong> Responsible AI  
<br><strong>App Type:</strong> H2O Wave App  
<br><strong>Tags:</strong> Guardrails, Prompt Safety, LLM Moderation, Ethical AI, Prompt Engineering
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Problem Statement
# -----------------------------
st.markdown('<div class="section-title">🧠 Problem Statement</div>', unsafe_allow_html=True)
st.markdown("""
Protecting Large Language Models (LLMs) from harmful or manipulative prompts and ensuring their outputs are ethically aligned is a growing concern.  
Without robust safeguards, LLMs may generate biased, offensive, or unethical content — posing significant risks for businesses and users alike.
""")

# -----------------------------
# Solution
# -----------------------------
st.markdown('<div class="section-title">🚀 Solution</div>', unsafe_allow_html=True)
st.markdown("""
**LLM Armour** introduces intelligent prompt validation and output moderation using customizable guardrails.  
Suspicious or unsafe prompts are flagged before processing, and output is filtered against ethical guidelines to ensure responsible content generation.
""")

# -----------------------------
# Key Features
# -----------------------------
st.markdown('<div class="section-title">💡 Key Features</div>', unsafe_allow_html=True)
st.markdown("""
- 🚫 **Prompt Screening**: Detect and block suspicious, manipulative, or harmful prompts.  
- 🛡️ **Output Validation**: Apply moderation and filtering on LLM responses using predefined guardrails.  
- 📜 **Ethical Alignment**: Adheres to responsible AI practices by preventing toxic or biased content.  
- 🎮 **Interactive Game Mode**: Test your prompt engineering skills by trying to reveal 'secret passwords' hidden in documents — while guardrails stay active.  
- 🧰 **Developer Utilities**: Includes rulesets and templates for guardrail customization.
""")

# -----------------------------
# Technical Stack
# -----------------------------
st.markdown('<div class="section-title">🧰 Technical Stack</div>', unsafe_allow_html=True)
st.markdown("""
| Component       | Technology                         |
|----------------|------------------------------------|
| UI Framework   | [H2O Wave](https://wave.h2o.ai/)   |
| Backend        | Python                             |
| LLM Engine     | H2OGPTe                            |
| Guardrails     | LLM Guardrails Package             |
| Game Logic     | Prompt Engineering Challenge Layer |
""", unsafe_allow_html=True)

# -----------------------------
# GitHub Link
# -----------------------------
st.markdown('---')
st.markdown("🔗 [View GitHub Repository](https://github.com/h2oai/llm-guardrails)", unsafe_allow_html=True)



