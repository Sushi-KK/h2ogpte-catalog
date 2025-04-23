import streamlit as st

st.set_page_config(page_title="CustomGPT – Chat with Your Documents", layout="wide")

# Hide sidebar and nav elements
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            display: none !important;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Back to catalog button (opens home page in the same tab)
st.markdown("""
<a href="/" target="_self" style="text-decoration:none;">
    ⬅️ Back to Catalog
</a>
""", unsafe_allow_html=True)

# Title
st.title("🛠️ CustomGPT – Chat with Your Documents")

# Tags and Meta Info
st.markdown("**Use Case Category**: Document Intelligence  \n**App Type**: H2O Wave App  \n**Tags**: LLM, Document QA, PDF, Summarization, Enterprise Search, ChatGPT")

st.markdown("---")

# Problem Statement
st.subheader("🧠 Problem Statement")
st.markdown("""
Organizations struggle to quickly understand and extract information from long, complex documents such as contracts, briefs, and policies.
Traditional keyword search or manual review is time-consuming and error-prone.
""")

# Solution
st.subheader("🚀 Solution")
st.markdown("""
**CustomGPT** enables natural language interaction with documents (e.g., PDFs).
Employees can ask questions, summarize content, and collaborate across departments — boosting productivity and reducing information overload.
""")

# Features
st.subheader("💡 Key Features")
st.markdown("""
- 🔍 **Chat with PDF**: Ask contextual questions directly from the document content.  
- 📝 **Summarization**: Generate concise summaries from lengthy PDFs.  
- 🤝 **Team Collaboration**: Useful across legal, HR, compliance, and marketing.  
- 📬 **Email Delivery**: Send summaries straight to your inbox.  
- ⚙️ **Built on H2O Wave**: Real-time, interactive UI backed by Python.
""")

# Industry Applications
st.subheader("🏢 Industry Applications")
st.table({
    "Industry": ["Legal", "Marketing", "HR", "Compliance"],
    "Use Case": [
        "Review and summarize contract clauses",
        "Collaborate on campaign briefs and reports",
        "Answer onboarding queries from policy documents",
        "Extract regulatory terms from governance manuals"
    ]
})

# Technical Stack
st.subheader("🧰 Technical Stack")
st.markdown("""
| Component       | Technology                   |
|----------------|------------------------------|
| UI Framework   | [H2O Wave](https://wave.h2o.ai/) |
| Backend        | Python                       |
| LLM Engine     | H2OGPTe (RAG-based)          |
| PDF Handling   | PyMuPDF / pdfplumber         |
| Notifications  | SMTP (email summaries)       |
""", unsafe_allow_html=True)

# GitHub Link
st.markdown("---")
st.markdown("🔗 [View GitHub Repository](https://github.com/Sushi-KK/custom-gpt)", unsafe_allow_html=True)
