import streamlit as st
from utils import extract_text_from_pdf
from matcher import calculate_similarity

st.title("📄 EU Job Match Pro")

cv_file = st.file_uploader("Upload your CV (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description here")

if st.button("Match Now"):
    if cv_file and jd_text.strip() != "":
        cv_text = extract_text_from_pdf(cv_file)
        score = calculate_similarity(cv_text, jd_text)
        st.success(f"✅ Match Score: {score}%")
        if score >= 80:
            st.info("Great match! 🔥")
        elif score >= 50:
            st.warning("Average match. Improve your CV.")
        else:
            st.error("Low match. Customize your resume.")
    else:
        st.error("Please upload your CV and paste the job description.")
