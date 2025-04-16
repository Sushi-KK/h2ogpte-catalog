import streamlit as st
import json

# Load metadata
with open("use_case_metadata.json", "r") as f:
    use_cases = json.load(f)

st.set_page_config(page_title="H2O.ai Catalog", layout="wide")

# ----------------------------
# Custom CSS for Layout & Font
# ----------------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Hind:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Hind', sans-serif;
        }

        .centered-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 1rem 2rem;
        }

        .title-highlight {
            font-size: 2.8rem;
            font-weight: 700;
            text-align: center;
        }

        .title-highlight span {
            background-color: #FFD54F;
            padding: 0 0.4rem;
            border-radius: 4px;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
            margin-bottom: 2rem;
        }

        .tile {
            background-color: #fff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .tag {
            display: inline-block;
            background-color: #ffecb3;
            color: #444;
            font-size: 0.75rem;
            padding: 0.2rem 0.6rem;
            margin-right: 0.3rem;
            margin-top: 0.3rem;
            border-radius: 12px;
        }

        .arrow-button {
            text-align: right;
            font-size: 1.5rem;
            color: #f9a825;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Begin centered container
# ----------------------------
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

# ----------------------------
# Title and Subtitle
# ----------------------------
st.markdown('<div class="title-highlight">H2O.ai <span>Catalog</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Collection of h2oGPTe Use Cases</div>', unsafe_allow_html=True)

# ----------------------------
# Filters (Side by Side)
# ----------------------------
with st.expander("🔍 Search for a particular use case in this catalog", expanded=True):
    industries = sorted(set(uc["industry"] for uc in use_cases))
    problems = sorted(set(uc["problem_type"] for uc in use_cases))

    col1, col2 = st.columns(2)
    with col1:
        selected_industry = st.selectbox("Industry", ["All"] + industries)
    with col2:
        selected_problem = st.selectbox("Problem Type", ["All"] + problems)

# ----------------------------
# Filter Logic
# ----------------------------
def matches_filters(uc):
    return (
        (selected_industry == "All" or uc["industry"] == selected_industry) and
        (selected_problem == "All" or uc["problem_type"] == selected_problem)
    )

filtered = [uc for uc in use_cases if matches_filters(uc)]

# ----------------------------
# Tile Grid Display
# ----------------------------
cols = st.columns(3)
if filtered:
    for idx, case in enumerate(filtered):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="tile">
                    <div>
                        <div style="font-size:1.6rem;">🔥</div>
                        <h4 style="margin-top:0.2rem;">{case['title']}</h4>
                        <p>{case['description']}</p>
                        {"".join(f"<span class='tag'>{tag}</span>" for tag in case['tags'])}
                    </div>
                    <div class="arrow-button">➜</div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.warning("No use cases match your selected filters.")

# ----------------------------
# End centered container
# ----------------------------
st.markdown('</div>', unsafe_allow_html=True)
