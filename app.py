import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.preprocessing import preprocess_text

st.set_page_config(
    page_title="AI Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Candidate Ranking Tool")

st.markdown("---")

st.subheader("Upload Job Description")

job_description = st.file_uploader(
    "Upload Job Description (.txt)",
    type=["txt"]
)

st.markdown("---")

st.subheader("Upload Candidate Resumes")

resume_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

st.markdown("---")

if st.button("Start Screening"):
    if job_description is None:
        st.error("Please upload a Job Description.")
    elif len(resume_files) == 0:
        st.error("Please upload at least one resume.")
    else:
        st.success("Files uploaded successfully!")
        for resume in resume_files:
            text= extract_text_from_pdf(resume)
            clean_text = preprocess_text(text)

            st.subheader(resume.name)

            st.text_area(
                "Cleaned Resume Text",
                text[:2500],
                height=250
            )
