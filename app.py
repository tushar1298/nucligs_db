import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="NucLigs Database",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------
# Hide Streamlit Default UI
# -------------------------------------------------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}

.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}

html, body, [class*="css"] {
    margin: 0;
    padding: 0;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------------------------------------------
# App Header
# -------------------------------------------------------
st.markdown(
    """
    <div style="
        background-color:#060a14;
        padding:12px 20px;
        border-bottom:1px solid rgba(99,130,191,.2);
        display:flex;
        align-items:center;
        gap:18px;
    ">
        <img 
            src="https://raw.githubusercontent.com/tushar1298/nucligs_db/main/NucLigs.png"
            style="
                height:72px;
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
                NucLigs Database — Nucleotide & Nucleoside Analog Database
            </h2>
            <h4 style="
                color:#94a3b8;
                margin-top:6px;
                margin-bottom:0;
                font-family:Arial;
                font-weight:400;
                letter-spacing:.5px;
            ">
                Designed by Tushar Gupta and Dr. Pradeep Pant
            </h4>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# -------------------------------------------------------
# HTML File Path
# -------------------------------------------------------
html_file = Path("nucligs_visualizer.html")

# -------------------------------------------------------
# Load and Render HTML
# -------------------------------------------------------
if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")

    components.html(
        html_content,
        height=2500,
        scrolling=True
    )

else:
    st.error(
        "HTML file not found. Please place 'nucligs_visualizer.html' in the same folder as app.py"
    )

# -------------------------------------------------------
# Optional File Upload Helper
# -------------------------------------------------------
st.sidebar.title("Upload HTML File")

uploaded_html = st.sidebar.file_uploader(
    "Upload HTML File",
    type=["html", "htm"]
)

if uploaded_html is not None:
    html_data = uploaded_html.read().decode("utf-8")

    st.success("HTML File Loaded Successfully")

    components.html(
        html_data,
        height=2500,
        scrolling=False
    )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown(
    """
    <div style="
        text-align:center;
        padding:10px;
        color:#94a3b8;
        font-size:12px;
        background:#060a14;
        border-top:1px solid rgba(99,130,191,.1);
    ">
        NucLigs Database 2026 Verson 1.0
    </div>
    """,
    unsafe_allow_html=True
)
