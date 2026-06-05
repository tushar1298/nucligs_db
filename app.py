import streamlit as st
from pathlib import Path

# --- Page Config ---
st.set_page_config(
    page_title="NucLigs Database",
    page_icon="NucLigs.png",  # Ensure this file exists or use st.image
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Define Paths ---
# Adjust this to point to your NucLigs logo file
logo_path = Path(__file__).parent / "NucLigs.png"
if logo_path.exists():
    logo_src = str(logo_path)
else:
    logo_src = "https://raw.githubusercontent.com/tushar1298/nucligs_db/main/NucLigs.png" # Fallback to URL

# --- Custom CSS (Hide Streamlit UI & Style Elements) ---
# We use this section to also style the Tutorial button text size
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

    /* Standardize typography (optional but recommended for a dark theme) */
    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    /* --- Custom Styling for the Tutorial Button --- */
    /* Target the link in the native Streamlit button to increase text size */
    .stLinkButton a {
        background-color: #38bdf8 !important;
        color: white !important;
        font-size: 24px !important;  /* CRITICAL: Increased font size here */
        font-weight: 700 !important; /* Bold for readability */
        padding: 15px 30px !important; /* Adjust padding to accommodate larger text */
        border-radius: 12px !important; /* Match your image's style */
        text-decoration: none !important;
        transition: background-color 0.2s ease;
    }

    .stLinkButton a:hover {
        background-color: #0ea5e9 !important;
    }

    /* Custom Header and Title style to match input image color */
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
        color: #38bdf8; /* The requested blue color */
        margin-left: 15px;
        font-size: 28px; /* Standardize font size for the main title */
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# --- Header Layout (Manual Layout instead of markdown to allow link_button) ---
# Column layout allows st.link_button to work natively
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
    # Use native st.link_button to ensure it opens in a new tab correctly.
    # The CSS defined above targets this button.
    st.link_button(
        "Tutorial", 
        "https://cdn.jsdelivr.net/gh/tushar1298/nucligs_db@main/tutorial.pdf", 
        use_container_width=True # Fills the column width for a prominent box
    )

# --- Subheader stats (Example placeholders for image fidelity) ---
st.markdown("""
<div style="color: grey; padding-bottom: 20px;">
    11,897 compounds | 6,122 analysis | 6,418 analysis
</div>
""", unsafe_allow_html=True)


# --- Main App Logic (Place your visualizer/search logic here) ---
# Example visual elements from the input image to build structure.
if st.button("Download PDF"):
    st.info("PDF Generation requested (functionality depends on implementation).")

col_search, col_spacer = st.columns([0.8, 0.2])
with col_search:
    search_query = st.text_input("Search", placeholder="Search name, no, PDB ID, etc...")
    st.markdown("""<div style="color: red;">CR</div>""", unsafe_allow_html=True) # Placeholder CR indicator

st.warning("Database visualizer and compound exploration content is missing. Ensure the backend logic is correctly implemented.")

# --- Footer or Other content ---
st.markdown("""
<div style="text-align: center; color: grey; padding-top: 50px;">
    Developed by Tushar Gupta and Dr. Pradeep Pant
</div>
""", unsafe_allow_html=True)
