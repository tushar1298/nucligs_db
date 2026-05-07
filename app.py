import streamlit as st
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
