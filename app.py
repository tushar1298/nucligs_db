import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="NucLigs Database",
    page_icon="🧬",
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
        padding:10px 20px;
        border-bottom:1px solid rgba(99,130,191,.2);
    ">
        <h2 style="
            color:#38bdf8;
            margin:0;
            font-family:Arial;
            letter-spacing:1px;
        ">
            NucLigs Database — Nucleotide & Nucleoside Analog Database
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------
# HTML File Path
# -------------------------------------------------------
html_file = Path("nucligs_visualizer(4).html")

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
        "HTML file not found. Please place 'nucligs_visualizer(4).html' in the same folder as app.py"
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
        scrolling=True
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
        NucLigs Database Streamlit Interface
    </div>
    """,
    unsafe_allow_html=True
)
