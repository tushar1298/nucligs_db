import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="NucLigs Database",
    page_icon="NucLigs.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------
# Hide Streamlit UI
# -------------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.stDeployButton {display:none;}

.block-container{
    padding:0rem;
    max-width:100%;
}

html, body, [class*="css"]{
    margin:0;
    padding:0;
}

iframe{
    border:none !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown("""
<div style="
    background:#060a14;
    padding:12px 20px;
    border-bottom:1px solid rgba(99,130,191,.2);
    display:flex;
    align-items:center;
    gap:10px;
">
    <img
        src="https://raw.githubusercontent.com/tushar1298/nucligs_db/main/NucLigs.png"
        style="
            height:68px;
            width:auto;
            border-radius:10px;
        "
    >
    <div>
        <h2 style="
            color:#38bdf8;
            margin:0;
            font-family:Arial;
            letter-spacing:1px;
        ">
            NucLigs Database : A Nucleotide and Nucleoside Analog Database
        </h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Cache HTML File
# -------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_html():
    html_path = Path("nucligs_visualizer.html")

    if not html_path.exists():
        return None

    return html_path.read_text(encoding="utf-8")

html_content = load_html()

# -------------------------------------------------------
# Render HTML
# -------------------------------------------------------
if html_content:

    components.html(
        html_content,
        height=1200,
        scrolling=True
    )

else:
    st.error(
        "nucligs_visualizer.html not found in app directory"
    )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown("""
<div style="
    text-align:center;
    color:#060a14;
    #margin-top:2px;
    font-size:14px;
    font-family:Arial;
    border-top:1px solid rgba(99,130,191,.1);
">
    Designed by Tushar Gupta and Dr. Pradeep Pant
</div>
<div style="
    text-align:center;
    padding:10px;
    color:#94a3b8;
    font-size:12px;
    background:#060a14;
">
    © NucLigs Database 2026 Version 1.0
</div>
""", unsafe_allow_html=True)
