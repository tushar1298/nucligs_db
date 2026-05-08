# -------------------------------------------------------
# App Header with Logo
# -------------------------------------------------------
import base64

logo_path = "nucligs_db/nucligs.png"

logo_base64 = ""

if Path(logo_path).exists():
    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <div style="
        background-color:#060a14;
        padding:12px 20px;
        border-bottom:1px solid rgba(99,130,191,.2);
        display:flex;
        align-items:center;
        gap:18px;
    ">

        <img src="data:image/png;base64,{logo_base64}"
             style="
                height:70px;
                width:auto;
                border-radius:10px;
             ">

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
