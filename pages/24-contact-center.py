
import streamlit as st

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="CustomGPT – Chat with Your Documents", layout="wide")

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
st.title("🛠️ CustomGPT – Chat with Your Documents")
st.markdown("""
<div class="tag-block">
<strong>Use Case Category:</strong> Document Intelligence  
<br><strong>App Type:</strong> H2O Wave App  
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Problem Statement
# -----------------------------
st.markdown('<div class="section-title">🧠 Problem Statement</div>', unsafe_allow_html=True)
st.markdown("""
Organizations often face challenges in efficiently extracting insights from lengthy, complex documents like contracts, briefs, and policies.  
Manual reviews are slow and prone to oversight, while keyword searches lack context and accuracy—making information retrieval tedious and unreliable.
""")

# -----------------------------
# Solution
# -----------------------------
st.markdown('<div class="section-title">🚀 Solution</div>', unsafe_allow_html=True)
st.markdown("""
**CustomGPT** allows users to engage with documents conversationally.  
Ask questions, summarize content, and streamline collaboration across teams — improving productivity and reducing information overload.
""")

# -----------------------------
# Key Features
# -----------------------------
st.markdown('<div class="section-title">💡 Key Features</div>', unsafe_allow_html=True)
st.markdown("""
- 🔍 **Chat with PDF**: Ask contextual questions directly from the document.  
- 📝 **Summarization**: Generate quick summaries of lengthy documents.  
- 🤝 **Team Collaboration**: Built for cross-functional use (legal, HR, marketing, compliance).  
- 📬 **Email Delivery**: Receive summary digests via email.  
- ⚙️ **Built on H2O Wave**: Real-time, Python-powered UI.
""")

# -----------------------------
# Industry Applications
# -----------------------------
st.markdown('<div class="section-title">🏢 Industry Applications</div>', unsafe_allow_html=True)
industry_data = {{
    "Industry": ["Legal", "Marketing", "HR", "Compliance"],
    "Use Case": [
        "Review and summarize contract clauses",
        "Collaborate on campaign briefs and reports",
        "Answer onboarding queries from policy documents",
        "Extract regulatory terms from governance manuals"
    ]
}}
st.table(industry_data)

# -----------------------------
# Technical Stack
# -----------------------------
st.markdown('<div class="section-title">🧰 Technical Stack</div>', unsafe_allow_html=True)
st.markdown("""
| Component       | Technology                   |
|----------------|------------------------------|
| UI Framework   | [H2O Wave](https://wave.h2o.ai/) |
| Backend        | Python                       |
| LLM Engine     | [H2OGPTe](https://h2o.ai/platform/enterprise-h2ogpte/) (RAG-based)           |
| PDF Handling   | PyMuPDF / pdfplumber         |
| Notifications  | SMTP (email summaries)       |
""", unsafe_allow_html=True)

# -----------------------------
# GitHub Link
# -----------------------------
st.markdown('---')
st.markdown("🔗 [View GitHub Repository](https://github.com/h2oai/cust-cba-agentic-contact-centre)", unsafe_allow_html=True)
