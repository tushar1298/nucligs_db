import streamlit as st
import time  # Imported to generate unique cache-busting strings
from pathlib import Path

# --- Page Config ---
st.set_page_config(
    page_title="NucLigs Database",
    page_icon="NucLigs.png", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Define Paths ---
logo_path = Path(__file__).parent / "NucLigs.png"
if logo_path.exists():
    logo_src = str(logo_path)
else:
    logo_src = "https://raw.githubusercontent.com/tushar1298/nucligs_db/main/NucLigs.png"

# --- Custom CSS (Hide Streamlit UI & Style Elements) ---
st.markdown("""
<style>
    /* Hide Streamlit components */
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}
    .stDeployButton {display:none;}

    /* Adjust main container padding */
    .block-container {
        padding: 0rem 1rem;
        max-width: 100%;
    }

    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    /* --- Custom Styling for the Tutorial Button --- */
    .stLinkButton a {
        background-color: #38bdf8 !important;
        color: white !important;
        font-size: 24px !important;  
        font-weight: 700 !important; 
        padding: 15px 30px !important; 
        border-radius: 12px !important; 
        text-decoration: none !important;
        transition: background-color 0.2s ease;
    }

    .stLinkButton a:hover {
        background-color: #0ea5e9 !important;
    }

    .database-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
    }

    .logo-title-group {
        display: flex;
        align-items: center;
    }

    .app-title {
        color: #38bdf8; 
        margin-left: 15px;
        font-size: 28px; 
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# --- Header Layout ---
col_logo_title, col_button = st.columns([0.8, 0.2])

with col_logo_title:
    header_html = f"""
    <div class="database-header">
        <div class="logo-title-group">
            <img src="{logo_src}" style="height: 60px; border-radius: 10px;" alt="NucLigs Logo">
            <h1 class="app-title">NucLigs Database : A Nucleotide and Nucleoside Analog Database</h1>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

with col_button:
    # 1. Generate a unique epoch timestamp string (e.g., "1717871234")
    nocache_suffix = str(int(time.time()))
    
    # 2. Append it to the URL as a query parameter.
    # This tricks the CDN and browser into thinking it's a completely brand new request every page load.
    fresh_url = f"https://cdn.jsdelivr.net/gh/tushar1298/nucligs_db@main/tutorial.pdf?cb={nocache_suffix}"

    st.link_button(
        "Tutorial", 
        fresh_url, 
        use_container_width=True 
    )

# --- Subheader stats ---
st.markdown("""
<div style="color: grey; padding-bottom: 20px;">
    11,897 compounds | 6,122 analysis | 6,418 analysis
</div>
""", unsafe_allow_html=True)

# --- Main App Logic Placeholder ---
col_search, col_spacer = st.columns([0.8, 0.2])
with col_search:
    search_query = st.text_input("Search", placeholder="Search name, no, PDB ID, etc...")

st.warning("Database visualizer and compound exploration content is missing. Ensure the backend logic is correctly implemented.")

# --- Footer ---
st.markdown("""
<div style="text-align: center; color: grey; padding-top: 50px;">
    Developed by Tushar Gupta and Dr. Pradeep Pant
</div>
""", unsafe_allow_html=True)
