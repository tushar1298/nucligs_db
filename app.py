import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import time # Imported to generate the unique non-cached string profiles

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
# Hide Streamlit UI & Strip Extra Borders/Margins
# -------------------------------------------------------
st.markdown("""
<style>

/* Hide native Streamlit layout infrastructure completely */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.stDeployButton {display:none;}
[data-testid="stHeader"] {background: rgba(0,0,0,0); height: 0rem;}

/* Remove all padding from the main app container frame */
.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
    margin: 0px !important;
}

/* Eliminate browser canvas boundary spaces */
html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    margin: 0 !important;
    padding: 0 !important;
    background-color: #060a14 !important; /* Forces the root page body background to seamlessly blend */
}

iframe {
    border: none !important;
    display: block;
}

/* Style and bind the header flex layout row safely */
[data-testid="stHorizontalBlock"] {
    background: #060a14 !important;
    padding: 0px 20px !important;
    border-bottom: 1px solid rgba(99,130,191,.2) !important;
    margin: 0 !important;
    gap: 0px !important;
    align-items: center !important;
}

/* Customize the native Streamlit link button */
div.stLinkButton {
    display: flex;
    justify-content: flex-end;
    width: auto !important;
}

div.stLinkButton > a {
    background-color: #38bdf8 !important;
    color: white !important;
    border: none !important;
    font-size: 28px !important;
    border-radius: 10px !important;
    padding: 8px 18px !important; /* Reduced padding inside to control box size profile */
    font-weight: 600 !important;
    max-width: 140px !important; /* Forces the box container boundaries tight */
    width: 140px !important;
    box-shadow: 0 4px 12px rgba(56,189,248,.25) !important;
    transition: background 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

div.stLinkButton > a:hover {
    background-color: #0ea5e9 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header Layout using Streamlit Columns
# -------------------------------------------------------
header_left, header_right = st.columns([0.88, 0.12]) # Modified ratios for clean button right-alignment space

with header_left:
    st.markdown("""
    <div style="display:flex; align-items:center; background:#060a14;">
        <img
            src="https://raw.githubusercontent.com/tushar1298/nucligs_db/main/NucLigs.png"
            style="
                height:68px;
                width:auto;
                border-radius:10px;
                margin-right:12px;
            "
        >
        <div>
            <h2 style="
                color:#38bdf8;
                margin:0;
                font-family:Arial;
                letter-spacing:1px;
                font-size:28px;
            ">
                NucLigs Database : A Nucleotide and Nucleoside Analog Database
            </h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

with header_right:
    # Generates custom dynamic endpoint configuration 
    nocache_suffix = str(int(time.time()))
    fresh_url = f"https://cdn.jsdelivr.net/gh/tushar1298/nucligs_db@main/tutorial.pdf?cb={nocache_suffix}"

    st.link_button(
        label="Tutorial", 
        url=fresh_url,
        use_container_width=False # Set to false to reject broad wrapper stretching
    )

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
    color:#94a3b8;
    font-size:28px;
    font-family:Arial;
    border-top:0px solid rgba(99,130,191,.1);
    background:#060a14;
    padding-top:0px;
">
    Designed by Tushar Gupta and Dr. Pradeep Pant
</div>
<div style="
    text-align:center;
    padding:10px 10px 20px 10px;
    color:#64748b;
    font-size:18px;
    background:#060a14;
">
    © NucLigs Database 2026 Version 1.0
</div>
""", unsafe_allow_html=True)
